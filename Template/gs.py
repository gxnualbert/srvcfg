#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import subprocess
import string


def ModifyGSConf(gs_local_ip, gs_instance_id, kafka_brokers, zookeeper_servers, sc_group_topic, gc_group_topic,gs_construct_file_path):
    template = """
{
    "ip":"$gs_local_ip",
    "instance_id":"$gs_instance_id",
    "kafka_brokers":"$kafka_brokers",
    "zookeeper":"$zookeeper_servers",
    "sc_topic":"$sc_group_topic",
    "gc_topic":"$gc_group_topic",
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

    with open(gs_construct_file_path + "/gs.config", "w") as f:
        f.write(new_content)




