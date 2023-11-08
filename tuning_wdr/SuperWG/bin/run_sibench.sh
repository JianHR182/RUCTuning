# 执行benchbase生成工具
# 生成sibench负载
echo "-- generate sibench quries using benchbase:"
    cd ../benchbase/benchbase-postgres/
    sudo java -jar benchbase.jar -b sibench -c config/postgres/sample_sibench_config.xml --create=true --load=true --execute=true

pg_dump -U postgres -h localhost -p 5432 -s lzz --inserts > ../../res/sibench_create.sql
pg_dump -U postgres -h localhost -p 5432 -a lzz --inserts > ../../res/sibench_insert.sql