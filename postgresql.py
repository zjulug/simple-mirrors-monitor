__author__ = 'vxst'

import urllib.request
import compare
import time
import tstt

def check_it():
    checkURL = "http://mirrors.zju.edu.cn/postgresql/sync_timestamp"
    with urllib.request.urlopen(checkURL) as response:
        plain_string = str(response.read())
        timestruct = time.strptime(plain_string, "b'%Y-%m-%d %H:%M:%S %Z\\n'")
        timestamp = tstt.convert(timestruct, tstt.find_tmzone(plain_string))
        return compare.compare(timestamp, 3600 * 24 * 2.5)
