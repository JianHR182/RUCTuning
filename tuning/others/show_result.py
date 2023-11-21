import sys
sys.path.append('.')
from utils import load_sampling_data
data=load_sampling_data('./records')
for i in range(530):
    print(data.loc[i,'shared_buffers'])
#{"wal_buffers": 1030, "shared_buffers": 2242354, "max_process_memory": 57452710, "maintenance_work_mem": 40196980, "work_mem": 17494242, "effective_cache_size": 33702379, "effective_io_concurrency": 905, "temp_buffers": 2985614, "vacuum_cost_limit": 5470, "vacuum_cost_page_dirty": 2936, "vacuum_cost_page_hit": 9683, "vacuum_cost_page_miss": 2262, "autovacuum_vacuum_cost_limit": 589, "backend_flush_after": 208, "tps": -206623.0}
