import json

# from Database import Database
#
# db = Database()
# db.get_conn()
import os

import threading
import time

out = os.popen('free -g')
res = out.readlines()[1].split()[1]
print(res)
