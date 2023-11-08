import json
f = open('/home/puzhao/opengauss_tuning/knobs_config/knobs-151.json', 'r')
content = json.load(f)

result = {}
count = 0
print(len(content.keys()))