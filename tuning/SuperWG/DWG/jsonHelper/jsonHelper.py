#!/usr/bin/env python
# vim: set fileencoding=utf-8
import paramiko
import re
import json
import argparse
# import sys
# import os
# current_file_path = os.path.split(os.path.abspath(__file__))[0]
# config_path = current_file_path.rsplit('/',3)[0]
# sys.path.append(config_path)
import config


# 初始化ssh客户端
def init(config):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=config.hostname, username="omm", password=config.omm_password)

    stdin, stdout, stderr = ssh_client.exec_command('whoami')
    output = stdout.read().decode()

    pattern = r"[a-zA-Z]+\n?"
    output_alter = re.sub(pattern, lambda m: m.group().strip(), output)

    if output_alter != "omm":
        print("fatal error : not login correctly.")
    return ssh_client


# 语法解析函数
def parseSQL2json2(create_table_sql):
    one_table = {
        "Table Name": "",
        "Table Columns": [],
        "Column Distribution": [],
        "Primary Key": {
            "Name": "",
            "Data Type": ""
        },
        "Foreign Key": [
            {
                "Foreign Key Name": "",
                "Foreign Key Type": "",
                "Referenced Table": "",
                "Referenced Primary Key": "",
                "Referenced Primary Key Type": ""
            }
        ]
    }
    filter_pattern = r"(CREATE TABLE .*)WITH"
    create_table_sql_prum = re.search(pattern=filter_pattern, string=create_table_sql, flags=re.DOTALL).group(1)

    import psqlparse
    try:
        statements = psqlparse.parse(create_table_sql_prum)
        table_name_match = statements[0]['CreateStmt']['relation']['RangeVar']['relname']
    except Exception as e:
        print("fatal error : sql syntax incorrect.")
        print("wrong sql : {create_table_sql_prum}")
        return

    index_ = 1
    columns = []
    for i in statements[0]['CreateStmt']['tableElts']:
        # 各个列
        for j, k in i.items():
            # print(j,":")
            # print(f"{index_} : ")
            one_column = {
                "Column Name": 'column_name',
                "Data Type": 'column_type',
                "Data Type Mod": 0,
                "Data Distribution": ["minv", "maxv"]
            }
            for m, n in k.items():
                if m == "typeName":
                    one_column["Data Type"] = n['TypeName']['names'][len(n['TypeName']['names']) - 1]['String']['str']
                    one_column["Data Type"] = one_column["Data Type"].lower()
                    if one_column["Data Type"][0:3] == "int":
                        one_column["Data Type"] = 'int'
                    elif one_column["Data Type"][0:5] == "float":
                        one_column["Data Type"] = 'float'
                    # elif one_column["Data Type"]=="bpchar":
                    #     one_column["Data Type"]='varchar'

                    # 处理typemod
                    # print("\tcoltype : ",n['TypeName']['names'][len(n['TypeName']['names'])-1]['String']['str'])
                    if n['TypeName']['names'][len(n['TypeName']['names']) - 1]['String']['str'] in ["varchar", "text"]:
                        if "typmods" not in n['TypeName'].keys():
                            one_column["Data Type Mod"] = 255
                        else:
                            one_column["Data Type Mod"] = n['TypeName']['typmods'][0]['A_Const']['val']['Integer'][
                                'ival']

                    # 处理定长数组bpchar类型
                    elif n['TypeName']['names'][len(n['TypeName']['names']) - 1]['String']['str'] == "bpchar":
                        one_column["Data Type Mod"] = n['TypeName']['typmods'][0]['A_Const']['val']['Integer']['ival']

                    # timestamp有两种情形，有精度和无精度
                    # 无精度就默认精度最低，也就是0
                    elif n['TypeName']['names'][len(n['TypeName']['names']) - 1]['String']['str'] == 'timestamp':
                        if 'typmods' in n['TypeName'].keys():
                            one_column["Data Type Mod"] = n['TypeName']['typmods'][0]['A_Const']['val']['Integer'][
                                'ival']
                        else:
                            one_column["Data Type Mod"] = 0
                    # numeric也有两种情形，一维和二维
                    # numeric数据类型需要两个参数，这两个参数分别用于指定数值的总位数和小数位数
                    # 比如，numeric(5,2)代表333.33这种数字
                    elif n['TypeName']['names'][len(n['TypeName']['names']) - 1]['String']['str'] == 'numeric':
                        if 'typmods' in n['TypeName'].keys():
                            one_column['Data Type Mod'] = \
                                [n['TypeName']['typmods'][0]['A_Const']['val']['Integer']['ival'],
                                 n['TypeName']['typmods'][1]['A_Const']['val']['Integer']['ival']]
                        else:
                            one_column['Data Type Mod'] = [10, 0]

                    # 设置缺省值域
                    if one_column["Data Type"] in ["varchar"]:
                        one_column["Data Distribution"] = [1, max(one_column["Data Type Mod"] - 2, 1)]
                    elif one_column["Data Type"] in ["bpchar"]:
                        one_column["Data Distribution"] = [one_column["Data Type Mod"], one_column["Data Type Mod"]]
                    elif one_column["Data Type"] in ["int", "float", "tinyint", "double", "bigint"]:
                        one_column["Data Distribution"] = [0, 100]
                    elif one_column["Data Type"] in ["numeric"]:
                        # one_column["Data Distribution"]=[1,100]
                        one_column["Data Distribution"] = \
                            [
                                0,
                                10 ** (one_column['Data Type Mod'][0] - one_column['Data Type Mod'][1]) - 1
                            ]
                    elif one_column["Data Type"] in ["timestamp"]:
                        one_column["Data Distribution"] = ["1900-11-02 0:0:0", "2023-9-1 0:0:0"]
                    else:
                        one_column["Data Distribution"] = ["unknown", "unknown"]

                elif m == "colname":
                    index_ += 1
                    # print("\tcolname : ",n)
                    one_column["Column Name"] = n
                else:
                    pass
            columns.append(one_column)

    # 过去的匹配法，支持较少的数据类型，现已优化掉
    # column_matches = re.findall(column_pattern, create_table_sql_prum)

    # for column_match in column_matches:
    #     column_name = column_match[0]
    #     column_type = column_match[1]
    #     if column_name.upper()=="CREATE":
    #         pass
    #     else:
    #         # columns.append((column_name, column_type))
    #         if column_type=="varchar":
    # one_column={
    #     "Column Name": column_name,
    #     "Data Type": column_type,
    #     "Data Distribution": ["minv","maxv"]
    # }
    #         else:  
    #             one_column={
    #                 "Column Name": column_name,
    #                 "Data Type": column_type,
    #                 "Data Distribution": [0,100]
    #             }
    #         columns.append(one_column)

    one_table["Table Name"] = table_name_match
    one_table["Table Columns"] = columns

    one_table["Column Distribution"] = [1.0 / len(columns) for i in range(len(columns))]
    for i in range(len(columns)):
        one_table["Column Distribution"][i] = 0
    one_table["Column Distribution"][0] = 1.0
    return one_table


