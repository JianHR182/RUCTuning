# 执行benchbase生成工具
# 生成tatp负载
echo "-- generate tatp quries using benchbase:"
    cd ../benchbase/benchbase-postgres/
    sudo java -jar benchbase.jar -b tatp -c config/postgres/sample_tatp_config.xml --create=true --load=true --execute=true

pg_dump -U postgres -h localhost -p 5432 -Fp lzz > ../../res/tatp_dump_file.sql