#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import string
import json

# import stream_installer

###### install



def ModifyMSConf(kafka_brokers,zookeeper_servers,ice_addr,ms_topic,sc_ms_topic,destdir,ms_dirname):
     t_config = """
    application.name=ms

    bootstrap.servers=$kafka_brokers
    zookeeper.servers=$zookeeper_servers
    retry.policy=0
    zk.acl.name=ma
    zk.acl.password=123456
    ice.addr=$ice_addr
    topic.ms=$ms_topic
    topic.partions=1
    topic.replication=1
    topic.sc.py.group1.name = $sc_ms_topic
    poll.time=10


    master.path=/fsp/master/ms
    node.ma.parent=/fsp/ma
    service.parent.node=/fsp/ms
    access.path=/fsp/access
    gc.py.path=/fsp/gc.py
    rule.py.path=/fsp/rule.py
    sc.py.path=/fsp/sc.py
    sp.path=/fsp/sp
    cp.path=/fsp/cp
    ice.path=/fsp/ice
    ss.path=/fsp/ss
    gs.path=/fsp/gs
    cpu.overload = 0.8
    mem.overload = 0.8
    bindwidth.overload = 0.8
    """

     items = {}

     # items["ice_addr"] = "DBIceGrid/Locator:default -h 192.168.7.84 -p 10000:default -h 192.168.7.85 -p 10001"
     # items["kafka_brokers"] = "192.168.7.84:9092,192.168.7.85:9092,192.168.7.86:9092"
     # items["zookeeper_servers"] = "192.168.7.84:2181,192.168.7.85:2181,192.168.7.86:2181"

     items["ice_addr"] = ice_addr
     items["kafka_brokers"] = kafka_brokers
     items["zookeeper_servers"] = zookeeper_servers
     items["ms_topic"] = ms_topic
     items["sc_ms_topic"] = sc_ms_topic
     t = string.Template(t_config)
     new_content = t.substitute(items)
     # return new_content
     ms_conf_path = "{0}/{1}/conf/init.properties".format(destdir, ms_dirname)
     with open(ms_conf_path, "w") as f:
          f.write(new_content)

def StartMS(destdir,ms_dirname):
     os.chdir("{0}/{1}/bin".format(destdir, ms_dirname))
     pid = subprocess.Popen(["./ms_start.sh"]).pid














