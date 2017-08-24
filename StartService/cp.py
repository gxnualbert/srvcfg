#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import subprocess


#由于CP没有配置文件，所以直接启动CP。

def StartCP(cp_ip,cp_port,ice_addr,session_app_id,instance_id,sc_group_topic,kafka_brokers,zookeeper_servers,destdir,cp_dirname):
    os.chdir("/{0}/{1}".format(destdir, cp_dirname))
    pid = subprocess.Popen(["./test_proxy",
                            cp_ip, cp_port,
                            ice_addr,
                            session_app_id, instance_id,
                            sc_group_topic, kafka_brokers,
                            zookeeper_servers]).pid
