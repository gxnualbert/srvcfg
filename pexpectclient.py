#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: pexpectclient.py
@time: 2017/08/25/7:54 PM
"""


import pexpect

import os
import sys
import traceback
import pexpect

child=pexpect.spawn('ssh root@192.168.7.81')