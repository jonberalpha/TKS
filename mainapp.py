#!/usr/bin/env python
import os
import time

os.system("xterm -e \"python /home/pi/Bierrallye/ZMS_python/TwoRC522_RPi2-3/1-TwoRC522_RPi2-3/run_main_test.py\" &")
time.sleep(2)
os.system("xterm -e \"python /home/pi/Bierrallye/ZMS_python/TwoRC522_RPi2-3/2-TwoRC522_RPi2-3/run_main_test.py\" &")
