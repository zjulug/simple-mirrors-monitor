__author__ = 'vxst'

import urllib.request
import compare
import time
import tstt

def check_it():
    checkURL = "http://mirrors.zju.edu.cn/debian/project/trace/ftp-master.debian.org"
    with urllib.request.urlopen(checkURL) as response:
        plain_string = response.read()
        time_line = plain_string.decode().split("\n")[0]
        timestruct = time.strptime(time_line, "%a %b  %d %H:%M:%S %Z %Y")
        timestamp = tstt.convert(timestruct, tstt.find_tmzone(time_line))
        return compare.compare(timestamp, 3600 * 24 * 1.5)
