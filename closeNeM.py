#!usr/bin/python3

import sys
import os
from time import sleep

closeCmd = "killall \"NeteaseMusic\"" 
mins = 10
if len(sys.argv) == 2:
    mins = float(sys.argv[1])
	
for i in range(int(mins * 60), 0, -1):
    sleep(1)
    print('Remaining ', i // 60, ' mins ', i % 60, ' seconds')

os.system(closeCmd)