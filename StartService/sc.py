#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import string
import json


###### install

# destdir = None
# sc_dirname = None

# download_url = sys.argv[3]
# destdir, sc_dirname = stream_installer.do_install("sc.py", url=download_url)
# if (destdir is None) or (sc_dirname is None):
#     sys.exit(2)

###### configure

def ModifySCConf(ice_addr,kafka_brokers,zookeeper_servers,sc_topic,sc_group_topic,consumer_client_id,sc_ms_group,destdir, sc_dirname):


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
    items["consumer_client_id"] = consumer_client_id

    t = string.Template(template)
    new_content = t.substitute(items)

    sc_conf_path = "/{0}/{1}/conf/init.properties".format(destdir, sc_dirname)
    with open(sc_conf_path, "w") as f:
        f.write(new_content)

def StartSC(destdir,sc_dirname):


    os.chdir("/{0}/{1}/bin".format(destdir, sc_dirname))
    pid = subprocess.Popen(["./sc_start.sh"]).pid

# ###### record
#
# stream_installer.save_service_status(
#     name="sc.py",
#     script="{0}/{1}/bin/sc_stop.sh".format(destdir, sc_dirname),
#     pid=[])

