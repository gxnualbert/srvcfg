#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import string
import random
import json

import stream_installer

###### install

def ModifyGSConf(gs_local_ip, gs_instance_id, kafka_brokers, zookeeper_servers, sc_group_topic, gc_group_topic,destdir, ss_dirname):
    template = """
        {
            "ip":$gs_local_ip,
            "instance_id":$gs_instance_id,
            "kafka_brokers":$kafka_brokers,
            "zookeeper":$zookeeper_servers,
            "sc_topic":$sc_group_topic,
            "gc_topic":$gc_group_topic,
            "app_id":1,
            "listen_port":50002
        }
        """

    items = {}

    items["gs_local_ip"] = gs_local_ip
    items["gs_instance_id"] = gs_instance_id
    items["kafka_brokers"] = kafka_brokers
    items["zookeeper_servers"] = zookeeper_servers
    items["sc_group_topic"] = sc_group_topic
    items["gc_group_topic"] = gc_group_topic

    t = string.Template(template)
    new_content = t.substitute(items)

    sc_conf_path = "/{0}/{1}/gs.config".format(destdir, ss_dirname)
    with open(sc_conf_path, "w") as f:
        f.write(new_content)


def StartGS(destdir, ss_dirname):
    os.chdir("/{0}/{1}".format(destdir, ss_dirname))
    pid = subprocess.Popen(["./test_group_server < gs.config"]).pid


# pid = subprocess.Popen(["./service"]).pid

###### record

# stream_installer.save_service_status(name="gs", script="", pid=[pid])
