#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen

@time: 2017/08/24/8:38 AM
"""

from Template import ms, rule,ss,sc,gc,ma,sp,access,gs,cp
from MyUtil import transferfile as tf

import subprocess
import os,ConfigParser
import time, datetime,shutil


class ReadConf(object):
    def readcf(self):
        cf = ConfigParser.ConfigParser()
        cf.read("setup.conf")
        return cf


class Get_time():
    def get_time(self):
        aa = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return aa.replace("-", "_")


class Deploy(object):

    cf=ReadConf().readcf()
    #common part
    destdir = "/fsp_sss_stream"

    ice_addr=cf.get("common","ice_addr")
    kafka_brokers = cf.get("common","kafka_brokers")
    zookeeper_servers= cf.get("common","zookeeper_servers")

    time_suffix = Get_time().get_time()

    sc_group_topic ="sc_group_"+time_suffix
    sc_ms_group_topic = "sc_ms_group_"+time_suffix
    gc_group_topic="gc_group_"+time_suffix


    #machine info
    port=22
    user="root"
    password="123456"
    cureen_path=os.getcwd()
    conf="ConfigFile"
    init="init.properties"

    remote_script_path="/usr/"

    sp_remote_init_path = "/fsp_sss_stream/sp/WEB-INF/classes/init.properties"
    access_remote_init_path = "/fsp_sss_stream/access/WEB-INF/classes/init.properties"
    ma_remote_init_path = destdir + "/ma/conf/init.properties"
    ms_remote_init_path=destdir+"/ms/conf/init.properties"
    rule_remote_init_path = destdir + "/rule/conf/init.properties"
    sc_remote_init_path=destdir + "/sc/conf/init.properties"
    gc_remote_init_path =destdir + "/gc/conf/init.properties"
    ss_remote_init_path= destdir+"/ss/ss.config"
    gs_remote_init_path = destdir+"/gs/gs.config"
    cp_remote_init_path= destdir + "/cp/cp.config"

    def get_host_suffix(self,host):
        return host.split(".")[-1]


    def create_path(self,FILE_PATH):
        if os.path.exists(FILE_PATH):
            pass
        else:
            os.makedirs(FILE_PATH)

    def combine_path(self,path,*paths):

        return os.path.join(path,*paths)

    # def transfer_script_to_machine(self,host):
    #     cwd=os.getcwd() + "/StartService/"
    #     files=os.listdir(cwd)
    #     filelist=[]
    #     for a in files:
    #         if "pyc" not in a and "init" not in a:
    #             filelist.append(a)
    #     print filelist
    #
    #     for i in filelist:
    #         tf.uploadFile(host,self.port,self.user,self.password,cwd+i,self.remote_script_path+i)

    def deploy_ma(self,host):
        ma_topic="ma_"+self.get_host_suffix(host)+"_"+self.time_suffix
        # ma_construct_file_path=os.getcwd()+"/ConfigFile/ma"
        ma_construct_file_path=self.combine_path(self.cureen_path,self.conf,"ma")
        self.create_path(ma_construct_file_path)
        ma.ModifyMAConf(self.ice_addr,self.kafka_brokers,self.zookeeper_servers,ma_topic,ma_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(ma_construct_file_path,self.init),self.ma_remote_init_path)
        # tf.uploadFile(host,self.port,self.user,self.password,ma_construct_file_path+"/init.properties",self.ma_remote_init_path)
        print "modify ma configure file, Done"
        maInfo=["ma instance: "+ma_topic]

    def deploy_ms(self,host):
        ms_topic="ms_"+self.get_host_suffix(host)+"_"+self.time_suffix
        ms_construct_file_path = self.combine_path(self.cureen_path,self.conf,"ms")
        # ms_construct_file_path = os.getcwd() + "/ConfigFile/ms"
        self.create_path(ms_construct_file_path)
        ms.ModifyMSConf(self.kafka_brokers,self.zookeeper_servers,self.ice_addr,ms_topic,self.sc_ms_group_topic,ms_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(ms_construct_file_path,self.init),self.ms_remote_init_path)
        # tf.uploadFile(host,self.port,self.user,self.password,ms_construct_file_path+"/init.properties",self.ms_remote_init_path)
        print "modify ms configure file, Done"

    def deploy_rule(self,host):
        rule_service_instance="rule_"+self.get_host_suffix(host)+"_"+self.time_suffix
        rule_construct_file_path = self.combine_path(self.cureen_path,self.conf,"rule")
        # rule_construct_file_path = os.getcwd() + "/ConfigFile/rule"
        self.create_path(rule_construct_file_path)
        rule.ModifyRuleConf(self.ice_addr,self.zookeeper_servers,rule_service_instance,rule_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(rule_construct_file_path,self.init),self.rule_remote_init_path)
        # tf.uploadFile(host,self.port,self.user,self.password,rule_construct_file_path+"/init.properties",self.rule_remote_init_path)
        print "modify rule configure file, Done"

    def deploy_sc(self,host):

        sc_topic="sc_"+self.get_host_suffix(host)+"_"+self.time_suffix
        sc_consumer_client_id=self.get_host_suffix(host)
        sc_construct_file_path = self.combine_path(self.cureen_path,self.conf,"sc")
        # sc_construct_file_path = os.getcwd() + "/ConfigFile/sc"
        self.create_path(sc_construct_file_path)
        sc.ModifySCConf(self.ice_addr,self.kafka_brokers,self.zookeeper_servers,sc_topic,self.sc_group_topic,sc_consumer_client_id,self.sc_ms_group_topic,sc_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(sc_construct_file_path,self.init),self.sc_remote_init_path)
        # tf.uploadFile(host,self.port,self.user,self.password,sc_construct_file_path+"/init.properties",self.sc_remote_init_path)
        print "modify sc configure file, Done"

    def deploy_gc(self,host):
        gc_topic="gc_"+self.get_host_suffix(host)+"_"+self.time_suffix
        gc_consumer_client_id = self.get_host_suffix(host)
        gc_construct_file_path = self.combine_path(self.cureen_path,self.conf,"gc")
        # gc_construct_file_path = os.getcwd() + "/ConfigFile/gc"
        self.create_path(gc_construct_file_path)
        gc.ModifyGCConf(self.ice_addr,self.kafka_brokers,self.zookeeper_servers,gc_topic,self.gc_group_topic,self.sc_group_topic,gc_consumer_client_id,gc_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(gc_construct_file_path,self.init),self.gc_remote_init_path)
        # tf.uploadFile(host,self.port,self.user,self.password,gc_construct_file_path+"/init.properties",self.gc_remote_init_path)
        print "modify gc configure file, Done"


    def deploy_sp(self,host):

        sp_topic="sp_"+self.get_host_suffix(host)+"_"+self.time_suffix
        sp_server_id=sp_topic
        sp_construct_file_path = self.combine_path(self.cureen_path,self.conf,"sp")
        # sp_construct_file_path = os.getcwd() + "/ConfigFile/sp"
        self.create_path(sp_construct_file_path)
        sp.ModifySPConf(self.ice_addr, self.kafka_brokers, self.zookeeper_servers, sp_topic,self.sc_group_topic,self.gc_group_topic, sp_server_id,sp_construct_file_path)
        tf.uploadFile(host, self.port, self.user, self.password, self.combine_path(sp_construct_file_path,self.init), self.sp_remote_init_path)
        # tf.uploadFile(host, self.port, self.user, self.password, sp_construct_file_path+"/init.properties", self.sp_remote_init_path)
        print "modify sp configure file, Done"

    def deploy_access(self,host):
        access_instance="access_"+self.get_host_suffix(host)+"_"+self.time_suffix
        access_construct_file_path= self.combine_path(self.cureen_path,self.conf,"access")
        # access_construct_file_path= os.getcwd() + "/ConfigFile/access"
        self.create_path(access_construct_file_path)
        access.ModifyAccessConf(self.ice_addr,self.zookeeper_servers,access_instance,access_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(access_construct_file_path,self.init),self.access_remote_init_path)
        print "modify access configure file, Done"

        # tf.uploadFile(host,self.port,self.user,self.password,access_construct_file_path+"/init.properties",self.access_remote_init_path)

    def deploy_ss(self,host):

        ss_instance_id = "ss_"+self.get_host_suffix(host)+"_"+self.time_suffix
        ss_construct_file_path= self.combine_path(self.cureen_path,self.conf,"ss")
        # ss_construct_file_path= os.getcwd() + "/ConfigFile/ss"
        self.create_path(ss_construct_file_path)
        ss.ModifySSConf(host,ss_instance_id, self.kafka_brokers,self.zookeeper_servers,self.sc_group_topic,ss_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(ss_construct_file_path,"ss.config"),self.ss_remote_init_path)
        # tf.uploadFile(host,self.port,self.user,self.password,ss_construct_file_path+"/ss.config",self.ss_remote_init_path)
        print "modify ss configure file, Done"

    def deploy_gs(self,host):
        gs_instance_id="gs_"+self.get_host_suffix(host)+"_"+self.time_suffix
        gs_construct_file_path= self.combine_path(self.cureen_path,self.conf,"gs")
        # gs_construct_file_path= os.getcwd() + "/ConfigFile/gs"
        self.create_path(gs_construct_file_path)
        gs.ModifyGSConf(host,gs_instance_id,self.kafka_brokers,self.zookeeper_servers,self.sc_group_topic,self.gc_group_topic,gs_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(gs_construct_file_path,"gs.config"),self.gs_remote_init_path)
        # tf.uploadFile(host,self.port,self.user,self.password,gs_construct_file_path+"/gs.config",self.gs_remote_init_path)
        print "modify gs configure file, Done"
    def deploy_cp(self,host):
        cp_instance_id="cp_"+self.get_host_suffix(host)+"_"+self.time_suffix
        cp_construct_file_path = self.combine_path(self.cureen_path,self.conf,"cp")
        # cp_construct_file_path = os.getcwd() + "/ConfigFile/cp"
        self.create_path(cp_construct_file_path)
        cp.ModifyCPConf(host,cp_instance_id,self.kafka_brokers,self.zookeeper_servers,self.sc_group_topic,cp_construct_file_path)
        tf.uploadFile(host,self.port,self.user,self.password,self.combine_path(cp_construct_file_path,"cp.config"),self.cp_remote_init_path)
        # tf.uploadFile(host,self.port,self.user,self.password,cp_construct_file_path+"/cp.config",self.cp_remote_init_path)
        print "modify cp configure file, Done"
    def remove_folder(self,FILE_PATH):
        shutil.rmtree(FILE_PATH)



if __name__ == "__main__":

    #1 读取配置文件
    starttime = datetime.datetime.now()
    print "\n",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"\n"
    support_service_list = ["access", "sp", "sc", "gc", "ma", "ms", "rule", "gs", "ss", "cp"]
    rc = ReadConf().readcf()
    mysectionlist=[]
    version = rc.get("common","package_version")
    buildid = rc.get("common","buildid")
    mysections = rc.sections()
    DeployObj = Deploy()
    for i in mysections:
        if "common" in i:
            pass
        else:
            mysectionlist.append(i)
    for i in mysectionlist:
        myip = rc.get(i,"ip")
        myservices = rc.get(i,"service")
        tf.uploadFile(myip,22,"root","123456",os.path.join("MyUtil","startService.sh"),"/tmp/startService.sh")
        subprocess.Popen([os.getcwd()+"/MyUtil/auto.exp "+myip+" 123456 "+version+" "+buildid],shell=True).wait()


        myserviceslist=myservices.split(",")
        for k in myserviceslist:
            print "\n","%s installing..."%k
            subprocess.Popen([os.getcwd() + "/MyUtil/call_install_server.exp " + myip + " 123456 " + version + " " + k],shell=True).wait()
            if k in support_service_list:
                if k =="access":
                    DeployObj.deploy_access(myip)
                if k == "sp":
                    DeployObj.deploy_sp(myip)
                if k == "sc":
                    DeployObj.deploy_sc(myip)
                if k == "gc":
                    DeployObj.deploy_gc(myip)
                if k == "ma":
                    DeployObj.deploy_ma(myip)
                if k == "ms":
                    DeployObj.deploy_ms(myip)
                if k == "rule":
                    DeployObj.deploy_rule(myip)
                if k == "gs":
                    DeployObj.deploy_gs(myip)
                if k == "ss":
                    DeployObj.deploy_ss(myip)
                if k == "cp":
                    DeployObj.deploy_cp(myip)
            else:
                print "service %s is not supported!!!!!"%k
            #start service
            subprocess.Popen([os.getcwd() + "/MyUtil/startService.exp " + myip + " 123456 " + k ],shell=True).wait()
            print "start %s , Done"%k


    # DeployObj.remove_folder(os.path.join(os.getcwd(),"ConfigFile"))
    endtime = datetime.datetime.now()
    total = (endtime - starttime).seconds
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    print "Spend time: %ss" % total





