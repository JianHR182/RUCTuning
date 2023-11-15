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
        f = len(features[0])
        t = AnnoyIndex(f, "euclidean")
        for i,fea in zip(range(len(features)), features):
            t.add_item(i, fea)
        t.build(10)
        t.save("test.ann")

