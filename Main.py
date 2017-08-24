import sc
import ss

from StartService import ms, rule


class Deploy(object):

    #common part
    destdir = "/fsp_sss_stream"

    ice_addr="DBIceGrid/Locator:default -h 192.168.7.84 -p 10000:default -h 192.168.7.85 -p 10001"
    kafka_brokers = "192.168.7.84:9092,192.168.7.85:9092,192.168.7.86:9092"
    zookeeper_servers= "192.168.7.84:2181,192.168.7.85:2181,192.168.7.86:2181"
    sc_ms_topic = "sc_ms_group"
    sc_group_topic = "sc_group2"
    sc_ms_group = "sc_ms_group"

    #ms part
    ms_topic="ms_topic"
    ms_dirname = "fsp-ms-1.0-SNAPSHOT"

    #rule part
    rule_service_instance="rule_instance"
    rule_dirname="fsp-rule-1.0-SNAPSHOT"

    #sc part
    sc_topic="sc_instance111"
    sc_consumer_client_id=""



    #ss part
    ss_local_ip="192.168.7.111"
    ss_instance_id="ss1"
    ss_dirname="ss"




    def deploy_ms(self):
        ms.ModifyMSConf(self.kafka_brokers, self.zookeeper_servers, self.ice_addr, self.ms_topic, self.sc_ms_topic, self.destdir, self.ms_dirname)
        ms.StartMS(self.destdir, self.ms_dirname)

    def deploy_rule(self):
        rule.ModifyRuleConf(self.ice_addr, self.zookeeper_servers, self.rule_service_instance, self.destdir, self.rule_dirname)
        rule.StartRule(self.destdir, self.rule_dirname)

    def deploy_sc(self):
        sc.ModifySCConf(self.ice_addr, self.kafka_brokers, self.zookeeper_servers, self.sc_topic, self.sc_group_topic, self.sc_consumer_client_id, self.sc_ms_group, self.destdir, self.ms_dirname)
        sc.StartSC(self.destdir, self.ms_dirname)

    def deploy_ss(self):
        ss.ModifySSConf(self.ss_local_ip, self.ss_instance_id, self.kafka_brokers, self.zookeeper_servers, self.sc_group_topic, self.destdir, self.ss_dirname)
        ss.StartSS(self.destdir, self.ss_dirname)








if __name__ == "__main__":
    print("Hello python !!!")


    def func_print():
        print("in func_print")


    def main():
        print("In main")


    main()