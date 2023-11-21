import json
import numpy as np
import config
from SuperWG.DWG.WP.WorkloadParser import WP2
import argparse
import re
from SuperWG.DWG.jsonHelper.jsonHelper import parseSQL2json2
from annoy import AnnoyIndex
import os


def get_train_feature(db, begin, end):
    inner = db.fetch_inner_metric()
    wdr_metrics = db.get_wdr_metric(begin, end)

    if  config.static and config.benchmark == 'dwg':
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
        parser.add_argument('--cache_path', type=str, default=config.local_cache_path)
        parser.add_argument('--result_path', type=str, default=config.json_extract_result_path)

        args = parser.parse_args()

        if args.use_local=='false':
            command = "gs_dump -U {} -f {} -p {} -s {} -n {} -F p ".format(args.username, args.sql_path, args.port,
                                                                           args.database_name, args.schema_name)
            stdin, stdout, stderr = db.ssh.exec_command(command=command)
            stdin.write(f'{args.user_password}\n')
            stdin.flush()
            output = stdout.read().decode()
            # print(output)

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

        with open(args.result_path, "w") as f:
            json.dump(json_data, f, indent=4)
            print("parse succeeded.")
            print("result written in res.json.")


        wp = WP2()
        wp.parse_schema(args.result_path)
        static = wp.parse_workload(config.workload)
        feature = inner + wdr_metrics + static
    else:
        feature = inner + wdr_metrics
    return feature

def get_mapping_feature(db, begin, end):
    inner = db.fetch_inner_metric()
    wdr_metrics = db.get_wdr_metric(begin, end)
    if config.isworkload:
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
        parser.add_argument('--cache_path', type=str, default=config.local_cache_path)
        parser.add_argument('--result_path', type=str, default=config.json_extract_result_path)

        args = parser.parse_args()

        if args.use_local=='false':
            command = "gs_dump -U {} -f {} -p {} -s {} -n {} -F p ".format(args.username, args.sql_path, args.port,
                                                                           args.database_name, args.schema_name)
            stdin, stdout, stderr = db.ssh.exec_command(command=command)
            stdin.write(f'{args.user_password}\n')
            stdin.flush()
            output = stdout.read().decode()
            # print(output)

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

        with open(args.result_path, "w") as f:
            json.dump(json_data, f, indent=4)
            print("parse succeeded.")
            print("result written in res.json.")


        wp = WP2()
        wp.parse_schema(args.result_path)
        static = wp.parse_workload(config.workload)
        feature = inner + wdr_metrics + static
    else:
        feature = inner + wdr_metrics
    return feature


def update_knowledge(feature, id, knowledge_path):
    with open(knowledge_path, "r") as k:
        knowledge_len = len(k.readlines())
        # print(knowledge_len)
    if knowledge_len == 0:
        knowledge = dict()
    else:
        with open(knowledge_path, "r") as k:
            knowledge = json.load(k)
        #     知识库大于1000条，每隔100条更新一次索引
        if len(knowledge) >= 500 and len(knowledge) % 50 == 0:
            build_index(knowledge_path)
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

        # 将knowledge_dict中的所有key (feature) 转换成二维数组, 便于匹配时归一化各维数据
        keys = []
        for k in knowledge_dict.keys():
            if len(k.split(' ')) != len(feature):
                continue
            keys.append(np.array(string2list(k)))
        keys = np.array(keys)

        # 判断知识库大于1000条
        # if len(knowledge_dict) >= 1000:
        if len(knowledge_dict) >= 1 :
            isann = False
            current_directory = os.path.dirname(os.path.abspath(__file__))
            for filename in os.listdir(current_directory):
                # 判断是否已经建立索引
                if filename.endswith(".ann"):
                    isann = True
                    break
            if isann:
                # 返回top10相似负载
                top10_keys = []
                top10_feas = get_top10(feature)
                for fea in top10_feas:
                    top10_keys.append(np.array(fea))
                keys = np.array(top10_keys)
                print("从索引中查找")

        # 匹配知识库
        min_dist = 99999999999
        familiar = None

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

def build_index(knowledge_path):
    with open(knowledge_path, "r") as f:
        data = f.read()
    if data:
        knowledge = json.loads(data)
        features = []
        dims = []
        features_str = knowledge.keys()
        for fea in features_str:
            vector = fea.strip().split(' ')
            vector = [float(i) for i in vector]
            features.append(vector)
        # 带静态指标和不带静态指标分开建立索引
        dim = len(features[0])
        t = AnnoyIndex(dim, "euclidean")
        i = 0
        restfeas = []
        for fea in features:
            if len(fea) != dim:
                restfeas.append(fea)
                continue
            t.add_item(i, fea)
            i += 1
        # 树的数量为10，树的数量影响建立索引的时间和准确度，建立森林是为了解决“真实的 Top K 中部分点不在这个区域”
        t.build(10)
        t.save("{}dims.ann".format(dim))

        dim = len(restfeas[0])
        tr = AnnoyIndex(dim, "euclidean")
        i = 0
        for fea in restfeas:
            tr.add_item(i, fea)
            i += 1
        tr.build(10)
        tr.save("{}dims.ann".format(dim))


def get_top10(feature):
    fea = [float(i) for i in feature]
    dim = len(fea)
    # 读入索引文件进行查找
    u = AnnoyIndex(dim, "euclidean")
    u.load("{}dims.ann".format(dim))
    # 得到的是top10特征的下标
    index = u.get_nns_by_vector(fea, 10)
    features = []
    for i in index:
        # 得到特征值
        features.append(u.get_item_vector(i))
    u.unload()
    return features




