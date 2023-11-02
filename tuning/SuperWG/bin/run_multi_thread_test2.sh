cd ../DWG/PressureTest
# 执行DWG动态负载生成器
# config_file参数指定的是配置文件名称及路径

sum=0
i=1
while [ $i -le 10 ]
do
    gs_om -t restart
    sudo python3 multi_thread_test_only_run_workloads_without_create_schema.py --workload_path "workloads/res.wg"
    i=$((i + 1))
    sleep 10
done