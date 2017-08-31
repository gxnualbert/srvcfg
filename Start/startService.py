#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: ma.py
@time: 2017/08/27/10:57 AM
"""
import subprocess,os,sys

class startService(object):

    ###### run
    # 这里的停止tomcat的方式使用 kill由端口查找到线程, 代替运行./shutdown 命令
    # access 的http监听端口约定为8080
    def access(self):
        tomcat_home = "/fsp_sss_stream/apache-tomcat-access"
        tomcat_bin = "{0}/bin".format(tomcat_home)
        os.chdir(tomcat_bin)
        subprocess.call(["netstat -anp|grep 8080|awk '{print $7}'|awk -F'/' '{print $1}'|xargs kill -9"], shell=True)
        subprocess.call(["./startup.sh"])
    ###### run
    # 这里的停止tomcat的方式使用 kill由端口查找到线程, 代替运行./shutdown 命令
    # sp 的http2 端口约定为 8444
    def sp(self):
        tomcat_home = "/fsp_sss_stream/apache-tomcat-sp"
        tomcat_bin = "{0}/bin".format(tomcat_home)
        os.chdir(tomcat_bin)
        subprocess.call(["netstat -anp|grep 8444|awk '{print $7}'|awk -F'/' '{print $1}'|xargs kill -9"], shell=True)
        subprocess.call(["./startup.sh"])


    def gc(self):
        subprocess.Popen(["/fsp_sss_stream/gc/bin/gc_start.sh"], shell=True).wait(300)
    def ma(self):
        subprocess.Popen(["/fsp_sss_stream/ma/bin/ma_start.sh"], shell=True)

    def ms(self):
        subprocess.Popen(["/fsp_sss_stream/fsp-ms-1.0-SNAPSHOT/bin/ms_start.sh"], shell=True)

    def rule(self):
        subprocess.Popen(["/fsp_sss_stream/rule/bin/rule_start.sh"], shell=True)

    def sc(self):
        subprocess.Popen(["/fsp_sss_stream/sc/bin/sc_start.sh"], shell=True)
    def ss(self):
        subprocess.Popen(["/fsp_sss_stream/ss/test_stream_server_ss < ss.config"],shell=True)

    def cp(self):
        subprocess.Popen(["/fsp_sss_stream/cp/test_group_server < cp.config"],shell=True)

    def gs(self):
        subprocess.Popen(["/fsp_sss_stream/gs/test_group_server < gs.config"],shell=True)

if __name__ == "__main__":
    serviceName=sys.argv[2]
    start=startService()
    # support_service_list = ["access", "sp", "sc", "gc", "ma", "ms", "rule", "gs", "ss", "cp"]
    if serviceName=="access":
        start.access()
    elif serviceName=="sp":
        start.sp()
    elif serviceName=="sc":
        start.sc()
    elif serviceName=="gc":
        start.gc()
    elif serviceName=="ma":
        start.ma()
    elif serviceName=="ms":
        start.ms()
    elif serviceName=="rule":
        start.rule()
    elif serviceName=="gs":
        start.gs()
    elif serviceName=="ss":
        start.ss()
    elif serviceName=="cp":
        start.cp()
