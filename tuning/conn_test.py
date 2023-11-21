import datetime
import json

# from Database import Database
#
# db = Database()
# db.get_conn()
import os
import threading
import time
import matplotlib.pyplot as plt
import numpy as np
import paramiko

import config
import utils
from Database import Database
from stress_testing_tool import stress_testing_tool

db = Database()

# max_tps = 0
# best_knob = None
# with open('history_results/1700116394', 'r') as f:
#     lines = f.readlines()
#     for l in lines:
#         data = json.loads(l)
#         if float(data['tps']) > max_tps:
#             max_tps = float(data['tps'])
#             del data['tps']
#             best_knob = data
#
# print(best_knob)
# print(max_tps)
# db.change_knob(best_knob)
# db.restart()

sst = stress_testing_tool(utils.get_knobs_detail(config.knobs_file), 100000, db)
log_file = 'log/benchmark_log/'.format(100000) + '{}.log'.format(int(time.time()))
qps = []
for i in range(10):
    y = sst.test_by_dwg(log_file)
    qps.append(y)
    print("{}\t{}".format(i + 1, y))
print(qps)

#
# with open('testdwg', 'a') as f:
#     f.write(str(qps) + '\n')

# sys_qps = []
# dwg_qps = []
#
# with open('testdwg') as f:
#     lines = f.readlines()
#     data = lines[3][1:-2].split(',')
#     for d in data:
#         sys_qps.append(float(d))
#     data = lines[4][1:-2].split(',')
#     for d in data:
#         dwg_qps.append(float(d))
#
# sys_mean = np.mean(sys_qps)
# dwg_mean = np.mean(dwg_qps)
#
# sys_std = np.std(sys_qps)
# dwg_std = np.std(dwg_qps)
#
#
#
#
#
# a = [822, 822, 832, 858, 819, 920, 855, 888, 882, 965,
#      970, 823, 861, 922, 920, 818, 930, 939, 922, 911,
#      925, 1011, 901, 966, 918, 985, 962, 997, 990, 996,
#      993, 988, 958, 986, 1046, 963, 1001, 1016, 1039, 977,
#      1002, 1040, 1070, 1067, 1080, 1010, 1041, 1018, 1065, 1095]
#
# a_mean = np.mean(a)
# a_std = np.std(a)
#
# print(sys_mean)
# print(sys_std)
# print(dwg_mean)
# print(dwg_std)
#
# print(a_mean)
# print(a_std)
#
# plt.plot(np.arange(len(sys_qps)), sys_qps)
# plt.plot(np.arange(len(dwg_qps)), dwg_qps / dwg_mean * sys_mean)
# plt.plot(np.arange(len(a)), a / a_mean * sys_mean)
# plt.show()

# qps = []
# with open('history_results/1700116394', 'r') as f:
#     lines = f.readlines()
#     for l in lines:
#         data = json.loads(l)
#         qps.append(float(data['tps']))
# plt.plot(np.arange(len(qps)), qps)
# plt.show()
