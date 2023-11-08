import json
import numpy as np
import config
from SuperWG.DWG.WP.WorkloadParser import WP2
import argparse
import re
from SuperWG.DWG.jsonHelper.jsonHelper import parseSQL2json2


def get_train_featrue(db, begin, end):
    inner = db.fetch_inner_metric()
    wdr_metrics = db.get_wdr_metric(begin, end)

    if  config.static and config.benchmark == 'dwg':
        parser = argparse.ArgumentParser()
        parser.add_argument('--hostname', type=str, default='10.77.10.139')
        parser.add_argument('--username', type=str, default='lzz')
        parser.add_argument('--omm_password', type=str, default='1234321abc@')
        parser.add_argument('--user_password', type=str, default='zongze123@')
        parser.add_argument('--sql_path', type=str, default='downloadsql.sql')
        parser.add_argument('--port', type=int, default=15400)
        parser.add_argument('--database_name', type=str, default='sysbench')
        parser.add_argument('--schema_name', type=str, default='public')
        parser.add_argument('--use_local', type=str, default='false')
        parser.add_argument('--cache_path', type=str, default='SuperWG/DWG/jsonHelper/data/test.sql')
        parser.add_argument('--config_file', type=str, default='SuperWG/DWG/jsonHelper/data/res.json')
        parser.add_argument('--workload_path', default='SuperWG/DWG/PressureTest/workloads/res.wg')

        args = parser.parse_args()

        if args.use_local=='false':
            command=f"gs_dump -U {args.username} -f {args.sql_path} -p {args.port} -s {args.database_name} -n {args.schema_name} -F p"
            stdin, stdout, stderr = db.ssh.exec_command(command=command)
            stdin.write(f'{args.user_password}\n')
            stdin.flush()
            output = stdout.read().decode()
            print(output)

            sftp_client = db.ssh.open_sftp()
            sftp_client.get(localpath=args.cache_path, remotepath=args.sql_path)
            sftp_client.close()

            with open(args.cache_path, 'r') as f:
                content=f.read()
            # print(type(content),len(content))
        else:
            with open(args.sql_path, 'r') as f:
                content=f.read()
            # print(type(content),len(content))  

        content_split=re.split('[\n]*;+[\n]*',content)
        print(len(content_split))
        real_content=[]
        for it in content_split:
            filter_pattern = r"(CREATE TABLE .*)WITH"
            if re.search(pattern=filter_pattern,string=it,flags=re.DOTALL)!=None:
                real_content.append(it)

        json_data={
            "Table Schema": "noobschema",
            "Tables": [],
            "Constraints": {
            "size of workload" : 1000,
            "read write ratio": 0.9,
            "average table num": [0.5,0.5],
            "table-query access distribution": [],
            "query comparison operator ratio" : [0.25,0.25,0.25,0.25],
            "table domain distribution" : [0.5,0.5],
            "query logic predicate num" : [0.4,0.4,0.2],
            "average aggregation operator num" : [0.5,0.3,0.2],
            "average query colomn num":[0,0.4,0.3,0.3],
            "group by ratio if read SQL":[0.8,0.2],
            "order by desc or asc if grouped":[0.85,0.15]
            },
            "Generation File":"../res/res.wg"
        }

        tables=[]
        for it in real_content:
            one_table=parseSQL2json2(it)
            tables.append(one_table)
        json_data["Tables"]=tables
        import numpy as np
        json_data["Constraints"]["table-query access distribution"]\
            =np.full(len(json_data["Tables"]),1.0/len(json_data["Tables"])).tolist()

        with open(args.config_file, "w") as f:
            json.dump(json_data, f, indent=4)
            print("parse succeeded.")
            print("result written in res.json.")


        wp = WP2()
        wp.parse_schema(args.config_file)
        static = wp.parse_workload(args.workload_path)
        feature = inner + wdr_metrics + static
    else:
        feature = inner + wdr_metrics
    return feature

