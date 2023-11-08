import os
import sys
sys.path.append('/home/puzhao/opengauss_tuning')
from utils import get_knobs_detail

knobs = get_knobs_detail('/home/puzhao/opengauss_tuning/knobs_config/knobs-23.json',23).keys()

set_knobs_command =''
for knob in knobs:
    set_knobs_command += 'gs_guc set -c "{}" -D /home/omm/data;'.format(knob)
command = 'sshpass -p opgs1234321# ssh omm@2408:400a:bd:b900:126f:c207:760a:8912 "{}"'.format(set_knobs_command)

os.system(command)

