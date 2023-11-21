import os

import config
import utils
from Database import Database
from knob_ranking.shap_final import knob_selection
from knowledge_transfer import update_knowledge, mapping, get_train_feature, get_mapping_feature
from tuner import tuner
from utils import analyse_result, save_result

if __name__ == '__main__':

    # 查询系统内存
    out = os.popen('free -g')
    res = out.readlines()[1].split()[1]
    config.memory = int(res) + 1

    # 初始化数据库实例, 创建数据库连接, 修改参数, 查询数据库状态, 重启等操作
    db = Database()

    # 初始化调优模型
    t = tuner(db)

    # 0. 备份postgresql.conf, 测试初始性能
    print('测试初始配置性能...')
    # 如果没有备份配置文件, 则备份; 反之确保数据库恢复初始状态
    out = os.popen('find {} -name postgresql_bak.conf'.format(config.opengauss_node_path))
    res = out.readlines()
    if len(res) == 0:
        os.popen('cp {}/postgresql.conf {}/postgresql_bak.conf'.format(config.opengauss_node_path,
                                                                       config.opengauss_node_path))
    else:
        os.popen('cp {}/postgresql_bak.conf {}/postgresql.conf'.format(config.opengauss_node_path,
                                                                       config.opengauss_node_path))
        db.restart()

    # 测试初始配置性能
    init_config = db.fetch_knob()
    init_tps = t.stt.test_config(init_config)
    print('初始配置性能为: tps = {}'.format(init_tps))

    # offline tuning
    if not config.online:
        # 1. 离线调优
        begin = db.get_snapshot()
        t.tune()
        end = db.get_snapshot()
        feature = get_train_feature(db, begin, end)
        # 2. 结果整理: 初始与最优的对比, 结果保存在final_results中
        print('offline tuning over')
        best_knob, max_tps = analyse_result(t.id, 'offline')
        save_result(best_knob, max_tps, init_tps, 'offline')
        print('best knob is {}\nmax_tps is {}\t initial tps is {}'.format(best_knob, max_tps, init_tps))
        # 3. 参数排名
        knob_selection(records='history_results/{}'.format(t.id),
                       knobs_config=config.knobs_file,
                       ranking_results='ranked_knob/knob_{}.json'.format(t.id),
                       knob_num=config.ranked_knobs_number)
        print('参数排名完成, 从{}个参数中选取最重要的{}个, 结果保存在ranked_knob/knob_{}.json'.format(t.knobs_number,
                                                                               config.ranked_knobs_number,
                                                                               t.id))
        # 3. 存入知识库
        update_knowledge(feature=feature,
                         id=t.id,
                         knowledge_path=config.knowledge)
        print('已将本次离线调优数据保存在知识库中')

        # 排序好的knob在knobs_config/ranked_knob_{id}.json里
        # 调优记录在history_results/{id}里
        # 知识库的格式 inner_metrics: id    通过id可以找到ranked_knob以及records

        # 4. 恢复postgresql.conf
        os.popen('cp {}/postgresql_bak.conf {}/postgresql.conf'.format(config.opengauss_node_path,
                                                                       config.opengauss_node_path))
        db.restart()
        print('已恢复数据库的初始配置')
    # online tuning
    else:
        # 1. 负载匹配
        # 知识库匹配获取id
        begin, end = db.get_snapshot()
        feature = get_mapping_feature(db, begin, end)
        id = mapping(feature=feature,
                     knowledge_path=config.knowledge)
        print('最相似的历史调优记录为: history_results/{}'.format(id))
        # 2. 应用最优配置, 测试性能, 与初始性能对比
        best_knob, _ = analyse_result(id, 'online')
        ranked_knobs = utils.get_knobs_detail('ranked_knob/knob_{}.json'.format(id))
        # 根据配置选择是否修改需要重启的参数
        if not config.restart_when_online:
            for k in list(best_knob.keys()):
                if db.knobs[k]['restart']:
                    del best_knob[k]
        max_tps = t.stt.test_config(best_knob)

        print('匹配到的最优参数为: {}\n最优性能为: {}'.format(best_knob, max_tps))
        # 整理在线0调优结果
        save_result(best_knob, max_tps, init_tps, 'online')

        # 3. 微调
        if config.finetune:
            print('开始微调...')
            # 根据配置选择是否修改需要重启的参数
            if not config.restart_when_online:
                for k in list(ranked_knobs.keys()):
                    if ranked_knobs[k]['restart']:
                        del ranked_knobs[k]
            db.knobs = ranked_knobs
            t.HEBO(id)
            # 整理微调结果
            best_knob, max_tps = analyse_result(t.id, 'fine_tune')
            save_result(best_knob, max_tps, init_tps, 'fine_tune')
            print('微调最优参数为: {}\n最优性能为: {}'.format(best_knob, max_tps))
