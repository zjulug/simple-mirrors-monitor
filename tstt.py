# Convert tm_struct to unix timestamp with the CORRECT timezone
__author__ = 'vxst'
import pytz
import datetime
import re

def convert(tm_info, tm_zone):
    timezone = pytz.timezone(tm_zone)
    utc = pytz.timezone("UTC")
    epoch = datetime.datetime(1970, 1, 1, 0, 0, 0, 0, utc)
    return (datetime.datetime(tm_info.tm_year, tm_info.tm_mon, tm_info.tm_mday, tm_info.tm_hour,
                                   tm_info.tm_min, tm_info.tm_sec, 0, timezone)-epoch).total_seconds()

def find_tmzone(str):
    q1 = re.compile('\d*:\d*:\d*\s*.*')
    q2 = re.compile('\w{3}')

    q1res = q1.findall(str)[0]
    q2res = q2.findall(q1res)[0]

    return q2res