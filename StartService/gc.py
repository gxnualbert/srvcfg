#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import string
import json


###### install


def ModifyGCConf(ice_addr,kafka_brokers,zookeeper_servers,gc_topic,gc_group_topic,sc_group_topic,consumer_client_id,destdir, gc_dirname):


    template = """
    application.name=gc
    bootstrap.servers=$kafka_brokers
    zookeeper.servers=$zookeeper_servers
    retry.policy=0
    ice.addr=$ice_addr
    topic.partions=3
    topic.replication=2
    topic.gc.name = $gc_topic
    topic.gc.group.name = $gc_group_topic
    consumer.client.id=$consumer_client_id
    topic.sc.group.name = $sc_group_topic
    message.protocol.version = 1
    max.instance.size = 10
    lock.root.path = /gclock
    lock.getStream.timeout=20
    service.parent.node=/fsp/gc
    """

    items = {}

    items["ice_addr"] = ice_addr
    items["kafka_brokers"] = kafka_brokers
    items["zookeeper_servers"] = zookeeper_servers

    items["gc_topic"] = gc_topic
    items["gc_group_topic"] = gc_group_topic
    items["sc_group_topic"] = sc_group_topic
    items["consumer_client_id"] = consumer_client_id

    t = string.Template(template)
    new_content = t.substitute(items)

    gc_conf_path = "/{0}/{1}/conf/init.properties".format(destdir, gc_dirname)
    with open(gc_conf_path, "w") as f:
        f.write(new_content)

####### run
def StartGC(destdir, gc_dirname):
    os.chdir("/{0}/{1}/bin".format(destdir, gc_dirname))
    pid = subprocess.Popen(["./gc_start.sh"]).pid

###### record

# stream_installer.save_service_status(
#     name="gc.py",
#     script="{0}/{1}/bin/gc_stop.sh".format(destdir, gc_dirname),
#     pid=[])
