#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import string
import json


def ModifyMSConf(ice_addr,kafka_brokers,zookeeper_servers,ma_topic,destdir, ma_dirname):

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

    ma_conf_path = "{0}/{1}/conf/init.properties".format(destdir, ma_dirname)
    with open(ma_conf_path, "w") as f:
        f.write(new_content)

def StartMA(destdir,ma_dirname):

    os.chdir("{0}/{1}/bin".format(destdir, ma_dirname))
    pid = subprocess.Popen(["./ma_start.sh"]).pid

###### record

# stream_installer.save_service_status(
#     name="ma",
#     script="{0}/{1}/bin/ma_stop.sh".format(destdir, ma_dirname),
#     pid=[])
