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


def get_knobs_detail(path, num):
    f = open(path, 'r')
    content = json.load(f)
    content = set_expert_rule(content)

    result = {}
    count = 0
    for i in content.keys():
        result[i] = content[i]
        count += 1
        if count == num:
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
    content['max_process_memory']['max'] = int(memory_kb * 0.9)
    content['max_process_memory']['min'] = int(memory_kb * 0.8)

    content['shared_buffers']['max'] = int(memory_kb / 8 * 0.3)
    content['shared_buffers']['min'] = int(memory_kb / 8 * 0.05)

    content['maintenance_work_mem']['max'] = content['max_process_memory']['min']

    content['work_mem']['max'] = content['max_process_memory']['min']

    content['effective_cache_size']['max'] = content['max_process_memory']['min']

    return content


def analyse_result(id):
    max_tps = 0
    best_config = {}
    with open('history_results/{}'.format(id), 'r') as f:
        lines = f.readlines()
        for l in lines:
            data = json.loads(l)
            tps = data['tps']
            if tps > max_tps:
                max_tps = tps
                best_config = data
    best_config.pop('tps')
    return best_config, max_tps


def save_result(best_knob, max_tps, init_tps, id, mode):
    with open(config.final_results, 'a') as f:
        f.writelines(str(mode) + '\t' + str(id) + '\t' + str(best_knob) + '\t' + str(max_tps) + '\t' + str(init_tps) + '\n')
