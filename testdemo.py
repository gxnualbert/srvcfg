#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: testdemo.py
@time: 2017/08/26/7:48 AM
"""
import  time

def get_host_suffix(self, host):
    return host.split(".")[-1]

aa=time.strftime('%Y-%m-%d',time.localtime(time.time()))

print aa.replace("-","_")

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


import datetime
starttime = datetime.datetime.now()
#long running
time.sleep(3)
endtime = datetime.datetime.now()
print (endtime - starttime).seconds