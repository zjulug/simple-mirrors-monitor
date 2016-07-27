__author__ = 'vxst'

import urllib.request
import compare

def check_it():
    checkURL = "http://mirrors.zju.edu.cn/archlinux/lastupdate"
    with urllib.request.urlopen(checkURL) as response:
        plain_string = response.read()
        timestamp = int(plain_string)
        return compare.compare(timestamp, 3600 * 12)