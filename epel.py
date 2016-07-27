__author__ = 'vxst'

import urllib.request
import compare
import time
import re

def check_it():
    checkURL = "http://mirrors.zju.edu.cn/epel/"
    line_regex = re.compile('<a href="fullfilelist">fullfilelist</a>.*')
    date_regex = re.compile("\w*\-\w*-\w* \w*:\w*")

    with urllib.request.urlopen(checkURL) as response:
        plain_string = response.read().decode()
        time_line = date_regex.findall(line_regex.findall(plain_string)[0])[0]
        timestruct = time.strptime(time_line, "%d-%b-%Y %H:%M")
        timestamp = time.mktime(timestruct) # In local time, NO TSTT!
        return compare.compare(timestamp, 3600 * 24 * 5)
