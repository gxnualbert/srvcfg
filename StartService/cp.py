#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os,string
import subprocess


#由于CP没有配置文件，所以直接启动CP。

def ModifySSConf(cp_local_ip,cp_instance_id,kafka_brokers,zookeeper_servers,sc_group_topic,cp_construct_file_path):
    template = """
{
    "ip": "$cp_local_ip",
    "instance_id": "$cp_instance_id",
    "kafka_brokers": "$kafka_brokers",
    "zookeeper": "$zookeeper_servers",
    "sc_topic": "$sc_group_topic",
    "app_id": 88,
    "listen_port": 50001
}
        """

    items = {}

    items["cp_local_ip"] = cp_local_ip
    items["cp_instance_id"] = cp_instance_id
    items["kafka_brokers"] = kafka_brokers
    items["zookeeper_servers"] = zookeeper_servers
    items["sc_group_topic"] = sc_group_topic


    t = string.Template(template)
    new_content = t.substitute(items)

    with open(cp_construct_file_path + "/cp.config", "w") as f:
        f.write(new_content)


def StartCP(cp_ip,cp_port,ice_addr,session_app_id,instance_id,sc_group_topic,kafka_brokers,zookeeper_servers,destdir,cp_dirname):
    os.chdir("/{0}/{1}".format(destdir, cp_dirname))
    pid = subprocess.Popen(["./test_proxy",
                            cp_ip, cp_port,
                            ice_addr,
                            session_app_id, instance_id,
                            sc_group_topic, kafka_brokers,
                            zookeeper_servers]).pid
