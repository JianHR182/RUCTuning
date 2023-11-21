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
        self.knobs = utils.get_knobs_detail(config.knobs_file)
        self.ssh = None
        self.get_ssh()
        self.logger = utils.get_logger('log/db_log/{}.log'.format(int(time.time())))
        self.restart_flag = False

    # 获取数据库远程连接
    def get_conn(self):
        return psycopg2.connect(database=self.database,
                                user=self.user,
                                password=self.password,
                                host=self.host,
                                port=int(self.port))

    # 获取数据库所在机器的SSH连接, 用于执行修改参数的命令, 重启数据库等
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

    # 数据库重启
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

    # 数据库恢复
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
                if self.knobs[knob]['vartype'] == 'integer' or self.knobs[knob]['vartype'] == 'int64':
                    knobs[knob] = int(s[1])
                elif self.knobs[knob]['vartype'] == 'real':
                    knobs[knob] = float(s[1])
                else:
                    knobs[knob] = s[1]
        cursor.close()
        conn.close()
        return knobs

    # 获取数据库状态信息, 机器信息等, 用于知识匹配
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

        '''
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
        '''

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
            '''
            # 缓存命中率
            cursor.execute(cache_hit_rate_sql)
            result = cursor.fetchall()
            for s in result:
                state_list.append(float(s[0]))
            '''

            # 并发用户数量
            cursor.execute(concurrent_users)
            result = cursor.fetchall()
            state_list.append(float(result[0][0]))

            '''
            # 锁等待次数
            cursor.execute(lock)
            result = cursor.fetchall()
            state_list.append(float(result[0][0]))
            '''

            # 错误率
            cursor.execute(error_rate)
            result = cursor.fetchall()
            state_list.append(float(result[0][0]))

            '''
            # 逻辑读和物理读
            cursor.execute(read)
            result = cursor.fetchall()
            # print(result)
            for i in result[0]:
                state_list.append(float(i))
            '''

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

            '''
            # 扫描、更新、删除行
            cursor.execute(tup)
            result = cursor.fetchall()
            for i in result[0]:
                state_list.append(float(i))
            '''

            cursor.close()
            conn.close()
        except Exception as error:
            print(error)
        for i in range(len(state_list)):
            state_list[i] = float(state_list[i])
        return state_list

    # 修改配置参数
    def change_knob(self, knobs):
        ssh = self.get_ssh()
        print('修改配置参数...')
        for knob in knobs:
            # 在线调优仅修改经过筛选的参数(无需重启, 重要的)
            if knob not in self.knobs:
                continue

            # integer
            if self.knobs[knob]['vartype'] == 'integer' or self.knobs[knob]['vartype'] == 'int64':
                val = int(knobs[knob])
            # real
            elif self.knobs[knob]['vartype'] == 'real':
                val = float(knobs[knob])
            # string, bool, enum
            else:
                val = knobs[knob]
            if config.online:
                _, stdout, stderr = ssh.exec_command('gs_guc set -c "{}={}" -D {}'.format(knob, val, self.data_path))
            else:
                _, stdout, stderr = ssh.exec_command('gs_guc reload -c "{}={}" -D {}'.format(knob, val, self.data_path))
            info = stdout.read().decode('utf-8')
            if info.find("Success") == -1:
                self.logger.info(info)

        # 离线调优重启数据库, 若失败则还原postgresql.conf
        if not config.online:
            t = threading.Thread(target=self.restart)
            t.setDaemon(True)
            t.start()
            # 在time_wait时间内若重启失败, 则认为由于配置参数取值不合理导致数据库故障, 故恢复重置
            t.join(timeout=config.time_wait)
            if not self.restart_flag:
                self.restore()
                print('restore database')

        return self.restart_flag



    def get_snapshot(self):
        if not config.online:
            conn = psycopg2.connect(database=config.mon_db,
                                    user=config.mon_user,
                                    password=config.mon_password,
                                    host=config.host,
                                    port=int(config.port))
            cursor = conn.cursor()
            # 手动创建快照，并且快照刚刚创建查不到，需要稍等一下
            cursor.execute("select create_wdr_snapshot();")
            print("快照正在创建中，请稍候……")
            time.sleep(60)
            # 获取快照id
            cursor.execute("select * from snapshot.snapshot order by start_ts desc limit 5;")
            lines = cursor.fetchall()
            snap_id = str(lines[0][0])
            cursor.close()
            conn.close()
            return snap_id
        else:
            conn = psycopg2.connect(database=config.mon_db,
                                    user=config.mon_user,
                                    password=config.mon_password,
                                    host=config.host,
                                    port=int(config.port))
            cursor = conn.cursor()
            # 获取快照id
            cursor.execute("select * from snapshot.snapshot order by start_ts desc limit 5;")
            lines = cursor.fetchall()
            begin = str(lines[1][0])
            end = str(lines[0][0])
            cursor.close()
            conn.close()
            return begin, end

    def get_wdr_metric(self, begin_num:str, end_num:str):
        # 使用有监控权限的用户连接postgres数据库
        conn = psycopg2.connect(database=config.mon_db,
                                user=config.mon_user,
                                password=config.mon_password,
                                host=config.host,
                                port=int(config.port))
        cursor = conn.cursor()
        target = {}
        begin = begin_num
        end = end_num
        node_name_sql = 'select node_name as "Host Node Name" from pg_node_env;'
        cursor.execute(node_name_sql)
        result = cursor.fetchall()
        node_name = result[0][0]
        # print(node_name)


        # 效率百分比
        eff_sql = f'''
        select 
        unnest(array['Buffer Hit', 'Effective CPU']) as "Metric Name", 
        unnest(array[case when s1.all_reads = 0 then 1 else round(s1.blks_hit * 100 / s1.all_reads) end, s2.cpu_to_elapsd]) as "Metric Value" 
        from 
        (select (snap_2.all_reads - coalesce(snap_1.all_reads, 0)) as all_reads, 
                (snap_2.blks_hit - coalesce(snap_1.blks_hit, 0)) as blks_hit 
        from 
                (select sum(coalesce(snap_blks_read, 0) + coalesce(snap_blks_hit, 0)) as all_reads, 
                        coalesce(sum(snap_blks_hit), 0) as blks_hit 
                from snapshot.snap_summary_stat_database 
                where snapshot_id = {begin}) snap_1, 
                    (select sum(coalesce(snap_blks_read, 0) + coalesce(snap_blks_hit, 0)) as all_reads, 
                        coalesce(sum(snap_blks_hit), 0) as blks_hit 
                    from snapshot.snap_summary_stat_database 
                    where snapshot_id = {end}) snap_2 
                ) s1, 
                (select round(cpu_time.snap_value * 100 / greatest(db_time.snap_value, 1)) as cpu_to_elapsd 
                from 
                    (select coalesce(snap_2.snap_value, 0) - coalesce(snap_1.snap_value, 0) as snap_value 
                    from 
                        (select snap_stat_name, snap_value from snapshot.snap_global_instance_time 
                        where snapshot_id = {begin} and snap_stat_name = 'CPU_TIME') snap_1, 
                        (select snap_stat_name, snap_value from snapshot.snap_global_instance_time 
                        where snapshot_id = {end} and snap_stat_name = 'CPU_TIME') snap_2) cpu_time, 
                    (select coalesce(snap_2.snap_value, 0) - coalesce(snap_1.snap_value, 0) as snap_value 
                    from 
                        (select snap_stat_name, snap_value from snapshot.snap_global_instance_time 
                        where snapshot_id = {begin} and snap_stat_name = 'DB_TIME') snap_1, 
                        (select snap_stat_name, snap_value from snapshot.snap_global_instance_time 
                        where snapshot_id = {end} and snap_stat_name = 'DB_TIME') snap_2) db_time 
                ) s2;
        '''
        # 获得 'Buffer Hit'，'Effective CPU'
        cursor.execute(eff_sql)
        result = cursor.fetchall()
        for i in result:
            target[i[0]] = int(i[1])
            # print(i)
        # print(target)

        # 等待类型
        wait_sql = f"""
        select 
            snap_2.type as "Wait Class", 
            (snap_2.wait - snap_1.wait) as "Waits", 
            (snap_2.total_wait_time - snap_1.total_wait_time) as "Total Wait Time(us)", 
            round((snap_2.total_wait_time - snap_1.total_wait_time) / greatest((snap_2.wait - snap_1.wait), 1)) as "Wait Avg(us)" 
        from 
            (select 
                snap_type as type, 
                sum(snap_total_wait_time) as total_wait_time, 
                sum(snap_wait) as wait from snapshot.snap_global_wait_events 
            where snapshot_id = {end} 
            and snap_nodename = '{node_name}' 
            and snap_event != 'unknown_lwlock_event' 
            and snap_event != 'none' 
            group by snap_type) snap_2 
            left join 
            (select 
                snap_type as type, 
                sum(snap_total_wait_time) as total_wait_time, 
                sum(snap_wait) as wait 
            from snapshot.snap_global_wait_events 
            where snapshot_id = {begin} 
            and  snap_nodename = '{node_name}' 
            and  snap_event != 'unknown_lwlock_event' and snap_event != 'none' 
            group by snap_type) snap_1 
            on snap_2.type = snap_1.type 
            order by "Total Wait Time(us)" desc;
        """
        # 等待轻量级锁 LWLOCK_EVENT; 等待事务锁
        cursor.execute(wait_sql)
        result = cursor.fetchall()
        for i in result:
            if i[0] == 'LOCK_EVENT':
                target["LOCK_EVENT_NUM"] = int(i[1])
                target["LOCK_EVENT_TIME"] = int(i[2])
            elif i[0] == 'LWLOCK_EVENT':
                target["LWLOCK_EVENT_NUM"] = int(i[1])
                target["LWLOCK_EVENT_TIME"] = int(i[2])
            # print(i)
        # print(target)



        """
        此部分仅统计了top200的sql,
        系WDR报告本身仅统计前200条sql
        后续如果需要实现全部sql可通过查表实现统计,
        但是全部sql或许过于冗余,
        并且计算的均为总数而非每秒。
        """
        # SQL order by Rows Returned
        rows_return_sql = f"""
        select 	t2.snap_unique_sql_id 												  as "Unique SQL Id", 
                t2.snap_user_name 	  												  as "User Name",
                (t2.snap_total_elapse_time - coalesce(t1.snap_total_elapse_time, 0))  as "Total Elapse Time(us)", 
                (t2.snap_n_calls - coalesce(t1.snap_n_calls, 0))                      as "Calls", 
                round("Total Elapse Time(us)"/greatest("Calls", 1), 0)                as "Avg Elapse Time(us)", 
                t2.snap_min_elapse_time 	    				      as "Min Elapse Time(us)", 
                t2.snap_max_elapse_time 					      as "Max Elapse Time(us)", 
                (t2.snap_n_returned_rows - coalesce(t1.snap_n_returned_rows, 0))      as "Returned Rows", 
                ((t2.snap_n_tuples_fetched - coalesce(t1.snap_n_tuples_fetched, 0)) + 
                (t2.snap_n_tuples_returned - coalesce(t1.snap_n_tuples_returned, 0))) as "Tuples Read", 
                ((t2.snap_n_tuples_inserted - coalesce(t1.snap_n_tuples_inserted, 0)) + 
                (t2.snap_n_tuples_updated - coalesce(t1.snap_n_tuples_updated, 0)) + 
                (t2.snap_n_tuples_deleted - coalesce(t1.snap_n_tuples_deleted, 0)))   as "Tuples Affected", 
                (t2.snap_n_blocks_fetched - coalesce(t1.snap_n_blocks_fetched, 0))    as "Logical Read", 
                ((t2.snap_n_blocks_fetched - coalesce(t1.snap_n_blocks_fetched, 0)) - 
                (t2.snap_n_blocks_hit - coalesce(t1.snap_n_blocks_hit, 0)))           as "Physical Read", 
                (t2.snap_cpu_time - coalesce(t1.snap_cpu_time, 0)) 		      as "CPU Time(us)", 
                (t2.snap_data_io_time - coalesce(t1.snap_data_io_time, 0)) 	      as "Data IO Time(us)", 
                (t2.snap_sort_count - coalesce(t1.snap_sort_count, 0)) 		      as "Sort Count", 
                (t2.snap_sort_time - coalesce(t1.snap_sort_time, 0)) 		      as "Sort Time(us)", 
                (t2.snap_sort_mem_used - coalesce(t1.snap_sort_mem_used, 0)) 	      as "Sort Mem Used(KB)", 
                (t2.snap_sort_spill_count - coalesce(t1.snap_sort_spill_count, 0))    as "Sort Spill Count", 
                (t2.snap_sort_spill_size - coalesce(t1.snap_sort_spill_size, 0))      as "Sort Spill Size(KB)", 
                (t2.snap_hash_count - coalesce(t1.snap_hash_count, 0)) 		      as "Hash Count", 
                (t2.snap_hash_time - coalesce(t1.snap_hash_time, 0)) 		      as "Hash Time(us)", 
                (t2.snap_hash_mem_used - coalesce(t1.snap_hash_mem_used, 0)) 	      as "Hash Mem Used(KB)", 
                (t2.snap_hash_spill_count - coalesce(t1.snap_hash_spill_count, 0))    as "Hash Spill Count", 
                (t2.snap_hash_spill_size - coalesce(t1.snap_hash_spill_size, 0))      as "Hash Spill Size(KB)", 
                LEFT(t2.snap_query, 25) 					      as "SQL Text" 
        from 
                (select * from snapshot.snap_summary_statement where snapshot_id = {begin} and snap_node_name = '{node_name}') t1
                right join 
                (select * from snapshot.snap_summary_statement where snapshot_id = {end} and snap_node_name = '{node_name}') t2
                on t1.snap_unique_sql_id = t2.snap_unique_sql_id 
                and t1.snap_user_id = t2.snap_user_id 
                order by "Returned Rows" 
                desc limit 200;
        """
        # Rows_Return
        # print(rows_return_sql)
        cursor.execute(rows_return_sql)
        result = cursor.fetchall()
        rows_return = 0
        for i in result:
            # print(i[7])
            # print(type(i[7]))
            if i[7] == 0 :
                break
            rows_return += i[7]
            # print(i[7])
        target['Rows_Return'] = rows_return
        # print(target)


        # SQL order by Tuples Reads
        tuples_read_sql = f"""
        select 	t2.snap_unique_sql_id 												  as "Unique SQL Id", 
                t2.snap_user_name 	  												  as "User Name",
                (t2.snap_total_elapse_time - coalesce(t1.snap_total_elapse_time, 0))  as "Total Elapse Time(us)", 
                (t2.snap_n_calls - coalesce(t1.snap_n_calls, 0))                      as "Calls", 
                round("Total Elapse Time(us)"/greatest("Calls", 1), 0)                as "Avg Elapse Time(us)", 
                t2.snap_min_elapse_time 	    				      as "Min Elapse Time(us)", 
                t2.snap_max_elapse_time 					      as "Max Elapse Time(us)", 
                (t2.snap_n_returned_rows - coalesce(t1.snap_n_returned_rows, 0))      as "Returned Rows", 
                ((t2.snap_n_tuples_fetched - coalesce(t1.snap_n_tuples_fetched, 0)) + 
                (t2.snap_n_tuples_returned - coalesce(t1.snap_n_tuples_returned, 0))) as "Tuples Read", 
                ((t2.snap_n_tuples_inserted - coalesce(t1.snap_n_tuples_inserted, 0)) + 
                (t2.snap_n_tuples_updated - coalesce(t1.snap_n_tuples_updated, 0)) + 
                (t2.snap_n_tuples_deleted - coalesce(t1.snap_n_tuples_deleted, 0)))   as "Tuples Affected", 
                (t2.snap_n_blocks_fetched - coalesce(t1.snap_n_blocks_fetched, 0))    as "Logical Read", 
                ((t2.snap_n_blocks_fetched - coalesce(t1.snap_n_blocks_fetched, 0)) - 
                (t2.snap_n_blocks_hit - coalesce(t1.snap_n_blocks_hit, 0)))           as "Physical Read", 
                (t2.snap_cpu_time - coalesce(t1.snap_cpu_time, 0)) 		      as "CPU Time(us)", 
                (t2.snap_data_io_time - coalesce(t1.snap_data_io_time, 0)) 	      as "Data IO Time(us)", 
                (t2.snap_sort_count - coalesce(t1.snap_sort_count, 0)) 		      as "Sort Count", 
                (t2.snap_sort_time - coalesce(t1.snap_sort_time, 0)) 		      as "Sort Time(us)", 
                (t2.snap_sort_mem_used - coalesce(t1.snap_sort_mem_used, 0)) 	      as "Sort Mem Used(KB)", 
                (t2.snap_sort_spill_count - coalesce(t1.snap_sort_spill_count, 0))    as "Sort Spill Count", 
                (t2.snap_sort_spill_size - coalesce(t1.snap_sort_spill_size, 0))      as "Sort Spill Size(KB)", 
                (t2.snap_hash_count - coalesce(t1.snap_hash_count, 0)) 		      as "Hash Count", 
                (t2.snap_hash_time - coalesce(t1.snap_hash_time, 0)) 		      as "Hash Time(us)", 
                (t2.snap_hash_mem_used - coalesce(t1.snap_hash_mem_used, 0)) 	      as "Hash Mem Used(KB)", 
                (t2.snap_hash_spill_count - coalesce(t1.snap_hash_spill_count, 0))    as "Hash Spill Count", 
                (t2.snap_hash_spill_size - coalesce(t1.snap_hash_spill_size, 0))      as "Hash Spill Size(KB)", 
                LEFT(t2.snap_query, 25) 					      as "SQL Text" 
        from 
                (select * from snapshot.snap_summary_statement where snapshot_id = {begin} and snap_node_name = '{node_name}') t1
                right join 
                (select * from snapshot.snap_summary_statement where snapshot_id = {end} and snap_node_name = '{node_name}') t2
                on t1.snap_unique_sql_id = t2.snap_unique_sql_id 
                and t1.snap_user_id = t2.snap_user_id 
                order by "Tuples Read" 
                desc limit 200;
        """
        # tuples_read
        # print(tuples_read_sql)
        cursor.execute(tuples_read_sql)
        result = cursor.fetchall()
        tuples_read = 0
        for i in result:
            # print(i[8])
            # print(type(i[8]))
            if i[8] == 0:
                break
            tuples_read += i[8]
        target['Tuples_Read'] = tuples_read
        # print(target)



        # SQL order by Physical Reads
        physical_read_sql = f"""
        select 	t2.snap_unique_sql_id 												  as "Unique SQL Id", 
                t2.snap_user_name 	  												  as "User Name",
                (t2.snap_total_elapse_time - coalesce(t1.snap_total_elapse_time, 0))  as "Total Elapse Time(us)", 
                (t2.snap_n_calls - coalesce(t1.snap_n_calls, 0))                      as "Calls", 
                round("Total Elapse Time(us)"/greatest("Calls", 1), 0)                as "Avg Elapse Time(us)", 
                t2.snap_min_elapse_time 	    				      as "Min Elapse Time(us)", 
                t2.snap_max_elapse_time 					      as "Max Elapse Time(us)", 
                (t2.snap_n_returned_rows - coalesce(t1.snap_n_returned_rows, 0))      as "Returned Rows", 
                ((t2.snap_n_tuples_fetched - coalesce(t1.snap_n_tuples_fetched, 0)) + 
                (t2.snap_n_tuples_returned - coalesce(t1.snap_n_tuples_returned, 0))) as "Tuples Read", 
                ((t2.snap_n_tuples_inserted - coalesce(t1.snap_n_tuples_inserted, 0)) + 
                (t2.snap_n_tuples_updated - coalesce(t1.snap_n_tuples_updated, 0)) + 
                (t2.snap_n_tuples_deleted - coalesce(t1.snap_n_tuples_deleted, 0)))   as "Tuples Affected", 
                (t2.snap_n_blocks_fetched - coalesce(t1.snap_n_blocks_fetched, 0))    as "Logical Read", 
                ((t2.snap_n_blocks_fetched - coalesce(t1.snap_n_blocks_fetched, 0)) - 
                (t2.snap_n_blocks_hit - coalesce(t1.snap_n_blocks_hit, 0)))           as "Physical Read", 
                (t2.snap_cpu_time - coalesce(t1.snap_cpu_time, 0)) 		      as "CPU Time(us)", 
                (t2.snap_data_io_time - coalesce(t1.snap_data_io_time, 0)) 	      as "Data IO Time(us)", 
                (t2.snap_sort_count - coalesce(t1.snap_sort_count, 0)) 		      as "Sort Count", 
                (t2.snap_sort_time - coalesce(t1.snap_sort_time, 0)) 		      as "Sort Time(us)", 
                (t2.snap_sort_mem_used - coalesce(t1.snap_sort_mem_used, 0)) 	      as "Sort Mem Used(KB)", 
                (t2.snap_sort_spill_count - coalesce(t1.snap_sort_spill_count, 0))    as "Sort Spill Count", 
                (t2.snap_sort_spill_size - coalesce(t1.snap_sort_spill_size, 0))      as "Sort Spill Size(KB)", 
                (t2.snap_hash_count - coalesce(t1.snap_hash_count, 0)) 		      as "Hash Count", 
                (t2.snap_hash_time - coalesce(t1.snap_hash_time, 0)) 		      as "Hash Time(us)", 
                (t2.snap_hash_mem_used - coalesce(t1.snap_hash_mem_used, 0)) 	      as "Hash Mem Used(KB)", 
                (t2.snap_hash_spill_count - coalesce(t1.snap_hash_spill_count, 0))    as "Hash Spill Count", 
                (t2.snap_hash_spill_size - coalesce(t1.snap_hash_spill_size, 0))      as "Hash Spill Size(KB)", 
                LEFT(t2.snap_query, 25) 					      as "SQL Text" 
        from 
                (select * from snapshot.snap_summary_statement where snapshot_id = {begin} and snap_node_name = '{node_name}') t1
                right join 
                (select * from snapshot.snap_summary_statement where snapshot_id = {end} and snap_node_name = '{node_name}') t2
                on t1.snap_unique_sql_id = t2.snap_unique_sql_id 
                and t1.snap_user_id = t2.snap_user_id 
                order by "Physical Read" 
                desc limit 200;
        """
        # 物理读
        # print(physical_read_sql)
        cursor.execute(physical_read_sql)
        result = cursor.fetchall()
        physical_read = 0
        for i in result:
            # print(i[11])
            # print(type(i[11]))
            if i[11] == 0:
                break
            physical_read += i[11]
        target['Physical_Read'] = physical_read
        # print(target)


        # SQL order by Logical Reads
        logical_read_sql = f"""
        select 	t2.snap_unique_sql_id 												  as "Unique SQL Id", 
                t2.snap_user_name 	  												  as "User Name",
                (t2.snap_total_elapse_time - coalesce(t1.snap_total_elapse_time, 0))  as "Total Elapse Time(us)", 
                (t2.snap_n_calls - coalesce(t1.snap_n_calls, 0))                      as "Calls", 
                round("Total Elapse Time(us)"/greatest("Calls", 1), 0)                as "Avg Elapse Time(us)", 
                t2.snap_min_elapse_time 	    				      as "Min Elapse Time(us)", 
                t2.snap_max_elapse_time 					      as "Max Elapse Time(us)", 
                (t2.snap_n_returned_rows - coalesce(t1.snap_n_returned_rows, 0))      as "Returned Rows", 
                ((t2.snap_n_tuples_fetched - coalesce(t1.snap_n_tuples_fetched, 0)) + 
                (t2.snap_n_tuples_returned - coalesce(t1.snap_n_tuples_returned, 0))) as "Tuples Read", 
                ((t2.snap_n_tuples_inserted - coalesce(t1.snap_n_tuples_inserted, 0)) + 
                (t2.snap_n_tuples_updated - coalesce(t1.snap_n_tuples_updated, 0)) + 
                (t2.snap_n_tuples_deleted - coalesce(t1.snap_n_tuples_deleted, 0)))   as "Tuples Affected", 
                (t2.snap_n_blocks_fetched - coalesce(t1.snap_n_blocks_fetched, 0))    as "Logical Read", 
                ((t2.snap_n_blocks_fetched - coalesce(t1.snap_n_blocks_fetched, 0)) - 
                (t2.snap_n_blocks_hit - coalesce(t1.snap_n_blocks_hit, 0)))           as "Physical Read", 
                (t2.snap_cpu_time - coalesce(t1.snap_cpu_time, 0)) 		      as "CPU Time(us)", 
                (t2.snap_data_io_time - coalesce(t1.snap_data_io_time, 0)) 	      as "Data IO Time(us)", 
                (t2.snap_sort_count - coalesce(t1.snap_sort_count, 0)) 		      as "Sort Count", 
                (t2.snap_sort_time - coalesce(t1.snap_sort_time, 0)) 		      as "Sort Time(us)", 
                (t2.snap_sort_mem_used - coalesce(t1.snap_sort_mem_used, 0)) 	      as "Sort Mem Used(KB)", 
                (t2.snap_sort_spill_count - coalesce(t1.snap_sort_spill_count, 0))    as "Sort Spill Count", 
                (t2.snap_sort_spill_size - coalesce(t1.snap_sort_spill_size, 0))      as "Sort Spill Size(KB)", 
                (t2.snap_hash_count - coalesce(t1.snap_hash_count, 0)) 		      as "Hash Count", 
                (t2.snap_hash_time - coalesce(t1.snap_hash_time, 0)) 		      as "Hash Time(us)", 
                (t2.snap_hash_mem_used - coalesce(t1.snap_hash_mem_used, 0)) 	      as "Hash Mem Used(KB)", 
                (t2.snap_hash_spill_count - coalesce(t1.snap_hash_spill_count, 0))    as "Hash Spill Count", 
                (t2.snap_hash_spill_size - coalesce(t1.snap_hash_spill_size, 0))      as "Hash Spill Size(KB)", 
                LEFT(t2.snap_query, 25) 					      as "SQL Text" 
        from 
                (select * from snapshot.snap_summary_statement where snapshot_id = {begin} and snap_node_name = '{node_name}') t1
                right join 
                (select * from snapshot.snap_summary_statement where snapshot_id = {end} and snap_node_name = '{node_name}') t2
                on t1.snap_unique_sql_id = t2.snap_unique_sql_id 
                and t1.snap_user_id = t2.snap_user_id 
                order by "Logical Read" 
                desc limit 200;
        """
        # 逻辑读
        # print(logical_read_sql)
        cursor.execute(logical_read_sql)
        result = cursor.fetchall()
        logical_read = 0
        for i in result:
            # print(i[10])
            # print(type(i[10]))
            if i[10] == 0:
                break
            logical_read += i[10]
        target['Logical_Read'] = logical_read
        # print(target)



        # User table stats
        user_table_stats_sql = f"""
        SELECT 	snap_2.db_name 		as "DB Name", 
            snap_2.snap_schemaname 	as "Schema",
            snap_2.snap_relname 	as "Relname",
            (snap_2.snap_seq_scan - coalesce(snap_1.snap_seq_scan, 0)) 		     as "Seq Scan",
            (snap_2.snap_seq_tup_read - coalesce(snap_1.snap_seq_tup_read, 0))           as "Seq Tup Read",
            (snap_2.snap_idx_scan - coalesce(snap_1.snap_idx_scan, 0)) 		     as "Index Scan",
            (snap_2.snap_idx_tup_fetch - coalesce(snap_1.snap_idx_tup_fetch, 0))         as "Index Tup Fetch",
            (snap_2.snap_n_tup_ins - coalesce(snap_1.snap_n_tup_ins, 0)) 		     as "Tuple Insert",
            (snap_2.snap_n_tup_upd - coalesce(snap_1.snap_n_tup_upd, 0)) 		     as "Tuple Update",
            (snap_2.snap_n_tup_del - coalesce(snap_1.snap_n_tup_del, 0)) 		     as "Tuple Delete",
            (snap_2.snap_n_tup_hot_upd - coalesce(snap_1.snap_n_tup_hot_upd, 0)) as "Tuple Hot Update",
            snap_2.snap_n_live_tup 				                             as "Live Tuple", 
            snap_2.snap_n_dead_tup 							     as "Dead Tuple",
            to_char(snap_2.snap_last_vacuum, 'YYYY-MM-DD HH24:MI:SS') 		     as "Last Vacuum",
            to_char(snap_2.snap_last_autovacuum, 'YYYY-MM-DD HH24:MI:SS') 		     as "Last Autovacuum",
            to_char(snap_2.snap_last_analyze, 'YYYY-MM-DD HH24:MI:SS') 		     as "Last Analyze",
            to_char(snap_2.snap_last_autoanalyze, 'YYYY-MM-DD HH24:MI:SS') 		     as "Last Autoanalyze",
            (snap_2.snap_vacuum_count - coalesce(snap_1.snap_vacuum_count, 0)) 	     as "Vacuum Count",
            (snap_2.snap_autovacuum_count - coalesce(snap_1.snap_autovacuum_count, 0))   as "Autovacuum Count",
            (snap_2.snap_analyze_count - coalesce(snap_1.snap_analyze_count, 0)) 	     as "Analyze Count",
            (snap_2.snap_autoanalyze_count - coalesce(snap_1.snap_autoanalyze_count, 0)) as "Autoanalyze Count" 
        FROM
            (SELECT * FROM snapshot.snap_global_stat_all_tables 
            WHERE snapshot_id = {end} 
            and snap_node_name = '{node_name}' 
            and snap_schemaname NOT IN ('pg_catalog', 'information_schema', 'snapshot') 
            AND snap_schemaname !~ '^pg_toast') snap_2
        LEFT JOIN 
            (SELECT * FROM snapshot.snap_global_stat_all_tables 
            WHERE snapshot_id = {begin} 
            and snap_node_name = '{node_name}' 
            and snap_schemaname NOT IN ('pg_catalog', 'information_schema', 'snapshot') 
            AND snap_schemaname !~ '^pg_toast') snap_1 
        ON snap_2.snap_relid = snap_1.snap_relid 
        AND snap_2.snap_schemaname = snap_1.snap_schemaname 
        AND snap_2.snap_relname = snap_1.snap_relname 
        AND snap_2.db_name = snap_1.db_name 
        order by snap_2.db_name, snap_2.snap_schemaname 
        limit 200;
        """
        # 更新行，删除行
        # print(user_table_stats_sql)
        cursor.execute(user_table_stats_sql)
        result = cursor.fetchall()
        tuples_update = 0
        tuples_delete = 0
        for i in result:
            # 8更新行，9删除行
            # print(i[8],i[9])
            # print(type(i[8]),type(i[9]))
            tuples_update += i[8]
            tuples_delete += i[9]
        target['Tuples_update'] = tuples_update
        target['Tuples_Delete'] = tuples_delete
        # print(target)





        # User index stats
        user_index_stat_sql = f"""
        SELECT 	snap_2.db_name 			as "DB Name", 
            snap_2.snap_schemaname 		as "Schema",
            snap_2.snap_relname 		as "Relname", 
            snap_2.snap_indexrelname 	as "Index Relname",
            (snap_2.snap_idx_scan - coalesce(snap_1.snap_idx_scan, 0)) 		as "Index Scan",
            (snap_2.snap_idx_tup_read - coalesce(snap_1.snap_idx_tup_read, 0)) 	as "Index Tuple Read",
            (snap_2.snap_idx_tup_fetch - coalesce(snap_1.snap_idx_tup_fetch, 0)) 	as "Index Tuple Fetch" 
        FROM
            (SELECT * FROM snapshot.snap_global_stat_all_indexes 
            WHERE snapshot_id = {end} 
            and snap_node_name = '{node_name}' 
            and snap_schemaname NOT IN ('pg_catalog', 'information_schema', 'snapshot') 
            and snap_schemaname !~ '^pg_toast') snap_2
        LEFT JOIN 
            (SELECT * FROM snapshot.snap_global_stat_all_indexes 
            WHERE snapshot_id = {begin} 
            and snap_node_name = '{node_name}' 
            and snap_schemaname NOT IN ('pg_catalog', 'information_schema', 'snapshot')
            and snap_schemaname !~ '^pg_toast') snap_1 
        ON snap_2.snap_relid = snap_1.snap_relid 
        and snap_2.snap_indexrelid = snap_1.snap_indexrelid 
        and snap_2.snap_schemaname = snap_1.snap_schemaname 
        and snap_2.snap_relname = snap_1.snap_relname 
        and snap_2.snap_indexrelname = snap_1.snap_indexrelname 
        and snap_2.db_name = snap_1.db_name 
        order by "Index Scan" 
        desc limit 200;
        """
        # 索引返回数
        # print(user_index_stat_sql)
        cursor.execute(user_index_stat_sql)
        result = cursor.fetchall()
        index_scan = 0
        for i in result:
            # print(i[4])
            # print(type(i[4]))
            if i[4] == 0:
                break
            index_scan += i[4]
        target['Index_Scan'] = index_scan
        # print(target)




        # IO Profile
        io_sql = f"""
        WITH intervals AS (
            SELECT extract(epoch from snap2.start_ts - snap1.start_ts)::bigint AS interval
            FROM snapshot.snapshot snap2, snapshot.snapshot snap1
            WHERE snap2.snapshot_id = {end} AND snap1.snapshot_id = {begin}
        )
        SELECT
            (snap_2.phytotal - snap_1.phytotal) AS phytotal,
            (snap_2.phyblktotal - snap_1.phyblktotal) AS phyblktotal,
            (snap_2.phyrds - snap_1.phyrds) AS phyrds,
            (snap_2.phyblkrd - snap_1.phyblkrd) AS phyblkrd,
            (snap_2.phywrts - snap_1.phywrts) AS phywrts,
            (snap_2.phyblkwrt - snap_1.phyblkwrt) AS phyblkwrt,
            ROUND((snap_2.phytotal - snap_1.phytotal) / intervals.interval, 0) AS IOPS
        FROM
            (SELECT (snap_phyrds + snap_phywrts) AS phytotal,
                    (snap_phyblkwrt + snap_phyblkrd) AS phyblktotal,
                    snap_phyrds AS phyrds, snap_phyblkrd AS phyblkrd,
                    snap_phywrts AS phywrts, snap_phyblkwrt AS phyblkwrt
            FROM snapshot.snap_global_rel_iostat
            WHERE snapshot_id = {begin} AND snap_node_name = '{node_name}') snap_1,
            (SELECT (snap_phyrds + snap_phywrts) AS phytotal,
                    (snap_phyblkwrt + snap_phyblkrd) AS phyblktotal,
                    snap_phyrds AS phyrds, snap_phyblkrd AS phyblkrd,
                    snap_phywrts AS phywrts, snap_phyblkwrt AS phyblkwrt
            FROM snapshot.snap_global_rel_iostat
            WHERE snapshot_id = {end} AND snap_node_name = '{node_name}') snap_2,
            intervals;
        """
        # IOPS
        cursor.execute(io_sql)
        result = cursor.fetchall()
        iops = result[-1][-1]
        iops = int(iops)
        target['IOPS'] = iops
        # print(target)

        cursor.close()
        conn.close()
        return [float(x) for x in target.values()]