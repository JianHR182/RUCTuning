import json

# from Database import Database
#
# db = Database()
# db.get_conn()

import threading
import time

from knob_ranking.shap_final import knob_selection

knob_selection(records='testrecord',
                       knobs_config='knobs_config/knobs-13.json',
                       ranking_results='ranked_knob/knobs_13_ranked.json',
                       knob_num=13)
