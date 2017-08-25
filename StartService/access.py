#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import errno
import string
import json

def ModifyAccessConf(ice_addr,zookeeper_servers,access_construct_file_path):


    # tomcat_home = "/fsp_sss_stream/apache-tomcat-access"
    # tomcat_bin = "{0}/bin".format(tomcat_home)
    # tomcat_conf = "{0}/conf".format(tomcat_home)
    #
    # ###### install
    # access_home = "{0}/{1}".format(destdir, access_dirname)
    #
    # #绝对路径,后期优化 TODO:white
    # os.chdir(tomcat_conf)
    # subprocess.call(["mv server.xml server.xml.bak"], shell=True)
    # subprocess.call(["cp /fsp_sss_stream/access/server.xml ."], shell=True)

    ###### configure

    template = """
ice.addr=$ice_addr
zookeeper.servers=$zookeeper_servers
retry.policy=0
service.parent.node=/fsp/access
service.instance=access_instance
port=8080
    """

    items = {}
    items["ice_addr"] = ice_addr
    items["zookeeper_servers"] = zookeeper_servers

    t = string.Template(template)
    new_content = t.substitute(items)

    with open(access_construct_file_path + "/init.properties", "w") as f:
        f.write(new_content)

###### run
# 这里的停止tomcat的方式使用 kill由端口查找到线程, 代替运行./shutdown 命令
# access 的http监听端口约定为8080
def StartAccess():
    tomcat_home = "/fsp_sss_stream/apache-tomcat-access"
    tomcat_bin = "{0}/bin".format(tomcat_home)
    os.chdir(tomcat_bin)
    subprocess.call(["netstat -anp|grep 8080|awk '{print $7}'|awk -F'/' '{print $1}'|xargs kill -9"], shell=True)
    subprocess.call(["./startup.sh"])

###### record

