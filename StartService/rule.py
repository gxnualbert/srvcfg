#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import string
import json







def ModifyRuleConf(ice_addr,zookeeper_servers,instance,destdir, rule_dirname):
    t_config = """
    sqlite.url=$iplib_path
    rule.py.conf = $config_path
    ice.addr=$ice_addr
    zookeeper.servers=$zookeeper_servers
    retry.policy=0
    max.instance.size = 10
    service.parent.node=/fsp/rule.py
    service.instance=$instance
    """

    items = {}

    items["iplib_path"] = "{0}/{1}/conf/iplib.db".format(destdir, rule_dirname)
    items["config_path"] = "{0}/{1}/conf/rule.py-config.xml".format(destdir, rule_dirname)

    items["ice_addr"] = ice_addr
    items["zookeeper_servers"] = zookeeper_servers
    # items["max_instance_size"] = max_instance_size
    items["instance"] = instance

    t = string.Template(t_config)
    new_content = t.substitute(items)

    rule_conf_path = "{0}/{1}/conf/init.properties".format(destdir, rule_dirname)
    with open(rule_conf_path, "w") as f:
        f.write(new_content)

def StartRule(destdir,rule_dirname):

    os.chdir("{0}/{1}/bin".format(destdir, rule_dirname))
    pid = subprocess.Popen(["./rule_start.sh"]).pid

###### record

# stream_installer.save_service_status(
#     name="rule.py",
#     script="{0}/{1}/bin/rule_stop.sh".format(destdir, rule_dirname),
#     pid=[])
