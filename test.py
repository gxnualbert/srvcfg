#!/usr/bin/python

import subprocess

import fsp_smd_pb2 as smd

def test_cp():
    cp_conf = smd.CpConf()
    cp_conf.ice_addr = "databse:default -h 192.168.7.75 -p 10000"
    cp_conf.kafka_brokers = "192.168.7.61:1091;192.168.7.62:1091;192.168.7.63:1091"
    cp_conf.sc_topic = "sc1"
    cp_conf.session_app_id = "88"
    cp_conf.instance_id = "cp1"
    pid = subprocess.Popen(["./cp", cp_conf.SerializeToString(), "192.168.6.130", "http://192.168.5.30:8088/jenkins/view/%E5%B9%B3%E5%8F%B0%E4%BA%A7%E5%93%81%E7%BA%BF/job/build_platform_fsp_stream/lastSuccessfulBuild/artifact/fsp-sss-stream-1.0.0.1.tar.gz"]).pid

def test_ss():
    ss_conf = smd.SsConf()
    ss_conf.ice_addr = "databse:default -h 192.168.7.75 -p 10000"
    ss_conf.instance_id = "ss1"
    ss_conf.kafka_brokers = "192.168.7.61:1091;192.168.7.62:1091;192.168.7.63:1091"
    pid = subprocess.Popen(["./ss", ss_conf.SerializeToString(), "192.168.6.130", ""]).pid

def test_gs():
    gs_conf = smd.GsConf()
    gs_conf.ice_addr = "databse:default -h 192.168.7.75 -p 10000"
    gs_conf.kafka_brokers = "192.168.7.61:1091;192.168.7.62:1091;192.168.7.63:1091"
    gs_conf.sc_topic = "sc_topic"
    gs_conf.gc_topic = "gc_topic"
    gs_conf.instance_id = "gs1"
    gs_conf.group_id = "sc_group_id"
    pid = subprocess.Popen(["./gs", gs_conf.SerializeToString(), "192.168.6.130", ""]).pid

def test_sc():
    sc_conf = smd.ScConf()
    sc_conf.ice_addr = "databse:default -h 192.168.7.75 -p 10000"
    sc_conf.kafka_brokers = "192.168.7.61:1091;192.168.7.62:1091;192.168.7.63:1091"
    sc_conf.zookeeper_servers = "192.168.7.57:1091"
    sc_conf.sc_topic = "sc_topic"
    sc_conf.sc_group_topic = "sc_group"
    sc_conf.consumer_client_id = "test_sc_client"
    pid = subprocess.Popen(["./sc.py", sc_conf.SerializeToString(), "192.168.6.130", ""]).pid

def test_gc():
    gc_conf = smd.GcConf()
    gc_conf.ice_addr = "database:default -h 192.168.7.75 -p 10000"
    gc_conf.kafka_brokers = "192.168.7.61:1091;192.168.7.62:1091;192.168.7.63:1091"
    gc_conf.zookeeper_servers = "192.168.5.57:1091"

    gc_conf.gc_topic = "gc_group_instance_x1"
    gc_conf.gc_group_topic = "gc_group_name1"
    gc_conf.sc_group_topic = "sc_group_name1"
    gc_conf.consumer_client_id = "gc_client_101"

    pid = subprocess.Popen(["./gc.py", gc_conf.SerializeToString(), "192.168.6.130", ""]).pid

def test_ice():
    pid = subprocess.Popen(["./ice", "", "192.168.6.132", ""])

def test_access():
    access_conf = smd.AccessConf()
    access_conf.ice_addr = "databse:default -h 192.168.7.75 -p 10000"
    pid = subprocess.Popen(["./access", access_conf.SerializeToString(), "192.168.6.130", ""]).pid

def test_sp():
    sp_conf = smd.SpConf()
    sp_conf.ice_addr = "database:default -h 192.168.7.75 -p 10000"
    sp_conf.kafka_brokers = "192.168.7.60:9092,192.168.7.61:9092,192.168.7.62:9092"
    sp_conf.zookeeper_servers = "192.168.7.57:2181,192.168.7.58:2181,192.168.7.59:2181"

    sp_conf.sp_topic = "sp111"
    sp_conf.gc_group_topic = "gc_group1"
    sp_conf.sc_group_topic = "sc_group1"
    sp_conf.sp_server_id = "sp1"
    pid = subprocess.Popen(["./sp", sp_conf.SerializeToString(), "192.168.6.130", ""]).pid

def test_stream_as():
    sas_conf = smd.StreamAsConf()
    sas_conf.access_url = "http://192.168.7.165:8080"
    sas_conf.session_app_id = "2"
    pid = subprocess.Popen(["./stream_as", sas_conf.SerializeToString(), "192.168.6.132", ""]).pid

def test_group_as():
    gas_conf = smd.GroupAsConf()
    gas_conf.access_url = "http://192.168.7.165:8080"
    gas_conf.ice_addr = "databse:default -h 192.168.7.75 -p 10000"
    gas_conf.dev_id = "1"
    gas_conf.dev_verify_code = "1234"
    gas_conf.app_id = "1"
    gas_conf.verification_code = "xxxxxx"
    pid = subprocess.Popen(["./group_as", gas_conf.SerializeToString(), "192.168.6.130", ""]).pid

def test_ma():
    ma_conf = smd.MaConf()
    ma_conf.ice_addr = "databse:default -h 192.168.7.75 -p 10000"
    ma_conf.kafka_brokers = "192.168.7.60:9092,192.168.7.61:9092,192.168.7.62:9092"
    ma_conf.zookeeper_servers = "192.168.7.57:2181,192.168.7.58:2181,192.168.7.59:2181"
    ma_conf.ma_topic = "ma1"
    ma_conf.bandwidth = "1000"
    subprocess.call(["./ma", ma_conf.SerializeToString(), "192.168.6.130", ""])

def test_ms():
    ms_conf = smd.MsConf()
    ms_conf.ice_addr = "database:default -h 192.168.7.75 -p 10000"
    ms_conf.kafka_brokers = "192.168.7.60:9092,192.168.7.61:9092,192.168.7.62:9092"
    ms_conf.zookeeper_servers = "192.168.7.57:2181,192.168.7.58:2181,192.168.7.59:2181"
    ms_conf.ms_topic = "ms1"
    ms_conf.poll_time = "30"
    subprocess.call(["./ms", ms_conf.SerializeToString(), "192.168.6.130", ""])

def test_rule():
    rule_conf = smd.RuleConf()
    rule_conf.ice_addr = "database:default -h 192.168.7.75 -p 10000"
    rule_conf.zookeeper_servers = "192.168.7.57:2181,192.168.7.58:2181,192.168.7.59:2181"
    rule_conf.max_instance_size = "10"
    subprocess.call(["./rule.py", rule_conf.SerializeToString(), "192.168.6.130", ""])

services = {
    "ice": test_ice,
    "access": test_access,
    "cp": test_cp,
    "sp": test_sp,
    "ss": test_ss,
    "sc.py": test_sc,
    "gs": test_gs,
    "gc.py": test_gc,
    "ma": test_ma,
    "ms": test_ms,
    "rule.py": test_rule,
    "stream_as": test_stream_as,
    "group_as": test_group_as
}

while True:
    try:
        choice = raw_input("{0}: ".format(services.keys()))
    except KeyboardInterrupt:
        print "You press C-c, quit"
        break
    else:
        if choice in services.keys():
            action = services[choice]
            if action: action()
