#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os

import subprocess
import string



def ModifySCConf(ice_addr,kafka_brokers,zookeeper_servers,sc_topic,sc_group_topic,consumer_client_id,sc_ms_group,sc_construct_file_path):


    template = """
application.name=sc
bootstrap.servers=$kafka_brokers
zookeeper.servers=$zookeeper_servers
retry.policy=0
ice.addr=$ice_addr
topic.partions=3
topic.replication=2
topic.sc.name = $sc_topic
topic.sc.group.name = $sc_group_topic
topic.sc.group1.name=$sc_ms_group
consumer.client.id=$consumer_client_id

message.protocol.version = 1
max.instance.size = 5
routerStatus.return.size = 5

lock.root.path = /sclock
lock.getSuperiorStreamServer.timeout=5
service.parent.node=/fsp/sc
    """

    items = {}

    items["ice_addr"] = ice_addr
    items["kafka_brokers"] = kafka_brokers
    items["zookeeper_servers"] = zookeeper_servers
    items["sc_topic"] = sc_topic
    items["sc_group_topic"] = sc_group_topic
    items["sc_ms_group"] = sc_ms_group
    items["consumer_client_id"] = "client"+consumer_client_id

    t = string.Template(template)
    new_content = t.substitute(items)


    with open(sc_construct_file_path + "/init.properties", "w") as f:
        f.write(new_content)






