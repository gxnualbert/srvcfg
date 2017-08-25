#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: ma_path.py
@time: 2017/08/24/8:38 PM
"""
from StartService import ms, rule,ss,sc,gc,ma,sp,access,gs,cp
from MyUtil import transferfile as tf

import subprocess
import os,ConfigParser


class ReadConf(object):
    def readcf(self):
        cf = ConfigParser.ConfigParser()
        cf.read("setup.conf")
        return cf


class Deploy(object):

    # cf = ConfigParser.ConfigParser()
    # cf.read("setup.conf")
    # s = cf.sections()
    cf=ReadConf().readcf()
    # print cf.get("m1","service")

    #common part
    destdir = "/fsp_sss_stream"
    ice_addr=cf.get("common","ice_addr")
    kafka_brokers = cf.get("common","kafka_brokers")
    zookeeper_servers= cf.get("common","zookeeper_servers")
    sc_group_topic =cf.get("common","sc_group_topic")
    sc_ms_group_topic = cf.get("common","sc_ms_group_topic")
    gc_group_topic=cf.get("common","gc_group_topic")


    #machine info
    host="192.168.7.113"

    port=22
    user="root"
    password="123456"

    remotefile_path=""
    local_file_path=""
    remote_script_path="/usr/"

    # ma part
    ma_topic = "ma_01"
    ma_dirname = "fsp-ma-1.0-SNAPSHOT"
    ma_remote_init_path = destdir + "/" + ma_dirname + "/conf/init.properties"

    #ms part
    ms_topic="ms_topic"
    ms_dirname="fsp-ms-1.0-SNAPSHOT"
    ms_remote_init_path=destdir+"/"+ms_dirname+"/conf/init.properties"

    #rule part
    rule_service_instance="rule_instance"
    rule_dirname="fsp-rule-1.0-SNAPSHOT"
    rule_remote_init_path = destdir + "/" + rule_dirname + "/conf/init.properties"

    #sc part
    sc_topic="sc_instance111"
    sc_consumer_client_id="113"
    sc_dirname="fsp-sc"
    sc_remote_init_path=destdir + "/" + sc_dirname + "/conf/init.properties"

    #gc part
    gc_topic="gc_instance111"
    gc_consumer_client_id="111"
    gc_dirname="fsp-gc-1.0-SNAPSHOT"
    gc_remote_init_path =destdir + "/" + gc_dirname + "/conf/init.properties"

    #sp part
    sp_topic="sp_instance111"
    sp_server_id=sp_topic
    #hard code!!!!
    sp_remote_init_path="/usr/local/apache-tomcat-9.0.0.M17/www/fsp-sp/WEB-INF/classes/init.properties"

    #access part
    access_remote_init_path="/usr/local/apache-tomcat-9.0.0.M17/www/fsp-access/WEB-INF/classes/init.properties"

    #ss part
    # ss_local_ip="192.168.7.111"
    ss_instance_id="ss1"
    ss_dirname="ss"
    ss_remote_init_path=destdir+"/" +ss_dirname+"/ss.config"

    #gs aprt
    gs_instance_id="gs1"
    gs_remote_init_path = destdir + "/gs/gs.config"

    #cp part
    cp_instance_id="cp1"
    cp_remote_init_path= destdir + "/cp/cp.config"





    def create_path(self,FILE_PATH):
        if os.path.exists(FILE_PATH):
            print  "path:%s exits"%FILE_PATH
        else:
            os.makedirs(FILE_PATH)

    def transfer_script_to_machine(self):
        cwd=os.getcwd() + "/StartService/"
        files=os.listdir(cwd)
        filelist=[]
        for a in files:
            if "pyc" not in a and "init" not in a:
                filelist.append(a)
        print filelist

        for i in filelist:
            tf.uploadFile(self.host,self.port,self.user,self.password,cwd+i,self.remote_script_path+i)

    def deploy_ma(self):
        ma_construct_file_path=os.getcwd()+"/ConfigFile/ma"
        self.create_path(ma_construct_file_path)
        #modify init file
        ma.ModifyMSConf(self.ice_addr,self.kafka_brokers,self.zookeeper_servers,self.ma_topic,ma_construct_file_path)
        # upload init file
        tf.uploadFile(self.host,self.port,self.user,self.password,ma_construct_file_path+"/init.properties",self.ma_remote_init_path)
    def deploy_ms(self):
        ms_construct_file_path = os.getcwd() + "/ConfigFile/ms"
        self.create_path(ms_construct_file_path)
        #modify ms init.properties
        ms.ModifyMSConf(self.kafka_brokers,self.zookeeper_servers,self.ice_addr,self.ms_topic,self.sc_ms_group_topic,ms_construct_file_path)
        #upload ms init.properties
        tf.uploadFile(self.host,self.port,self.user,self.password,ms_construct_file_path+"/init.properties",self.ms_remote_init_path)
    def deploy_rule(self):
        rule_construct_file_path = os.getcwd() + "/ConfigFile/rule"
        self.create_path(rule_construct_file_path)
        rule.ModifyRuleConf(self.ice_addr,self.zookeeper_servers,self.rule_service_instance,rule_construct_file_path)
        tf.uploadFile(self.host,self.port,self.user,self.password,rule_construct_file_path+"/init.properties",self.rule_remote_init_path)
    def deploy_sc(self):
        sc_construct_file_path = os.getcwd() + "/ConfigFile/sc"
        self.create_path(sc_construct_file_path)
        sc.ModifySCConf(self.ice_addr,self.kafka_brokers,self.zookeeper_servers,self.sc_topic,self.sc_group_topic,self.sc_consumer_client_id,self.sc_ms_group_topic,sc_construct_file_path)
        tf.uploadFile(self.host,self.port,self.user,self.password,sc_construct_file_path+"/init.properties",self.sc_remote_init_path)
    def deploy_gc(self):
        gc_construct_file_path = os.getcwd() + "/ConfigFile/gc"
        self.create_path(gc_construct_file_path)
        gc.ModifyGCConf(self.ice_addr,self.kafka_brokers,self.zookeeper_servers,self.gc_topic,self.gc_group_topic,self.sc_group_topic,self.gc_consumer_client_id,gc_construct_file_path)
        tf.uploadFile(self.host,self.port,self.user,self.password,gc_construct_file_path+"/init.properties",self.gc_remote_init_path)
    def deploy_sp(self):
        sp_construct_file_path = os.getcwd() + "/ConfigFile/sp"
        self.create_path(sp_construct_file_path)
        sp.ModifySPConf(self.ice_addr,self.kafka_brokers,self.zookeeper_servers,self.sp_topic,self.sc_group_topic,self.gc_group_topic,self.sp_server_id,sp_construct_file_path)
        tf.uploadFile(self.host,self.port,self.user,self.password,sp_construct_file_path+"/init.properties",self.sp_remote_init_path)

    def deploy_access(self):
        access_construct_file_path= os.getcwd() + "/ConfigFile/access"
        self.create_path(access_construct_file_path)
        access.ModifyAccessConf(self.ice_addr,self.zookeeper_servers,access_construct_file_path)
        tf.uploadFile(self.host,self.port,self.user,self.password,access_construct_file_path+"/init.properties",self.access_remote_init_path)
    def deploy_ss(self):
        ss_construct_file_path= os.getcwd() + "/ConfigFile/ss"
        self.create_path(ss_construct_file_path)
        ss.ModifySSConf(self.host,self.ss_instance_id,self.kafka_brokers,self.zookeeper_servers,self.sc_group_topic,ss_construct_file_path)
        tf.uploadFile(self.host,self.port,self.user,self.password,ss_construct_file_path+"/ss.config",self.ss_remote_init_path)
    def deploy_gs(self):
        gs_construct_file_path= os.getcwd() + "/ConfigFile/gs"
        self.create_path(gs_construct_file_path)
        gs.ModifyGSConf(self.host,self.gs_instance_id,self.kafka_brokers,self.zookeeper_servers,self.sc_group_topic,self.gc_group_topic,gs_construct_file_path)
        tf.uploadFile(self.host,self.port,self.user,self.password,gs_construct_file_path+"/gs.config",self.gs_remote_init_path)
    def deploy_cp(self):
        cp_construct_file_path = os.getcwd() + "/ConfigFile/cp"
        self.create_path(cp_construct_file_path)
        cp.ModifySSConf(self.host,self.cp_instance_id,self.kafka_brokers,self.zookeeper_servers,self.sc_group_topic,cp_construct_file_path)
        tf.uploadFile(self.host,self.port,self.user,self.password,cp_construct_file_path+"/cp.config",self.cp_remote_init_path)



if __name__ == "__main__":


    #1 读取配置文件
    rc = ReadConf().readcf()
    mysectionlist=[]
    version = rc.get("common","package_version")
    buildid = rc.get("common","buildid")
    mysections = rc.sections()
    for i in mysections:
        if "common" in i:
            pass
        else:
            mysectionlist.append(i)

    for i in mysectionlist:

        myip = rc.get(i,"ip")
        myservices = rc.get(i,"service")
        #call script to get pkg
        # print os.getcwd()
        # print "/auto.exp ",myip,"123456",version,buildid
        # print os.getcwd()+"/auto.exp "+myip+" 123456 "+version+" "+buildid
        # subprocess.Popen([os.getcwd()+"/auto.exp "+myip+" 123456 "+version+" "+buildid],shell=True).wait()

        myserviceslist=myservices.split(",")
        for k in myserviceslist:
            print "start to install service %s"%k
            subprocess.Popen([os.getcwd() + "/call_install_server.exp " + myip + " 123456 " + version + " " + k],shell=True).wait()

        #start to modify init file


        # subprocess.Popen(["/root/autodeploy/srvcfg/auto.exp 192.168.7.81 123456 2.0.4.10 150"],shell=True).wait()
        # subprocess.Popen(["/root/autodeploy/srvcfg/auto.exp 192.168.7.81 123456 2.0.4.10 150"],shell=True).wait()


        print "finish"


        # myservice = rc.get(i, "service")

        # servicelist=myservice.split(",")

        # for a in servicelist:
        # cd /root/fsp-sss-stream-$version
        #     subprocess.call(["./call_install_server.exp", i, "123456", version, a])










    #遍历配置

    a=Deploy()
    # tf.ssh_cmd(a.host,a.port,"cd /","root","123456")

    # a.deploy_ma()
    # a.transfer_script_to_machine()
    # print  os.getcwd()
    # a.deploy_ms()
    # a.deploy_rule()
    # a.deploy_sc()
    # a.deploy_gc()
    # a.deploy_sp()
    # a.deploy_access()
    # a.deploy_ss()
    # a.deploy_gs()
    # a.deploy_cp()