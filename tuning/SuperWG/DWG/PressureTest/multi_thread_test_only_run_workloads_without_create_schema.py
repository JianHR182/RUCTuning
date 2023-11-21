from collections.abc import Callable, Iterable, Mapping
from typing import Any

import config
from SuperWG.DWG.PressureTest.single_thread_test import *
import argparse


class one_thread_given_queries(threading.Thread):
    def __init__(self, wg, log_path, thread_id, time_stamp) -> None:
        threading.Thread.__init__(self)
        self.wg = wg
        self.log_path = log_path
        self.connection, self.cur = connect_og(config.db, config.user, config.password, config.host, config.port)
        self.thread_id = thread_id
        self.time_stamp = time_stamp
        # print("thread {} connect og...{}".format(thread_id, self.connection))

    def run(self):

        self.cur.execute(f"SET search_path TO {config.schema_name};")
        self.connection.commit()

        sql_list = self.wg
        with open(self.log_path, 'a') as f:
            # 暂时注释
            # print(f"Thread {self.thread_id} log file start. Tot sql num : {len(sql_list)}")
            # f.write(f"Thread {self.thread_id} log file start. Tot sql num : {len(sql_list)}\n")
            start_time = time.time()
            for i, it in enumerate(sql_list):
                try:
                    # print("current sql : ", it)
                    self.cur.execute(it)
                    self.connection.commit()
                except Exception as e:
                    # print("Error: ", e)
                    # print("Error sql : ", it)
                    # f.write("Error: {}".format(e))
                    # f.write("Error sql : {}".format(it))
                    pass

                if self.thread_id == 0 and (i + 1) % config.sql_num_print == 0:
                    print(f"{i + 1} sqls have been processed per thread")

            end_time = time.time()
            self.time_stamp[self.thread_id] = key(len(sql_list), end_time - start_time)
            self.connection.close()


class multi_thread_without_create_schema:
    def __init__(self, config):

        self.config = config
        self.id = config.id
        self.log_path = 'log/benchmark_log/{}.log'.format(self.id)
        self.sql_list_idx = dict()

    def data_pre(self):

        with open(self.config.workload_path, 'r') as f:
            self.wg_file = f.read()

        sql_list = re.split(r'[;\n]+', self.wg_file)

        # sql_list = sql_list[:20000]

        for i, it in enumerate(sql_list):
            sql_list[i] += ";"

        if sql_list[-1] == ";":
            sql_list = sql_list[0:-2]

        self.sql_list_idx = dict()

        for i in range(self.config.n_jobs):
            self.sql_list_idx[i] = []

        for i in range(len(sql_list)):
            self.sql_list_idx[i % self.config.n_jobs].append(sql_list[i])

    def run(self):
        threads = []
        time_stamp = dict()

        for i in range(self.config.n_jobs):
            thread = one_thread_given_queries(
                wg=self.sql_list_idx[i],
                log_path=self.log_path,
                thread_id=i,
                time_stamp=time_stamp
            )
            threads.append(thread)

        print("Threads boxed up.")
        start_time = time.time()
        for it in threads:
            it.start()
        for it in threads:
            it.join()
        end_time = time.time()

        with open(self.log_path, 'a') as f:
            sql_num = len(self.wg_file.split(";"))
            f.write(f"total sql num : {sql_num}\n")
            f.write(f"total time consumed : {end_time - start_time}\n")

            tps = sql_num / (end_time - start_time)

            for i in range(self.config.n_jobs):
                f.write(f"\tthread {i} processed sql num : {time_stamp[i].value}\n")
                f.write(f"\tthread {i} using time : {time_stamp[i].type}\n")

        return tps

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--database_name', type=str, default='sysbench')
#     parser.add_argument('--user_name', type=str, default='lzz')
#     parser.add_argument('--password', type=str, default='zongze123@')
#     parser.add_argument('--host', type=str, default='10.77.10.139')
#     parser.add_argument('--port', type=int, default=15400)
#     parser.add_argument('--n_jobs', type=int, default=10)
#     parser.add_argument('--workload_path', default='workloads/res.wg')
#     args = parser.parse_args()
#
#     mh = multi_thread_without_create_schema(args)
#     mh.data_pre()
#     mh.run()
#     print("All threads have finished")
