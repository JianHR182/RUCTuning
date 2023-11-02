# 随机采样次数
sampling_number = 100
# 模型推荐次数
iteration = 100
# 调优方式, 在线True, 离线False
online = False
# 是否进行微调, iteration为微调次数
finetune = False

# 数据库配置
host = '10.77.10.139'
port = 15400
db = 'sysbench'
user = 'lzz'
password = 'zongze123@'
omm_password = '1234321abc@'
opengauss_node_path = '/home/omm/data'

# 所使用的压测工具 sysbench 或 dwg
benchmark = 'sysbench'

# sysbench配置
tables = 50
table_size = 1000000
threads = 32
mode = 'oltp_read_write'
runing_time = 5
# 正式压测之前预热时间, 结果不计算在最终tps中
warm_up_time = 10

# 重启数据库的等待时间, 若超时仍未启动, 则恢复数据库
time_wait = 30

# 数据库待调整的配置参数文件
knobs_file = './knobs_config/knobs-13.json'
knobs_number = 13
# 进行重要性排名后, 选取的配置参数的数量
ranked_knobs_number = 10

method = 'HEBO'
log_path = 'log'
final_results = 'final_results'
knowledge = 'knowledge.json'
# hardware configs
memory = 64
