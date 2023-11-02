# 执行benchbase生成工具
# 生成seats负载
echo "-- generate seats quries using benchbase:"
    cd ../benchbase/benchbase-postgres/
    sudo java -jar benchbase.jar -b seats -c config/postgres/sample_seats_config.xml --create=true --load=true --execute=true

pg_dump -U postgres -h localhost -p 5432 -Fp lzz > ../../res/seats_dump_file.sql