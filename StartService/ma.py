#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os,sys

import subprocess
import string



def ModifyMSConf(ice_addr,kafka_brokers,zookeeper_servers,ma_topic,ma_construct_file_path):

    t_config = """
application.name=ma
bootstrap.servers=$kafka_brokers
zookeeper.servers=$zookeeper_servers
retry.policy=0
zk.acl.name=ma
zk.acl.password=123456
ice.addr=$ice_addr
service.parent.node=/fsp/ma
node.ma.topic=$ma_topic
topic.partions=1
topic.replication=1
ping.times= 5
ping.timeout= 10
distance.expression = (p(L+1,2)-1)*32+D
ma.bandwidth=1000

    """

    items = {}

    items["ice_addr"] = ice_addr
    items["kafka_brokers"] = kafka_brokers
    items["zookeeper_servers"] = zookeeper_servers

    items["ma_topic"] = ma_topic


    t = string.Template(t_config)
    new_content = t.substitute(items)

    with open(ma_construct_file_path+"/init.properties", "w") as f:
        f.write(new_content)



if __name__ == "__main__":

    FILE_PATH="/fsp_sss_stream"
    if os.path.exists(FILE_PATH):
        print  "path:%s exits" % FILE_PATH
    else:
        os.makedirs(FILE_PATH)
    subprocess.Popen(["/fsp_sss_stream/fsp-ma-1.0-SNAPSHOT/bin/ma_start.sh"], shell=True)
