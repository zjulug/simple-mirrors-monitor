__author__ = 'vxst'
import time

# Using UNIX Timestamp
def compare(time_dist, max_delay):
    time_now = time.time()
    time_delay = time_now - time_dist
    if(time_delay > max_delay):
        time_delay_hours = time_delay/3600.0
        information = "This dist has been not updated for {}, please check it!".format(round(time_delay_hours, 2))
        return information, False
    else:
        time_delay_hours = time_delay/3600.0
        information = "Status good, delay {} hours".format(round(time_delay_hours, 2))
        return information, True