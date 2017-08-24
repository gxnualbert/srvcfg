#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
import subprocess
import errno
import string
import json

def ModifyAccessConf():

    conf = json.loads(sys.argv[1])

    tomcat_home = "/fsp_sss_stream/apache-tomcat-access"
    tomcat_bin = "{0}/bin".format(tomcat_home)
    tomcat_conf = "{0}/conf".format(tomcat_home)

    ###### install

    destdir = None
    access_dirname = None

    access_home = "{0}/{1}".format(destdir, access_dirname)

    #绝对路径,后期优化 TODO:white
    os.chdir(tomcat_conf)
    subprocess.call(["mv server.xml server.xml.bak"], shell=True)
    subprocess.call(["cp /fsp_sss_stream/access/server.xml ."], shell=True)

    ###### configure

    template = """
    ice.addr=$ice_addr
    zookeeper.servers=$zookeeper
    retry.policy=$retry_policy
    service.parent.node=/fsp/access
    service.instance=$instance
    port=8080
    """

    items = {}
    items["ice_addr"] = conf["ice_addr"]
    items["zookeeper"] = conf["zookeeper"]
    items["retry_policy"] = conf["retry_policy"]
    items["instance"] = conf["instance"]

    t = string.Template(template)
    new_content = t.substitute(items)

    access_conf_path = "{0}/WEB-INF/classes/init.properties".format(access_home)
    with open(access_conf_path, "w") as f:
        f.write(new_content)

###### run
# 这里的停止tomcat的方式使用 kill由端口查找到线程, 代替运行./shutdown 命令
# access 的http监听端口约定为8080
os.chdir(tomcat_bin)
subprocess.call(["netstat -anp|grep 8080|awk '{print $7}'|awk -F'/' '{print $1}'|xargs kill -9"], shell=True)
subprocess.call(["./startup.sh"])

###### record

