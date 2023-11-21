import datetime
import json
import logging
import pandas as pd
import config


def get_logger(log_file):
    path = log_file
    logger = logging.getLogger(path)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(path)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('[%(asctime)s:%(filename)s#L%(lineno)d:%(levelname)s]: %(message)s'))

    logger.addHandler(handler)
    return logger


def get_knobs_detail(path):
    f = open(path, 'r')
    content = json.load(f)
    content = set_expert_rule(content)

    result = {}
    for i in content.keys():
        result[i] = content[i]
    return result


def load_sampling_data(sampling_log):
    with open(sampling_log, 'r') as f:
        lines = f.readlines()[:]

    records = []
    for line in lines:
        records.append(json.loads(line))

    data = pd.DataFrame(records)

    return data


def set_expert_rule(content):
    memory_kb = config.memory * 1024 * 1024
    if 'max_process_memory' in content.keys():
        content['max_process_memory']['max_val'] = int(memory_kb * 0.9)
        content['max_process_memory']['min_val'] = int(memory_kb * 0.8)

    if 'shared_buffers' in content.keys():
        content['shared_buffers']['max_val'] = int(memory_kb / 8 * 0.3)
        content['shared_buffers']['min_val'] = int(memory_kb / 8 * 0.05)

    if 'maintenance_work_mem' in content.keys() and 'max_process_memory' in content.keys():
        content['maintenance_work_mem']['max_val'] = content['max_process_memory']['min_val']

    if 'work_mem' in content.keys() and 'max_process_memory' in content.keys():
        content['work_mem']['max_val'] = content['max_process_memory']['min_val']

    if 'effective_cache_size' in content.keys() and 'max_process_memory' in content.keys():
        content['effective_cache_size']['max_val'] = content['max_process_memory']['min_val']

    return content


def analyse_result(id, mode):
    max_tps = -1
    best_config = {}
    with open('history_results/{}'.format(id), 'r') as f:
        lines = f.readlines()
        # 微调结果文件的前两行是默认配置和在线匹配的结果, 需要剔除
        if mode == 'fine_tune':
            lines = lines[2:]

        for l in lines:
            data = json.loads(l)
            if 'tps' not in data:
                continue
            tps = data['tps']
            if tps > max_tps:
                max_tps = tps
                best_config = data
    best_config.pop('tps')
    return best_config, max_tps


def save_result(best_knob, max_tps, init_tps, mode):
    with open(config.final_results, 'a') as f:
        f.writelines(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(mode) + '\t' +
                     str(best_knob) + '\t' + str(max_tps) + '\t' + str(init_tps) + '\n')