if __name__ == "__main__":
    print("Extraction start.")

    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname', type=str, default=config.host)
    parser.add_argument('--username', type=str, default=config.user)
    parser.add_argument('--omm_password', type=str, default=config.omm_password)
    parser.add_argument('--user_password', type=str, default=config.password)
    parser.add_argument('--sql_path', type=str, default=config.remote_cache_path)
    parser.add_argument('--port', type=int, default=config.port)
    parser.add_argument('--database_name', type=str, default=config.db)
    parser.add_argument('--schema_name', type=str, default=config.schema_name)
    parser.add_argument('--use_local', type=str, default=config.use_local)
    parser.add_argument('--cache_path', type=str, default='../../../' + config.local_cache_path)
    parser.add_argument('--result_path', type=str, default='../../../' + config.json_extract_result_path)

    args = parser.parse_args()

    if args.use_local == 'false':
        ssh_client = init(args)

        command = "gs_dump -U {} -f {} -p {} -s {} -n {} -F p ".format(args.username, args.sql_path, args.port,
                                                                       args.database_name, args.schema_name)
        # command = "gs_dump -U jikun -f /home/tianjikun/schema/test.sql -p 15400 dwg -n public -F p"
        print("command : ", command)
        stdin, stdout, stderr = ssh_client.exec_command(command=command)
        stdin.write(args.user_password + '\n')
        stdin.flush()
        output = stdout.read().decode()
        print(output)

        sftp_client = ssh_client.open_sftp()
        sftp_client.get(localpath=args.cache_path, remotepath=args.sql_path)
        sftp_client.close()

        with open(args.cache_path, 'r') as f:
            content = f.read()
        print(type(content), len(content))

    else:
        print("Warning : using local file {args.sql_path}.")

        with open(args.sql_path, 'r') as f:
            content = f.read()
        print(type(content), len(content))

    content_split = re.split('[\n]*;+[\n]*', content)
    print(len(content_split))
    # content_split = re.sub('\n', '', content_split)
    real_content = []
    for it in content_split:
        # if "CREATE" in it and "GRANT" not in it and "INDEX" not in it:
        # print(it)
        # real_content.append(it)
        filter_pattern = r"(CREATE TABLE .*)WITH"
        if re.search(pattern=filter_pattern, string=it, flags=re.DOTALL) is not None:
            # print(it)
            real_content.append(it)

    json_data = {
        "Table Schema": args.schema_name,
        "Tables": [],
        "Constraints": {
            "size of workload": config.sql_num,
            "read write ratio": config.read_write_ratio,
            "average table num": [0.9, 0.1],
            "table-query access distribution": [],
            "query comparison operator ratio": [0.1, 0.1, 0.8, 0],
            "table domain distribution": [0.5, 0.5],
            "query logic predicate num": [0.6, 0.2, 0.2],
            "average aggregation operator num": [0.5, 0.3, 0.2],
            "average query colomn num": [0, 0.6, 0.3, 0.1],
            "group by ratio if read SQL": [0.5, 0.5],
            "order by desc or asc if grouped": [0.5, 0.5]
        },
        "Generation File": config.workload
    }

    tables = []
    for it in real_content:
        one_table = parseSQL2json2(it)
        tables.append(one_table)
    json_data["Tables"] = tables
    import numpy as np

    json_data["Constraints"]["table-query access distribution"] \
        = np.full(len(json_data["Tables"]), 1.0 / len(json_data["Tables"])).tolist()

    with open(args.result_path, "w") as f:
        json.dump(json_data, f, indent=4)
        print("parse succeeded.")
        print("result written in res.json.")

    if args.use_local == "false":
        ssh_client.close()
    else:
        pass