def get_mapping_feature(db, begin, end):
    inner = db.fetch_inner_metric()
    wdr_metrics = db.get_wdr_metric(begin, end)
    if config.workload:
        parser = argparse.ArgumentParser()
        parser.add_argument('--hostname', type=str, default='10.77.10.139')
        parser.add_argument('--username', type=str, default='lzz')
        parser.add_argument('--omm_password', type=str, default='1234321abc@')
        parser.add_argument('--user_password', type=str, default='zongze123@')
        parser.add_argument('--sql_path', type=str, default='downloadsql.sql')
        parser.add_argument('--port', type=int, default=15400)
        parser.add_argument('--database_name', type=str, default='sysbench')
        parser.add_argument('--schema_name', type=str, default='public')
        parser.add_argument('--use_local', type=str, default='false')
        parser.add_argument('--cache_path', type=str, default='SuperWG/DWG/jsonHelper/data/test.sql')
        parser.add_argument('--config_file', type=str, default='SuperWG/DWG/jsonHelper/data/res.json')
        parser.add_argument('--workload_path', default='SuperWG/DWG/PressureTest/workloads/res.wg')

        args = parser.parse_args()

        if args.use_local=='false':
            command=f"gs_dump -U {args.username} -f {args.sql_path} -p {args.port} -s {args.database_name} -n {args.schema_name} -F p"
            stdin, stdout, stderr = db.ssh.exec_command(command=command)
            stdin.write(f'{args.user_password}\n')
            stdin.flush()
            output = stdout.read().decode()
            print(output)

            sftp_client = db.ssh.open_sftp()
            sftp_client.get(localpath=args.cache_path, remotepath=args.sql_path)
            sftp_client.close()

            with open(args.cache_path, 'r') as f:
                content=f.read()
            # print(type(content),len(content))
        else:
            with open(args.sql_path, 'r') as f:
                content=f.read()
            # print(type(content),len(content))  

        content_split=re.split('[\n]*;+[\n]*',content)
        print(len(content_split))
        real_content=[]
        for it in content_split:
            filter_pattern = r"(CREATE TABLE .*)WITH"
            if re.search(pattern=filter_pattern,string=it,flags=re.DOTALL)!=None:
                real_content.append(it)

        json_data={
            "Table Schema": "noobschema",
            "Tables": [],
            "Constraints": {
            "size of workload" : 1000,
            "read write ratio": 0.9,
            "average table num": [0.5,0.5],
            "table-query access distribution": [],
            "query comparison operator ratio" : [0.25,0.25,0.25,0.25],
            "table domain distribution" : [0.5,0.5],
            "query logic predicate num" : [0.4,0.4,0.2],
            "average aggregation operator num" : [0.5,0.3,0.2],
            "average query colomn num":[0,0.4,0.3,0.3],
            "group by ratio if read SQL":[0.8,0.2],
            "order by desc or asc if grouped":[0.85,0.15]
            },
            "Generation File":"../res/res.wg"
        }

        tables=[]
        for it in real_content:
            one_table=parseSQL2json2(it)
            tables.append(one_table)
        json_data["Tables"]=tables
        import numpy as np
        json_data["Constraints"]["table-query access distribution"]\
            =np.full(len(json_data["Tables"]),1.0/len(json_data["Tables"])).tolist()

        with open(args.config_file, "w") as f:
            json.dump(json_data, f, indent=4)
            print("parse succeeded.")
            print("result written in res.json.")


        wp = WP2()
        wp.parse_schema(args.config_file)
        static = wp.parse_workload(args.workload_path)
        feature = inner + wdr_metrics + static
    else:
        feature = inner + wdr_metrics
    return feature


def update_knowledge(feature, id, knowledge_path):
    with open(knowledge_path, "r") as k:
        knowledge_len = len(k.readlines())
        print(knowledge_len)
    if knowledge_len == 0:
        knowledge = dict()
    else:
        with open(knowledge_path, "r") as k:
            knowledge = json.load(k)
    key = ''
    feature = str([float(i) for i in feature])
    for s in feature[1:-1].split(','):
        key = key + s
    knowledge[key] = id
    with open(knowledge_path, "w") as f:
        s = json.dumps(knowledge, indent=4)
        f.writelines(s)

def string2list(s):
    s = s.split(' ')
    data = []
    for i in range(len(s)):
        data.append(float(s[i]))
    return data

def mapping(feature, knowledge_path):
    # 如果知识库为空, 则匹配失败
    with open(knowledge_path, 'r') as f:
        if len(f.readlines()) == 0:
            return None

    with open(knowledge_path, 'r') as f:
        knowledge_dict = json.load(f)
        # 如果只有1条, 直接返回, 无需匹配
        if len(knowledge_dict) == 1:
            key = list(knowledge_dict.keys())[0]
            return knowledge_dict[key]

        # 匹配知识库
        min_dist = 99999999999
        familiar = None
        # 将knowledge_dict中的所有key (feature) 转换成二维数组, 便于匹配时归一化各维数据
        keys = []
        for k in knowledge_dict:
            if len(k.split(' ')) != len(feature):
                continue
            keys.append(np.array(string2list(k)))
        keys = np.array(keys)

        max_val = np.max(keys, axis=0)
        min_val = np.min(keys, axis=0)
        norm = max_val - min_val
        # 处理除零问题
        norm[norm == 0] = min_val[norm == 0]
        norm[norm == 0] = 1
        for k in keys:
            dist = np.sqrt(np.sum((np.array(feature) - k) ** 2 / norm ** 2))
            if dist < min_dist:
                min_dist = dist
                key = ''
                tmp = str(k.tolist())[1:-1].split(',')
                for t in tmp:
                    key = key + t
                familiar = knowledge_dict[key]
    return familiar


