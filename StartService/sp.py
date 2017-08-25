#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os

import subprocess
import string



def ModifySPConf(ice_addr,kafka_brokers,zookeeper_servers,sp_topic,sc_group_topic,gc_group_topic,sp_server_id,sp_construct_file_path):
    # tomcat_home = "/fsp_sss_stream/apache-tomcat-sp"
    # tomcat_conf = "{0}/conf".format(tomcat_home)
    # sp_home = "{0}/{1}".format(destdir, sp_dirname)
    #
    #
    # os.chdir(tomcat_conf)
    # subprocess.call(["mv server.xml server.xml.bak"], shell=True)
    # subprocess.call(["cp /fsp_sss_stream/sp/server.xml ."], shell=True)

    ###### configure

    #目前sp的实例名称设置为sp的topic.

    template = """
bootstrap.servers=$kafka_brokers
zookeeper.servers=$zookeeper_servers
retry.policy=0
ice.addr=$ice_addr
topic.partions=3
topic.replication=2
topic.sp.name = $sp_topic
topic.sc.group.name = $sc_group_topic
topic.gc.group.name = $gc_group_topic

sp.server.id = $sp_server_id
sp.port = $port

message.protocol.version = 1
service.parent.node=/fsp/sp
    """

    items = {}
    items["ice_addr"] = ice_addr
    items["kafka_brokers"] = kafka_brokers
    items["zookeeper_servers"] = zookeeper_servers

    items["sp_topic"] = sp_topic
    items["sc_group_topic"] = sc_group_topic
    items["gc_group_topic"] = gc_group_topic

    items["sp_server_id"] = sp_server_id
    items["port"] = "8444"

    t = string.Template(template)
    new_content = t.substitute(items)

    # sp_conf_path = "{0}/WEB-INF/classes/init.properties".format(sp_home)
    # with open(sp_conf_path, "w") as f:
    #     f.write(new_content)
    with open(sp_construct_file_path + "/init.properties", "w") as f:
        f.write(new_content)

###### run
# 这里的停止tomcat的方式使用 kill由端口查找到线程, 代替运行./shutdown 命令
# sp 的http2 端口约定为 8444

def StartSP(tomcat_home,destdir,sc_dirname):
    tomcat_home = "/fsp_sss_stream/apache-tomcat-sp"
    tomcat_bin = "{0}/bin".format(tomcat_home)
    os.chdir(tomcat_bin)
    subprocess.call(["netstat -anp|grep 8444|awk '{print $7}'|awk -F'/' '{print $1}'|xargs kill -9"], shell=True)
    subprocess.call(["./startup.sh"])



