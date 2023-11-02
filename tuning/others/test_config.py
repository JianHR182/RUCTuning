import os
import sys
sys.path.append('/home/puzhao/opengauss_tuning')
from utils import get_knobs_detail

config = {"wal_buffers": 27287, "shared_buffers": 441184, "max_process_memory": 59295757, "maintenance_work_mem": 43850188, "work_mem": 33377860, "effective_cache_size": 16930244, "effective_io_concurrency": 291, "temp_buffers": 3614192, "vacuum_cost_limit": 5450, "vacuum_cost_page_dirty": 4883, "vacuum_cost_page_hit": 796, "vacuum_cost_page_miss": 4967, "backend_flush_after": 251}






set_knobs_command =''
for knob in config:
    set_knobs_command += 'gs_guc set -c "{}={}" -D /home/omm/data;'.format(knob,config[knob])
command = 'sshpass -p opgs1234321# ssh omm@2408:400a:bd:b900:126f:c207:760a:8912 "{}"'.format(set_knobs_command)

os.system(command)