# 执行benchbase生成工具
# 生成tpcc负载
echo "-- generate tpcc quries using benchbase:"
    cd ../benchbase/benchbase-postgres/
    sudo java -jar benchbase.jar -b tpcc -c config/postgres/sample_tpcc_config.xml --create=true --load=true --execute=true

pg_dump -U postgres -h localhost -p 5432 -Fp lzz > ../../res/tpcc_dump_file.sql