import json
import psycopg2

import config

# 1. 将需要调整的参数名放入knob_list
knob_list = ['max_process_memory',
             'shared_buffers',
             'maintenance_work_mem',
             'wal_buffers',
             'temp_buffers',
             'backend_flush_after',
             'effective_cache_size'
             ]

# 2. 保存参数的文件
knob_config_file = 'knobs-7.json'

# 3. 运行该脚本即可

knob_dict = {}

conn = psycopg2.connect(database=config.db,
                        user=config.user,
                        password=config.password,
                        host=config.host,
                        port=config.port)

cursor = conn.cursor()

for knob in knob_list:
    cursor.execute("select name, min_val, max_val, boot_val, vartype, enumvals, context from pg_settings where name = '{}';".format(knob))
    result = cursor.fetchone()
    tmp = dict()
    tmp['min_val'] = result[1]
    tmp['max_val'] = result[2]
    tmp['boot_val'] = result[3]
    tmp['vartype'] = result[4]
    tmp['enumvals'] = result[5]
    if result[6] == 'postmaster':
        tmp['restart'] = True
    else:
        tmp['restart'] = False
    knob_dict[result[0]] = tmp

js = json.dumps(knob_dict, indent=4)
with open(knob_config_file, 'w') as f:
    f.write(js)


