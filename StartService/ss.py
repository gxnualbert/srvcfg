#!/usr/bin/python

from __future__ import with_statement

import os
import subprocess
import string


###### configure

def ModifySSConf(ss_local_ip,ss_instance_id,kafka_brokers,zookeeper_servers,sc_group_topic,destdir, ss_dirname):
    template = """
        {
            "ip": $ss_local_ip,
            "instance_id": $ss_instance_id,
            "kafka_brokers": $kafka_brokers,
            "zookeeper": $zookeeper_servers,
            "sc_topic": $sc_group_topic,
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

    sc_conf_path = "/{0}/{1}/ss.config".format(destdir, ss_dirname)
    with open(sc_conf_path, "w") as f:
        f.write(new_content)
def StartSS(destdir, ss_dirname):
    os.chdir("/{0}/{1}".format(destdir, ss_dirname))
    pid = subprocess.Popen(["./test_stream_server_ss < ss.config"]).pid

###### record

# stream_installer.save_service_status(name="ss", script="", pid=[pid])
