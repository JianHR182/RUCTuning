# 调优配置
# 随机采样次数
sampling_number = 1
# 模型推荐次数
iteration = 1
# 调优方式, 在线True, 离线False
online = False
# 是否进行微调, iteration为微调次数
finetune = False
# 在线调优是否允许重启
restart_when_online = False
# 是否需要分析静态特征，使用dwg离线调优时使用
static = True
# 是否提供负载样本，在线调优时使用，如果启用，需要在dwg配置中给出schema_name以及将负载放入（直接覆盖）workload参数所给路径文件中
isworkload = False
# 数据库待调整的配置参数文件
knobs_file = 'knobs_config/knobs-7.json'
# 进行重要性排名后, 选取的配置参数的数量
ranked_knobs_number = 7
method = 'HEBO'
log_path = 'log'
final_results = 'final_results'
knowledge = 'knowledge.json'


# 数据库配置
host = '10.77.10.139'
port = 15400
db = 'sysbench50_1m'
user = 'tianjikun'
password = 'tianjikun1234@'
omm_password = '1234321abc@'
opengauss_node_path = '/home/omm/data'
root_password = '1234321'
# 重启数据库的等待时间, 若超时仍未启动, 则恢复数据库
time_wait = 30


# 所使用的压测工具 sysbench 或 dwg
benchmark = 'dwg'
# 压测线程数
threads = 10


# sysbench配置
tables = 20
table_size = 8000000
mode = 'oltp_read_write'
runing_time = 5
# 正式压测之前预热时间, 结果不计算在最终tps中
warm_up_time = 10


# dwg配置
# 需要解析的schema名称
schema_name = 'public'
# 执行gs_dump命令后在服务端保存的结果(建表语句等, 用于生成负载)
remote_cache_path = '/home/omm/test.sql'
# 执行gs_dump命令后在本地保存的结果
local_cache_path = 'workloads/schema/test.sql'
# 默认不分析本地文件
use_local = 'false'
# 生成负载的规模
sql_num = 100000
# 生成负载的读写比 read / total
read_write_ratio = 0.6
# 生成负载的其他配置信息
json_extract_result_path = 'workloads/schema/res.json'
# 生成负载的保存路径, 也是使用dwg压测所用的负载
workload = 'workloads/res.wg'
# workload = 'workloads/sysbench20_8m.txt'
# 每个线程成功执行sql_num_print条sql后在控制台输出信息
sql_num_print = 100


# hardware configs
memory = 64

# monadmin
mon_db = 'postgres'
mon_user = 'jhr'
mon_password = 'jhr123456@'
