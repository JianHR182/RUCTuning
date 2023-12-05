from annoy import AnnoyIndex
import json
import os
import numpy as np


def build_index():
    with open("knowledge.json", "r") as f:
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
    fea = feature.strip().split(' ')
    fea = [float(i) for i in fea]
    dim = len(fea)
    u = AnnoyIndex(dim, "euclidean")
    u.load("{}dims.ann".format(dim))
    index = u.get_nns_by_vector(fea, 10)
    features = []
    for i in index:
        features.append(u.get_item_vector(i))
    u.unload()
    return features

def string2list(s):
    s = s.split(' ')
    data = []
    for i in range(len(s)):
        data.append(float(s[i]))
    return data


# def build_index(knowledge_path):
#     with open(knowledge_path, "r") as f:
#         data = f.read()
#     if data:
#         knowledge = json.loads(data)
#         features = []
#         features_str = knowledge.keys()
#         scale_factor = int(1e20)
#         for fea in features_str:
#             vector = fea.strip().split(' ')
#             vector = [round(i * scale_factor) for i in vector]
#             features.append(vector)
#         # 带静态指标和不带静态指标分开建立索引
#         dim = len(features[0])
#         print(features[0])
#         t = AnnoyIndex(dim, "euclidean")
#         i = 0
#         restfeas = []
#         for fea in features:
#             if len(fea) != dim:
#                 restfeas.append(fea)
#                 continue
#             t.add_item(i, fea)
#             i += 1
#         # 树的数量为10，树的数量影响建立索引的时间和准确度，建立森林是为了解决“真实的 Top K 中部分点不在这个区域”
#         t.build(10)
#         t.save("{}dims.ann".format(dim))
#         test = t.get_item_vector(0)
#         print([i / scale_factor for i in test])
#
#         dim = len(restfeas[0])
#         tr = AnnoyIndex(dim, "euclidean")
#         i = 0
#         for fea in restfeas:
#             tr.add_item(i, fea)
#             i += 1
#         tr.build(10)
#         tr.save("{}dims.ann".format(dim))
#
#
# def get_top10(feature):
#     dim = len(feature)
#     # 读入索引文件进行查找
#     u = AnnoyIndex(dim, "euclidean")
#     u.load("{}dims.ann".format(dim))
#     # 得到的是top10特征的下标
#     index = u.get_nns_by_vector(feature, 10)
#     features = []
#     for i in index:
#         # 得到特征值
#         features.append(u.get_item_vector(i))
#     u.unload()
#     print(features)
#     return features

if __name__ == "__main__":
    # test_fea1 = "35.3 53.8 2.0 0.00018547157201923614 9.0 92.3917588163385 100.0 7.0 608533.0 133987231894.0 38.0 52085.0 108704.0 2830316.0 5466.0 844630.0 0.0 0.0 539397369.0 228.0"
    # fea1 = get_top10(test_fea1)
    # print(fea1)

    # test_fea2 = "0.0 84.7 2.0 0.00010619788249587453 9.0 1918.64174819668 77.0 34.0 121.0 923612.0 0.0 0.0 19833.0 471314.0 141.0 158885.0 0.0 0.0 1134.0 4315.0 100000.0 0.9471960057301761 0.11313937810735654 0.004002696553467599 0.37180837616920875 1.7557196427066655"
    # fea2 = get_top10(test_fea2)
    # print(fea2)

    with open("knowledge.json", 'r') as f:
        knowledge_dict = json.load(f)
    print(knowledge_dict)
    for k in knowledge_dict.keys():
        print(k)
    # keys = []
    # for k in knowledge_dict:
    #     print(len(k.split(' ')))
    #     print(k)
    #     keys.append(np.array(string2list(k)))
    # keys = np.array(keys)
    # print(keys)