#!/usr/bin/env python
# vim: set fileencoding=utf-8
from collections.abc import Callable, Iterable, Mapping
from typing import Any
from single_thread_test import *
import argparse


class one_thread_given_queries(threading.Thread):
    def __init__(self, wg, log_path, connection, cur, thread_id, time_stamp) -> None:
        threading.Thread.__init__(self)
        self.wg = wg
        self.log_path = log_path
        self.connection = connection
        self.cur = cur
        self.thread_id = thread_id
        self.time_stamp = time_stamp

    def run(self):
        try:
            sql_list = self.wg
            with open(self.log_path, 'w') as f:
                print(f"Thread {self.thread_id} log file start. Tot sql num : {len(sql_list)}")
                f.write(f"Thread {self.thread_id} log file start. Tot sql num : {len(sql_list)}\n")
                start_time = time.time()
                for i, it in enumerate(sql_list):
                    error_info = it
                    self.cur.execute(it)
                    self.connection.commit()
                    # print(f"Thread {self.thread_id} sql id {i}")
                    if i % 20 == 0:
                        f.write(f"Thread {self.thread_id} {i} sqls has been processed successfully.\n")
                        print(f"Thread {self.thread_id} {i} sqls has been processed successfully.")
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        f.write(f"Thread {self.thread_id} processed time: {elapsed_time} seconds.\n")
                        print(f"Thread {self.thread_id} processed time: {elapsed_time} seconds.")

                end_time = time.time()
                self.time_stamp[self.thread_id] = key(len(sql_list), end_time - start_time)

        except Exception as e:
            print("Error: ", e)
            print(error_info)


class multi_thread:
    def __init__(self, config, workload_name, thread_num):

        self.config = config
        self.id = generate_random_string(10)
        self.workload_name = workload_name
        self.thread_num = thread_num
        self.schema_path = "workloads/" + workload_name + "_create" + ".sql"
        self.data_path = "workloads/" + workload_name + "_insert" + ".sql"
        self.wg_path = "workloads/" + workload_name + "_workload" + ".wg"
        self.log_path = "workloads/" + self.id + ".log"
        self.sql_list_idx = dict()

    def data_pre(self):
        connection, cur = connect_og(
            # database_name="l_test",
            # user_name="lzz",
            # password="zongze123@",
            # host="182.92.85.148",
            # port=15400
            database_name=self.config.database_name,
            user_name=self.config.user_name,
            password=self.config.password,
            host=self.config.host,
            port=self.config.port
        )
        print(connection.info)
        create_schema(connection, cur, self.schema_path)
        insert_data(connection, cur, self.data_path)
        connection.close()

        with open(self.config.workload_path, 'r') as f:
            self.wg_file = f.read()

        sql_list = re.split(r'[;\n]+', self.wg_file)
        for i, it in enumerate(sql_list):
            sql_list[i] += ";"

        if sql_list[-1] == ";":
            sql_list = sql_list[0:-2]

        self.sql_list_idx = dict()

        for i in range(self.thread_num):
            self.sql_list_idx[i] = []

        for i in range(len(sql_list)):
            self.sql_list_idx[i % self.thread_num].append(sql_list[i])

    def run(self):
        connection, cur = connect_og(
            # database_name="l_test",
            # user_name="lzz",
            # password="zongze123@",
            # host="182.92.85.148",
            # port=15400
            database_name=self.config.database_name,
            user_name=self.config.user_name,
            password=self.config.password,
            host=self.config.host,
            port=self.config.port
        )
        # connection, cur = connect_og(
        #     database_name="dwg",
        #     user_name="jikun",
        #     password="tianjikun123@",
        #     host="182.92.85.148",
        #     port=15400
        # )
        print(connection.info)
        threads = []
        time_stamp = dict()

        for i in range(self.thread_num):
            thread = one_thread_given_queries(
                wg=self.sql_list_idx[i],
                log_path="workloads/" + str(i) + "_" + generate_random_string() + ".log",
                connection=connection,
                cur=cur,
                thread_id=i,
                time_stamp=time_stamp
            )
            threads.append(thread)

        start_time = time.time()
        for it in threads:
            it.start()
        for it in threads:
            it.join()
        end_time = time.time()

        with open(self.log_path, 'w') as f:
            sql_num = len(self.wg_file.split(";"))
            f.write(f"total sql num : {sql_num}\n")
            f.write(f"total time consumed : {end_time - start_time}\n")
            for i in range(self.thread_num):
                f.write(f"\tthread {i} processed sql num : {time_stamp[i].value}\n")
                f.write(f"\tthread {i} using time : {time_stamp[i].type}\n")
        connection.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--database_name', type=str, default='l_test')
    parser.add_argument('--user_name', type=str, default='lzz')
    parser.add_argument('--password', type=str, default='zongze123@')
    parser.add_argument('--host', type=str, default='10.77.10.139')
    parser.add_argument('--port', type=int, default=15400)
    parser.add_argument('--n_jobs', type=int, default=3)
    parser.add_argument('--bench_name', type=str, default="sibench")
    parser.add_argument('--workload_path', default="workloads/res.wg")
    args = parser.parse_args()

    mh = multi_thread(args, "dwg", 3)
    mh.data_pre()
    mh.run()
    print("All threads have finished")
