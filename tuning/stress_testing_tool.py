import argparse
import os
import sys
import threading
import time
import json
from datetime import datetime

import paramiko

import config
import utils
from SuperWG.DWG.PressureTest.multi_thread_test_only_run_workloads_without_create_schema import \
    multi_thread_without_create_schema


class stress_testing_tool:
    def __init__(self, knobs_detail, id, db):
        self.port = config.port
        self.host = config.host
        self.user = config.user
        self.password = config.password
        self.dbname = config.db
        self.tables = config.tables
        self.table_size = config.table_size
        self.runing_time = config.runing_time
        self.omm_password = config.omm_password
        self.threads = config.threads
        self.logger = utils.get_logger('log/benchmark_log/{}.log'.format(id))
        self.benchmark = config.benchmark
        self.knobs_detail = knobs_detail
        self.id = id
        self.warm_up_time = config.warm_up_time
        self.db = db

    def handle_HORD_config(self, config):
        temp_config = {}

        for index, key in enumerate(self.knobs_detail.keys()):
            temp_config[key] = int(config[index])

        y = self.test_config(temp_config)
        return y

    def handle_HEBO_config(self, config):
        temp_config = {}
        config = config.reset_index(drop=True)

        for key in self.knobs_detail.keys():
            temp_config[key] = int(config.loc[0, key])

        y = self.test_config(temp_config)
        return y

    def handle_SMAC_config(self, config, seed=0):
        temp_config = {}
        for key in self.knobs_detail.keys():
            temp_config[key] = config[key]

        y = self.test_config(temp_config)
        return y

    def test_config(self, config):
        temp_config = {}
        for key in config.keys():
            if self.knobs_detail[key]['vartype'] == 'integer':
                if float(self.knobs_detail[key]['max_val']) > sys.maxsize:
                    temp_config[key] = config[key] * 1000000
                else:
                    temp_config[key] = config[key]
            elif self.knobs_detail[key]['vartype'] == 'enum':
                temp_config[key] = self.knobs_detail[key]['enumvals'][config[key]]

        self.db.change_knob(temp_config)

        log_file = 'log/benchmark_log/'.format(self.id) + '{}.log'.format(int(time.time()))

        if self.benchmark == 'sysbench':
            y = self.test_by_sysbench(log_file)
        elif self.benchmark == 'tpcc':
            y = self.test_by_tpcc(log_file)
        else:
            y = self.test_by_dwg(log_file)

        f = open('./history_results/{}'.format(self.id), 'a')
        temp_config['tps'] = y
        f.writelines(json.dumps(temp_config) + '\n')
        f.close()

        return y

    def test_by_sysbench(self, log_file):
        command_warm = 'sysbench --db-driver=pgsql --threads={} --pgsql-host={} --pgsql-port={} --pgsql-user={} --pgsql-password={} --pgsql-db={} --tables={} --table-size={} --time={} {} run'.format(
            self.threads,
            self.host,
            self.port,
            self.user,
            self.password,
            self.dbname,
            self.tables,
            self.table_size,
            self.warm_up_time,
            config.mode
        )

        command_run = 'sysbench --db-driver=pgsql --threads={} --pgsql-host={} --pgsql-port={} --pgsql-user={} --pgsql-password={} --pgsql-db={} --tables={} --table-size={} --time={} {} run'.format(
            self.threads,
            self.host,
            self.port,
            self.user,
            self.password,
            self.dbname,
            self.tables,
            self.table_size,
            self.runing_time,
            config.mode
        )

        ssh = self.db.get_ssh()
        print('run sysbench...')
        stdin, stdout, stderr = ssh.exec_command(command_warm)
        stdin, stdout, stderr = ssh.exec_command(command_run)
        res = stdout.read().decode('utf-8')
        print('run sysbench over...')

        lines = res.split('\n')
        for line in lines:
            if 'queries:' in line:
                tps = float(line.split()[2].split('(')[1])
                return tps
        self.logger.info('sysbench run error: \n')
        self.logger.info(res)
        return -1

    def test_by_tpcc(self, log_file):
        command = '/usr/local/benchmarksql-5.0/run/runBenchmark.sh props.pg > {}'.format(log_file)
        state = os.system(command)

        if state == 0:
            self.logger.info('tpcc running success')
        else:
            self.logger.info('tpcc running error')

        with open(log_file) as f:
            lines = f.readlines()
        for line in lines:
            if 'Measured tpmTOTAL' in line:
                tps = float(line.split()[9])

        return -tps

    def test_by_dwg(self, log_file):
        print("run dwg...")
        parser = argparse.ArgumentParser()
        parser.add_argument('--database_name', type=str, default=config.db)
        parser.add_argument('--user_name', type=str, default=config.user)
        parser.add_argument('--password', type=str, default=config.password)
        parser.add_argument('--host', type=str, default=config.host)
        parser.add_argument('--port', type=int, default=config.port)
        parser.add_argument('--n_jobs', type=int, default=config.threads)
        parser.add_argument('--workload_path', default=config.workload)
        parser.add_argument('--id', default=self.id)
        args = parser.parse_args()

        mh = multi_thread_without_create_schema(args)
        mh.data_pre()

        tps = mh.run()
        print("dwg over...")
        return tps
