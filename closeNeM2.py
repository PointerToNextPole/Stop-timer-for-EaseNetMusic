#!usr/bin/python3

import sys
import os
import time
from time import sleep

closeCmd = "killall \"NeteaseMusic\"" 
mins = 10
if len(sys.argv) == 2:
    time_argv = sys.argv[1]
    if ':' not in time_argv:
        mins = float(time_argv)
        remains_sec = int(mins*60)

    else:
        target_time = time_argv.split(':')
        for i in target_time:
            if not i.isnumeric():
                print('[ERROR]: Your target time\'s type is wrong!!!')
                exit()

        target_hour, target_min, tagret_sec = int(target_time[0]), int(target_time[1]), 0
        if target_hour < 0 or target_hour > 23:
            print('[ERROR]: Your target hour is wrong!!!\nPlease ensure your target hour ranges between 0 and 23')
            exit()
        if target_min < 0 or target_min > 59:
            print('[ERROR]: Your target min is wrong!!!\nPlease ensure your target min ranges between 0 and 59!')
            exit()

        cur_time = time.localtime(time.time())
        cur_hour, cur_min, cur_sec = cur_time[3], cur_time[4], cur_time[5]

        remains_sec = ((target_hour - cur_hour + 24) % 24) * 3600 + (target_min - cur_min) * 60 + (tagret_sec - cur_sec)

    for i in range(remains_sec, 0, -1):
        remains_hour = i // 60
        remains_sec = i %60
        min_type = 'mins'
        if remains_hour in (0, 1):
            min_type = 'min'
        sec_type = 'secs'
        if remains_sec in (0, 1):
            sec_type = 'sec'
        print('Remaining: (', remains_hour, min_type, remains_sec, sec_type, ')')
        sleep(1)

    os.system(closeCmd)
