#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os

import subprocess
import string


def ModifyRuleConf(ice_addr,zookeeper_servers,rule_instance,rule_construct_file_path):
    t_config = """
sqlite.url=$iplib_path
rule.conf = $config_path
ice.addr=$ice_addr
zookeeper.servers=$zookeeper_servers
retry.policy=0
max.instance.size =10
service.parent.node=/fsp/rule
service.instance=$instance
    """

    items = {}

    items["iplib_path"] = "/fsp_sss_stream/rule/conf/iplib.db"
    # items["iplib_path"] = "{0}/{1}/conf/iplib.db".format(destdir, rule_dirname)
    items["config_path"] = "/fsp_sss_stream/rule/conf/rule-config.xml"
    # items["config_path"] = "{0}/{1}/conf/rule.py-config.xml".format(destdir, rule_dirname)

    items["ice_addr"] = ice_addr
    items["zookeeper_servers"] = zookeeper_servers
    items["instance"] = rule_instance

    t = string.Template(t_config)
    new_content = t.substitute(items)

    # rule_conf_path = "{0}/{1}/conf/init.properties".format(destdir, rule_dirname)
    # with open(rule_conf_path, "w") as f:
    #     f.write(new_content)
    with open(rule_construct_file_path + "/init.properties", "w") as f:
        f.write(new_content)




