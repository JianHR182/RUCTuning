import json
import os

import config
from Database import Database
from knob_ranking.shap_final import knob_selection
from knowledge_transfer import update_knowledge, mapping
from tuner import tuner
from utils import analyse_result, save_result

if __name__ == '__main__':

    # 查询系统内存
    out = os.popen('free -g')
    res = out.readlines()[1].split()[1]
    config.memory = int(res)

    db = Database()
    t = tuner(db)

    # 0. 备份postgresql.conf, 测试初始性能
    print('测试初始配置性能...')
    # 如果没有备份配置文件, 则备份
    out = os.popen('find {} -name postresql_bak.conf'.format(config.opengauss_node_path))
    res = out.readlines()
    if len(res) == 0:
        os.popen('cp {}/postgresql.conf {}/postgresql_bak.conf'.format(config.opengauss_node_path,
                                                                   config.opengauss_node_path))
    init_config = db.fetch_knob()
    init_tps = t.stt.test_config(init_config)
    print('初始配置性能为: tps = {}'.format(init_tps))

    # offline tuning
    if not config.online:
        # 1. 离线调优
        t.tune()
        # 2. 结果整理: 初始与最优的对比
        print('offline tuning over')
        best_knob, max_tps = analyse_result(t.id)
        save_result(best_knob, max_tps, init_tps, t.id, 'offline')
        print('best knob is {}\nmax_tps is {}\t initial tps is {}'.format(best_knob, max_tps, init_tps))
        # 3. 参数排名
        knob_selection(records='history_results/{}'.format(t.id),
                       knobs_config=config.knobs_file,
                       ranking_results='ranked_knob/{}_knob_{}.json'.format(config.ranked_knobs_number, t.id),
                       knob_num=config.ranked_knobs_number)

        # 3. 存入知识库
        feature = db.fetch_inner_metric()
        update_knowledge(feature=feature,
                         id=t.id,
                         knowledge_path=config.knowledge)

        # 排序好的knob在knobs_config/ranked_knob_{id}.json里
        # 调优记录在history_results/{id}里
        # 知识库的格式 inner_metrics: id   通过id可以找到ranked_knob以及records

        # 4. 恢复postgresql.conf
        os.popen('cp {}/postgresql_bak.conf {}/postgresql.conf'.format(config.opengauss_node_path,
                                                                       config.opengauss_node_path))
    # online tuning
    else:
        # 1. 负载匹配
        # 匹配所需要的key从Database.py里查询, 看情况修改Database.py里的fetch_inner_metric方法
        #
        # 知识库匹配获取id
        feature = db.fetch_inner_metric()
        id = mapping(feature=feature,
                     knowledge_path=config.knowledge)
        print('最相似的历史调优记录为: {}'.format(id))
        # 2. 应用最优配置, 测试性能, 与初始性能对比
        best_knob, _ = analyse_result(id)

        max_tps = t.stt.test_config(best_knob)

        print('匹配到的最优参数为: {}\n最优性能为: {}'.format(best_knob, max_tps))
        # 整理在线调优结果
        save_result(best_knob, max_tps, init_tps, t.id, 'online')

        # 3. 微调
        if config.finetune:
            print('开始微调...')
            config.knobs_file = '{}_knob_{}.json'.format(config.ranked_knobs_number, id)
            t.HEBO(id)
            # 整理微调结果
            best_knob, max_tps = analyse_result(t.id)
            save_result(best_knob, max_tps, init_tps, t.id, 'fine_tune')
            print('微调最优参数为: {}\n最优性能为: {}'.format(best_knob, max_tps))
