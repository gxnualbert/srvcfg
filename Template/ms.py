#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os

import subprocess
import string

def ModifyMSConf(kafka_brokers,zookeeper_servers,ice_addr,ms_topic,sc_ms_group_topic,ms_construct_file_path):
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
topic.sc.group1.name = $sc_ms_topic
poll.time=10
master.path=/fsp/master/ms
node.ma.parent=/fsp/ma
service.parent.node=/fsp/ms
access.path=/fsp/access
gc.path=/fsp/gc
rule.path=/fsp/rule
sc.path=/fsp/sc
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


     items["ice_addr"] = ice_addr
     items["kafka_brokers"] = kafka_brokers
     items["zookeeper_servers"] = zookeeper_servers
     items["ms_topic"] = ms_topic
     items["sc_ms_topic"] = sc_ms_group_topic
     t = string.Template(t_config)
     new_content = t.substitute(items)
     # return new_content
     # ms_conf_path = "{0}/{1}/conf/init.properties".format(destdir, ms_dirname)
     # with open(ms_conf_path, "w") as f:
     #      f.write(new_content)
     with open(ms_construct_file_path + "/init.properties", "w") as f:
          f.write(new_content)













