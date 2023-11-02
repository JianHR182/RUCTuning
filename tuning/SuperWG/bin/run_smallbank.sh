# 执行benchbase生成工具
# 生成small bank负载
echo "-- generate smallbank quries using benchbase:"
    cd ../benchbase/benchbase-postgres/
    sudo java -jar benchbase.jar -b smallbank -c config/postgres/sample_smallbank_config.xml --create=true --load=true --execute=true

pg_dump -U postgres -h localhost -p 5432 -Fp lzz > ../../res/smallbank_dump_file.sql