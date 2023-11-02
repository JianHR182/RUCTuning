import os
command = "sysbench --db-driver=pgsql --threads=64 --pgsql-host=10.77.10.139 --pgsql-port=15400 --pgsql-user=puzhao --pgsql-password=1234321abc@ --pgsql-db=sysbench --tables=80 --table-size=1000000 --time=600 oltp_read_write run"
os.system(command)