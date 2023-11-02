import json
import psycopg2

import config

# 1. 将需要调整的参数名放入knob_list
knob_list = ['shared_buffers',
             'autovacuum_vacuum_scale_factor',
             'wal_level',
             'autovacuum',
             'dcf_log_level',
             ]

# 2. 保存参数的文件
knob_config_file = 'knobs_config.json'

# 3. 运行该脚本即可

knob_dict = {}

conn = psycopg2.connect(database=config.db,
                        user=config.user,
                        password=config.password,
                        host=config.host,
                        port=config.port)

cursor = conn.cursor()

for knob in knob_list:
    cursor.execute("select name, min_val, max_val, boot_val, vartype, enumvals from pg_settings where name = '{}';".format(knob))
    result = cursor.fetchone()
    tmp = dict()
    tmp['min_val'] = result[1]
    tmp['max_val'] = result[2]
    tmp['boot_val'] = result[3]
    tmp['vartype'] = result[4]
    tmp['enumvals'] = result[5]
    knob_dict[result[0]] = tmp

js = json.dumps(knob_dict, indent=4)
with open(knob_config_file, 'w') as f:
    f.write(js)


