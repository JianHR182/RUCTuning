import threading
import time

import numpy as np
import paramiko
import psycopg2

import config
import utils


class Database:
    def __init__(self):
        self.host = config.host
        self.port = config.port
        self.database = config.db
        self.user = config.user
        self.password = config.password
        self.omm_password = config.omm_password
        self.data_path = config.opengauss_node_path
        self.knobs = utils.get_knobs_detail(config.knobs_file, config.knobs_number)
        self.ssh = None
        self.get_ssh()
        self.logger = utils.get_logger('log/db_log/{}.log'.format(int(time.time())))
        self.restart_flag = False

    def get_conn(self):
        return psycopg2.connect(database=self.database,
                                user=self.user,
                                password=self.password,
                                host=self.host,
                                port=int(self.port))

    def get_ssh(self):
        if self.ssh is None:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.host,
                             port=22,
                             username='omm',
                             password=self.omm_password
                             )
        return self.ssh

    def restart(self):
        self.restart_flag = False
        ssh = self.get_ssh()
        print('database restarting...')
        _, stdout, stderr = ssh.exec_command('gs_om -t restart')
        info = stdout.read().decode('utf-8')
        self.logger.info(info)
        if info.find("Successfully started") != -1:
            print('database restart successfully')
            self.restart_flag = True

    def restore(self):
        ssh = self.get_ssh()
        _, stdout, stderr = ssh.exec_command('cp {}/postgresql_bak.conf {}/postgresql.conf'.format(self.data_path, self.data_path))
        self.restart()

    def fetch_knob(self):
        conn = self.get_conn()
        knobs = {}
        cursor = conn.cursor()
        for knob in self.knobs:
            sql = "SELECT name, setting FROM pg_settings WHERE name='{}'".format(knob)
            cursor.execute(sql)
            result = cursor.fetchall()
            for s in result:
                if self.knobs[knob]['type'] == 'integer' or self.knobs[knob]['type'] == 'int64':
                    knobs[knob] = int(s[1])
                elif self.knobs[knob]['type'] == 'real':
                    knobs[knob] = float(s[1])
                else:
                    knobs[knob] = s[1]
        cursor.close()
        conn.close()
        return knobs

    def fetch_inner_metric(self):
        state_list = []
        conn = self.get_conn()
        ssh = self.get_ssh()
        cursor = conn.cursor()

        # ['cpu_useage','memory_useage','kB_rd/s','kB_wr/s','cache_hit_rate','concurrent_users','lock_wait_count','error_rate','logical_reads_per_second','physical_reads_per_second','active_session','transactions_per_second','rows_scanned_per_second','rows_updated_per_second','rows_deleted_per_second']
        # cpu和内存占用率s
        stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
        lines = stdout.readlines()
        gaussdb_line = None
        for line in lines:
            if 'gaussdb' in line:
                gaussdb_line = line
                break
        if gaussdb_line:
            columes = gaussdb_line.split()
            cpu_usage = columes[8]
            state_list.append(cpu_usage)
            mem_usage = columes[9]
            state_list.append(mem_usage)
        else:
            print("gaussdb process not found in top output.")

        # 每秒读取和写入的kB数，kB_rd/s,kB_wr/s
        stdin, stdout, stderr = ssh.exec_command("pidstat -d")
        lines = stdout.readlines()[1:]
        gaussdb_line = None
        for line in lines:
            if 'gaussdb' in line:
                gaussdb_line = line
                break
        if gaussdb_line:
            columes = gaussdb_line.split()
            kB_rd = columes[3]
            state_list.append(kB_rd)
            kB_wr = columes[4]
            state_list.append(kB_wr)
        else:
            print("gaussdb process not found in pidstat")

        # cache_hit_rate
        cache_hit_rate_sql = "select blks_hit / (blks_read + blks_hit + 0.001) " \
                             "from pg_stat_database " \
                             "where datname = '{}';".format(self.database)

        # 并发用户数量
        concurrent_users = """
        SELECT
            count(DISTINCT usename)
        AS
            concurrent_users
        FROM
            pg_stat_activity
        WHERE
            state = 'active';
        """

        # 锁等待次数
        lock = """
        SELECT
            count(*) AS lock_wait_count
        FROM
            pg_stat_activity
        WHERE
            waiting = true;
        """

        # 错误率
        error_rate = """
        SELECT
            (sum(xact_rollback) + sum(conflicts) + sum(deadlocks)) / (sum(xact_commit) + sum(xact_rollback) + sum(conflicts) + sum(deadlocks)) AS error_rate
        FROM
            pg_stat_database;
        """

        # 逻辑读/秒和物理读/秒
        read = """
        SELECT
            logical_reads / (extract(epoch from now() - stats_reset)) AS logical_reads_per_second,
            physical_reads / (extract(epoch from now() - stats_reset)) AS physical_reads_per_second
        FROM (
            SELECT
                sum(tup_returned + tup_fetched) AS logical_reads,
                sum(blks_read) AS physical_reads,
                max(stats_reset) AS stats_reset
            FROM
                pg_stat_database
            ) subquery;
        """

        # 活跃会话数量
        active_session = """
        SELECT
            count(*) AS active_session
        FROM
            pg_stat_activity;
        """

        # 每秒提交的事务数
        transactions_per_second = """
        SELECT
            total_commits / (extract(epoch from now() - max_stats_reset)) AS transactions_per_second
        FROM (
            SELECT
            sum(xact_commit) AS total_commits,
            max(stats_reset) AS max_stats_reset
        FROM
            pg_stat_database
            ) subquery;
        """

        # 扫描行、更新行和删除行
        tup = """
        SELECT
            rows_scanned / (extract(epoch from now() - max_stats_reset)) AS rows_scanned_per_second,
            rows_updated / (extract(epoch from now() - max_stats_reset)) AS rows_updated_per_second,
             rows_deleted / (extract(epoch from now() - max_stats_reset)) AS rows_deleted_per_second
        FROM (
            SELECT
            sum(tup_returned) AS rows_scanned,
            sum(tup_updated) AS rows_updated,
            sum(tup_deleted) AS rows_deleted,
            max(stats_reset) AS max_stats_reset
            FROM
             pg_stat_database
            ) subquery;
        """

        try:
            cursor.execute(cache_hit_rate_sql)
            result = cursor.fetchall()
            for s in result:
                state_list.append(float(s[0]))

            # 并发用户数量
            cursor.execute(concurrent_users)
            result = cursor.fetchall()
            state_list.append(float(result[0][0]))

            # 锁等待次数
            cursor.execute(lock)
            result = cursor.fetchall()
            state_list.append(float(result[0][0]))

            # 错误率
            cursor.execute(error_rate)
            result = cursor.fetchall()
            state_list.append(float(result[0][0]))

            # 逻辑读和物理读
            cursor.execute(read)
            result = cursor.fetchall()
            # print(result)
            for i in result[0]:
                state_list.append(float(i))

            # 活跃会话数
            cursor.execute(active_session)
            result = cursor.fetchall()
            # print(result)
            state_list.append(float(result[0][0]))

            # 每秒提交的事务
            cursor.execute(transactions_per_second)
            result = cursor.fetchall()
            # print(result)
            state_list.append(float(result[0][0]))

            # 扫描、更新、删除行
            cursor.execute(tup)
            result = cursor.fetchall()
            for i in result[0]:
                state_list.append(float(i))

            cursor.close()
            conn.close()
        except Exception as error:
            print(error)
        for i in range(len(state_list)):
            state_list[i] = float(state_list[i])
        return state_list

    def change_knob(self, knobs):
        ssh = self.get_ssh()
        print('修改配置参数...')
        for knob in knobs:
            # integer
            if self.knobs[knob]['type'] == 'integer' or self.knobs[knob]['type'] == 'int64':
                val = int(knobs[knob])
            # real
            elif self.knobs[knob]['type'] == 'real':
                val = float(knobs[knob])
            # string, bool, enum
            else:
                val = knobs[knob]
            _, stdout, stderr = ssh.exec_command('gs_guc set -c "{}={}" -D {}'.format(knob, val, self.data_path))
            info = stdout.read().decode('utf-8')
            if info.find("Success") == -1:
                self.logger.info(info)

        # 离线调优重启数据库, 若失败则还原postgresql.conf
        if not config.online:
            t = threading.Thread(target=self.restart)
            t.setDaemon(True)
            t.start()

            t.join(timeout=config.time_wait)
            if not self.restart_flag:
                self.restore()
                print('restore database')

        return self.restart_flag
