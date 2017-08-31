#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import errno
import string
import json

def ModifyAccessConf(ice_addr,zookeeper_servers,access_instance,access_construct_file_path):


    # tomcat_home = "/fsp_sss_stream/apache-tomcat-access"
    # tomcat_bin = "{0}/bin".format(tomcat_home)
    # tomcat_conf = "{0}/conf".format(tomcat_home)
    #
    # ###### install
    # access_home = "{0}/{1}".format(destdir, access_dirname)
    #
    # #绝对路径,后期优化
    # os.chdir(tomcat_conf)
    # subprocess.call(["mv server.xml server.xml.bak"], shell=True)
    # subprocess.call(["cp /fsp_sss_stream/access/server.xml ."], shell=True)

    ###### configure

    template = """
ice.addr=$ice_addr
zookeeper.servers=$zookeeper_servers
retry.policy=0
service.parent.node=/fsp/access
service.instance=$access_instance
port=8080
    """

    items = {}
    items["ice_addr"] = ice_addr
    items["zookeeper_servers"] = zookeeper_servers
    items["access_instance"] = access_instance



    t = string.Template(template)
    new_content = t.substitute(items)

    with open(access_construct_file_path + "/init.properties", "w") as f:
        f.write(new_content)









