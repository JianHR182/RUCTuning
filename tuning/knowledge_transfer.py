import json
import numpy as np
import config
from SuperWG.DWG.WP.WorkloadParser import WP2
import argparse
import re
from SuperWG.DWG.jsonHelper.jsonHelper import parseSQL2json2
from annoy import AnnoyIndex
import os

threshold = 500
step = 1

def get_train_feature(db, begin, end):
    inner = db.fetch_inner_metric()
    wdr_metrics = db.get_wdr_metric(begin, end)

    if config.static and config.benchmark == 'dwg':
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

        if args.use_local == 'false':

            command = "gs_dump -U {} -f {} -p {} -s {} -n {} -F p ".format(args.username, args.sql_path, args.port,
                                                                           args.database_name, args.schema_name)
            # command = "gs_dump -U jikun -f /home/tianjikun/schema/test.sql -p 15400 dwg -n public -F p"
            print("command : ", command)
            stdin, stdout, stderr = db.ssh.exec_command(command=command)
            stdin.write(args.user_password + '\n')
            stdin.flush()
            output = stdout.read().decode()
            print(output)

            sftp_client = db.ssh.open_sftp()
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

        if args.use_local == 'false':

            command = "gs_dump -U {} -f {} -p {} -s {} -n {} -F p ".format(args.username, args.sql_path, args.port,
                                                                           args.database_name, args.schema_name)
            # command = "gs_dump -U jikun -f /home/tianjikun/schema/test.sql -p 15400 dwg -n public -F p"
            print("command : ", command)
            stdin, stdout, stderr = db.ssh.exec_command(command=command)
            stdin.write(args.user_password + '\n')
            stdin.flush()
            output = stdout.read().decode()
            print(output)

            sftp_client = db.ssh.open_sftp()
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
        # 设定建立二叉树的最小知识库大小以及步长
        if len(knowledge) >= threshold and len(knowledge) % step == 0:
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

        # 判断知识库大于最小阈值
        if len(knowledge_dict) >= threshold:
            isann = False
            current_directory = os.path.dirname(os.path.abspath(__file__))
            for filename in os.listdir(current_directory):
                # 判断是否已经建立索引
                if filename.endswith(".ann"):
                    isann = True
                    break
            if isann:
                print("--------------从知识库中查找---------------")
                familiar = get_familar(feature)
                return familiar

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



def format(knowledge_path):
    with open(knowledge_path, 'r') as f:
        if len(f.readlines()) == 0:
            return None

    with open(knowledge_path, 'r') as f:
        knowledge_dict = json.load(f)

    acc = 7
    factor = 1e7
    # 将knowledge_dict中的所有key (feature) 转换成二维数组, 便于匹配时归一化各维数据
    keys_20 = []
    value_20 = []
    keys_26 = []
    value_26 = []
    for k in knowledge_dict.keys():
        value = knowledge_dict[k]
        k = string2list(k)
        if len(k) == 20:
            keys_20.append(np.array(k))
            value_20.append(value)
        if len(k) == 26:
            keys_26.append(np.array(k))
            value_26.append(value)

    keys_20 = np.array(keys_20)
    keys_26 = np.array(keys_26)

    max_val = np.max(keys_20, axis=0)
    min_val = np.min(keys_20, axis=0)
    norm = max_val - min_val
    norm[norm == 0] = 1
    min = [str(i) for i in min_val.tolist()]
    min = ' '.join(min)
    norm_20 = [str(i) for i in norm.tolist()]
    norm_20 = ' '.join(norm_20)

    data_dict = {}
    data_dict["min_20"] = min
    data_dict["norm_20"] = norm_20
    for k, v in zip(keys_20, value_20):
        format_k = (k - min_val) / norm
        format_k = [round(float(i), acc) for i in format_k.tolist()]
        format_k = [str(int(i * factor)) for i in format_k]
        format_k = ' '.join(format_k)
        data_dict[format_k] = v


    max_val = np.max(keys_26, axis=0)
    min_val = np.min(keys_26, axis=0)
    norm = max_val - min_val
    norm[norm == 0] = 1
    min = [str(i) for i in min_val.tolist()]
    min = ' '.join(min)
    norm_26 = [str(i) for i in norm.tolist()]
    norm_26 = ' '.join(norm_26)

    data_dict["min_26"] = min
    data_dict["norm_26"] = norm_26
    for k, v in zip(keys_26, value_26):
        format_k = (k - min_val) / norm
        format_k = [round(float(i), acc) for i in format_k.tolist()]
        format_k = [str(int(i * factor)) for i in format_k]
        format_k = ' '.join(format_k)
        data_dict[format_k] = v

    with open("buildtree_data.json", 'w') as f:
        data = json.dumps(data_dict, indent=4)
        f.writelines(data)


def build_index(knowledge_path):
    format(knowledge_path)
    with open("buildtree_data.json", "r") as f:
        data = f.read()
    if data:
        knowledge = json.loads(data)
        del knowledge['min_20']
        del knowledge['min_26']
        del knowledge['norm_20']
        del knowledge['norm_26']
        features = []
        features_str = knowledge.keys()
        for fea in features_str:
            vector = fea.strip().split(' ')
            vector = [int(i) for i in vector]
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
        test = t.get_item_vector(0)

        dim = len(restfeas[0])
        tr = AnnoyIndex(dim, "euclidean")
        i = 0
        for fea in restfeas:
            tr.add_item(i, fea)
            i += 1
        tr.build(10)
        tr.save("{}dims.ann".format(dim))

def get_familar(feature):
    dim = len(feature)
    acc = 7
    factor = 1e7

    fea = np.array(feature)
    with open("buildtree_data.json", "r") as f:
        data = json.load(f)
    min = "min_{}".format(dim)
    norm = "norm_{}".format(dim)

    min = string2list(data[min])
    norm = string2list(data[norm])

    min = np.array(min)
    norm = np.array(norm)

    format_k = (fea - min) / norm
    format_k = [round(float(i), acc) for i in format_k]
    format_k = [int(i * factor) for i in format_k]

    # print(format_k)

    # 读入索引文件进行查找
    u = AnnoyIndex(dim, "euclidean")
    u.load("{}dims.ann".format(dim))
    # 得到的是top10特征的下标
    index = u.get_nns_by_vector(format_k, 1)
    # features = []
    # for i in index:
    #     # 得到特征值
    #     features.append(u.get_item_vector(i))
    vector = u.get_item_vector(index[0])
    u.unload()
    # print(features)
    vector = [str(int(i)) for i in vector]
    familiar = ' '.join(vector)
    return data[familiar]

if __name__ == "__main__":
    # format(config.knowledge)
    # build("buildtree_data.json")

    fea = "0.0 10.9 2.0 0.00014007859346543068 9.0 505.162224388209 38.0 -62094900.0 0.0 0.0 -100.0 -1576541.0 15140.0 286394.0 2360.0 86134.0 152.0 76.0 1224.0 -17326.0"
    fea = string2list(fea)
    # print(fea)
    f = get_familar(fea)
    print(f)


