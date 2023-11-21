# 执行benchbase生成工具
# 生成tpch负载
echo "-- generate tpch quries using benchbase:"
    cd ../benchbase/benchbase-postgres/
    sudo java -jar benchbase.jar -b tpch -c config/postgres/sample_tpch_config.xml --create=true --load=true --execute=true

pg_dump -U postgres -h localhost -p 5432 -Fp lzz > ../../res/tpch_dump_file.sql