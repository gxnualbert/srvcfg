#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import subprocess
import string


def ModifyGCConf(ice_addr,kafka_brokers,zookeeper_servers,gc_topic,gc_group_topic,sc_group_topic,consumer_client_id,gc_construct_file_path):


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
    items["consumer_client_id"] ="client"+consumer_client_id

    t = string.Template(template)
    new_content = t.substitute(items)

    with open(gc_construct_file_path + "/init.properties", "w") as f:
        f.write(new_content)


if __name__ == "__main__":
    FILE_PATH = "/fsp_sss_stream"
    if os.path.exists(FILE_PATH):
        print "path:%s exits" % FILE_PATH
    else:
        os.makedirs(FILE_PATH)
    subprocess.Popen(["/fsp_sss_stream/fsp-gc-1.0-SNAPSHOT/bin/gc_start.sh"], shell=True)

