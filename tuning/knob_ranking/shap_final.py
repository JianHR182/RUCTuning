import argparse
from pandas.core.frame import DataFrame
import numpy as np
import shap
import xgboost
import json


# records: <knobs, performance> from puzhao
# knob-40,json: knobs to be sorted
# shap_result.json: sorted knobs to jianhaoran --- knowledge_transfer/temporary_file/knobs.json
def knob_selection(records, knobs_config, ranking_results, knob_num):
    with open(records, 'r') as f, open(knobs_config, 'r') as t, open(ranking_results, 'w') as s:
        list = f.readlines()
        knobnames = []
        knobs_value = []
        throughput = []
        title = eval(list[0])
        # 得到给定数据集中使用的参数名字
        for key0, value0 in title.items():
            if key0 != "tps":
                knobnames.append(key0)

        for line in list:
            eachturn_knobs_value = []
            if line.find("NaN") != -1:
                continue
            record = eval(line)
            for key, value in record.items():
                if key != "tps":
                    # 把每条数据中的各个参数值记录到eachturn_knobs_value列表中
                    eachturn_knobs_value.append(float(value))
                elif key == "tps":
                    # 把每条数据中的tps记录到throughput列表中
                    if float(value) > 0:
                        throughput.append(float(value))
                    else:
                        throughput.append(-float(value))
            # 把各条数据的记录列表加入knobs_value中，成为2维数组
            knobs_value.append(eachturn_knobs_value)
        df = DataFrame(knobs_value)
        df_target = np.array(throughput)
        df.columns = knobnames

        xgbmodel = xgboost.XGBRegressor().fit(df, df_target)
        explainer = shap.Explainer(xgbmodel)
        # explainer类型,用来画图
        shap_values = explainer(df)
        # ndarray类型
        shap_values2 = explainer.shap_values(df)
        result = knobsort(shap_values2, df)
        # 使用shapley值从大到小得到最终的排名
        result_order = sorted(result.items(), key=lambda x: x[1], reverse=True)

        if len(result_order) > knob_num:
            result_order = result_order[:knob_num]

        # 排序后的结果
        result_dict = dict(result_order)
        print(result_dict)

        # 利用图画检查是否和排名一致
        # shap.plots.beeswarm(shap_values, max_display=21)

        # 把排名后的数组result_dict写入json文件中
        config = json.load(t)
        count = 1
        for i in result_dict:
            result_dict[i] = config[i]
            result_dict[i]['important_rank'] = count
            count = count + 1
        # 存进json文件给到简浩然
        dumps = json.dumps(result_dict, indent=4)
        s.write(dumps)

        # 返回简浩然需要的一条字典记录
        # return result_dict


# 得到每个参数的shapley值
def knobsort(shap_values, df):
    columns = [column for column in df]
    # 存储shapley value
    shaplist = {}
    for i in range(len(columns)):
        sum = 0
        for j in range(len(shap_values)):
            sum = sum + abs(shap_values[j][i])
        shaplist.update({columns[i]: sum})
    return shaplist


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--tuning_record_path', type=str, default='../testrecord')
    parser.add_argument('--knob_config', type=str, default='knobs_config/knobs-13.json')
    parser.add_argument('--ranking_result', type=str, default='knob_config/knob_ranked_13.json')
    parser.add_argument('--knob_num', type=int, default='13')
    args = parser.parse_args()
    knob_selection(args.tuning_record_path, args.knob_config, args.ranking_result, args.knob_num)
