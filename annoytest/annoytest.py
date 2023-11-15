from annoy import AnnoyIndex
import json


def build_index():
    with open("knowledge.json", "r") as f:
        data = f.read()
    if data:
        knowledge = json.loads(data)
        features = []
        features_str = knowledge.keys()
        for fea in features_str:
            vector = fea.strip().split(' ')
            vector = [float(i) for i in vector]
            features.append(vector)
        dim = len(features[0])
        t = AnnoyIndex(dim, "euclidean")
        for i,fea in zip(range(len(features)), features):
            t.add_item(i, fea)
        t.build(10)
        t.save("test.ann")


def get_top10(feature):
    fea = feature.strip().split(' ')
    fea = [float(i) for i in fea]
    dim = len(fea)
    u = AnnoyIndex(dim, "euclidean")
    u.load("test.ann")
    index = u.get_nns_by_vector(fea, 10)
    features = []
    for i in index:
        features.append(u.get_item_vector(i))
    u.unload()
    return features

if __name__ == "__main__":
    test = "35.3 53.8 2.0 0.00018547157201923614 9.0 92.3917588163385 100.0 7.0 608533.0 133987231894.0 38.0 52085.0 108704.0 2830316.0 5466.0 844630.0 0.0 0.0 539397369.0 228.0"
    top10_feas = get_top10(test)
    print(top10_feas)

