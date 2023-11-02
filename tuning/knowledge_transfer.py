import json
import numpy as np

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


