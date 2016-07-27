__author__='vxst'

import time.sleep as sleep
import check.check as check

tick = 0
while True:
    check(tick)
    tick += 1
    sleep(3600 * 2)