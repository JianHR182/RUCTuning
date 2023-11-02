cd ../DWG/WP
# 执行辅助配置工具
# config_file参数指定的是配置文件名称及路径
# workload_file参数指定的是历史负载文件名称及路径
# python WorkloadParser.py --config_file workloads/dwg.json --workload_file workloads/dwg_workload.txt
python WorkloadParser.py --config_file workloads/tpch.json --workload_file workloads/tpch_workload.txt
