#!/usr/bin/python

from __future__ import with_statement

import os
import subprocess
import string




def ModifySSConf(ss_local_ip,ss_instance_id,kafka_brokers,zookeeper_servers,sc_group_topic,ss_construct_file_path):
    template = """
{
    "ip": "$ss_local_ip",
    "instance_id": "$ss_instance_id",
    "kafka_brokers": "$kafka_brokers",
    "zookeeper": "$zookeeper_servers",
    "sc_topic": "$sc_group_topic",
    "app_id": 77,
    "listen_port": 50003
}
        """

    items = {}

    items["ss_local_ip"] = ss_local_ip
    items["ss_instance_id"] = ss_instance_id
    items["kafka_brokers"] = kafka_brokers
    items["zookeeper_servers"] = zookeeper_servers
    items["sc_group_topic"] = sc_group_topic


    t = string.Template(template)
    new_content = t.substitute(items)

    with open(ss_construct_file_path + "/ss.config", "w") as f:
        f.write(new_content)





