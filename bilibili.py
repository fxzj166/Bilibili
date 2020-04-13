#!/usr/bin/python
#- * -coding: utf - 8 - * -
#sudo ntpdate cn.pool.ntp.org 添加到/etc/rc.local里面实现开机自启动，同步网络时间

import os
import time, datetime
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
while 1==1:
    os.system("python /home/pi/bilibili01.py")
    second = sleeptime(0,30,0)  #刷新间隔，小时，分钟，秒，现在设置30分钟刷新一次
    time.sleep(second)
