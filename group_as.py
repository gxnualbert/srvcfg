#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import subprocess
import string
import random
import json

import stream_installer

###### install

nowdir = os.getcwd()
destdir = (os.path.split(nowdir))[0]
dir = "{0}/group_as".format(destdir)

subprocess.call(["curl", "-C", "-", "ftp://192.168.7.144/pub/as.tar.gz", "-o", "/tmp/as.tar.gz"])

# 删除之前的as
subprocess.call(["rm", "-rf", dir])
subprocess.call(["mkdir", dir])
subprocess.call(["tar", "xf", "/tmp/as.tar.gz", "-C", dir, "--strip-components", "1"])
# subprocess.call(["tar", "xf", "{0}/as.tar.gz".format(destdir), "-C", destdir])

###### configure

conf = json.loads(sys.argv[1])

template1 = """
<?xml version="1.0" encoding="UTF-8" ?>
<Root>
    <NATIPList>
        <NATIP />
    </NATIPList>

    <LogSaveDays>15</LogSaveDays>
    <DBProxy>
        <DBSrvAppID>32</DBSrvAppID>
        <DBServer>TCP:127.0.0.1:1088;</DBServer>
        <DBPort>1088</DBPort>
        <DBName>fsboss</DBName>
        <DBUser>test</DBUser>
        <DBPassword>test</DBPassword>
    </DBProxy>
    <ICEServer>
        <DBServer>$ice_ip</DBServer>
        <DBPort>$ice_port</DBPort>
    </ICEServer>
    <!--ICEServer>
        <DBServer>192.168.5.56</DBServer>
        <DBPort>10001</DBPort>
    </ICEServer-->

    <DBAccessType>3</DBAccessType>
    <FrontService>
        <AppID>20</AppID>
        <AddrLink>TCP:127.0.0.1:$listen_port</AddrLink>
    </FrontService>
    <Dev>
        <DevID>$dev_id</DevID>
        <VerifyCode>$dev_verify_code</VerifyCode>
        <DevType>1</DevType>
    </Dev>
    <ProcessList>
        <ServiceProcess>
            <ProcessName>FM_Server</ProcessName>
            <ListenList>
                <Listen>
                    <Addr>0</Addr>
                    <Protocol>TCP</Protocol>
                    <Port>$listen_port</Port>
                </Listen>
                <Listen>
                    <Addr>0</Addr>
                    <Protocol>UDP</Protocol>
                    <Port>$listen_port</Port>
                </Listen>
            </ListenList>
            <Service>
                <Guid>{53A92211-0041-47e1-9C6C-80DF6F496FF6}</Guid>
                <Name>DevProxy</Name>
                <Priority>7</Priority>
                <ApplicationID>31</ApplicationID>
                <Config />
            </Service>
            <Service>
                <Guid>{0293626F-D5F9-4d06-9522-FE0455D68E11}</Guid>
                <Name>FMVerSrv</Name>
                <Priority>3</Priority>
                <ApplicationID>30</ApplicationID>
                <Config>
                    <DefaultProduct>FMS101ZX</DefaultProduct>
                    <Product>
                        <ProductID>FMS001</ProductID>
                        <NewVersion>03.08.04.02</NewVersion>
                        <MinVersion>03.08.03.03</MinVersion>
                        <DownloadURL>http://fs.fsmeeting.com/download/FMDesktopYUNV3.8.4.2.exe</DownloadURL>
                        <DownloadURL>http://122.225.104.210/download/FMDesktopYUNV3.8.4.2.exe</DownloadURL>
                        <DownloadURL>http://60.12.108.210/download/FMDesktopYUNV3.8.4.2.exe</DownloadURL>
                        <GrayUpdate>
                            <Version>03.08.03.09</Version>
                            <NewVersion>03.08.04.99</NewVersion>
                            <MinVersion>03.08.03.99</MinVersion>
                            <DownloadURL>http://fs.fsmeeting.com/download/FMDesktopYUNV3.8.4.2.exe</DownloadURL>
                            <DownloadURL>http://122.225.104.210/download/FMDesktopYUNV3.8.4.2.exe</DownloadURL>
                        </GrayUpdate>
                        <GrayUpdate>
                            <Version>03.08.03.22</Version>
                            <NewVersion>03.08.04.22</NewVersion>
                            <MinVersion>03.08.03.22</MinVersion>
                            <DownloadURL>http://fs.fsmeeting.com/download/FMDesktopYUNV3.8.4.2.exe.test</DownloadURL>
                            <DownloadURL>http://122.225.104.210/download/FMDesktopYUNV3.8.4.2.exe.test</DownloadURL>
                        </GrayUpdate>
                    </Product>
                    <Product>
                        <ProductID>FMS101</ProductID>
                        <NewVersion>03.08.04.02</NewVersion>
                        <MinVersion>03.08.03.03</MinVersion>
                        <DownloadURL>http://fs.fsmeeting.com/download/FMDesktopYUNV3.8.4.2.exe</DownloadURL>
                    </Product>
                    <Product>
                        <ProductID>FMS101ZX</ProductID>
                        <NewVersion>03.08.03.03</NewVersion>
                        <MinVersion>03.08.03.03</MinVersion>
                        <DownloadURL>http://fs.fsmeeting.com/download/FMDesktopZXV3.8.exe</DownloadURL>
                    </Product>
                </Config>
            </Service>
            <Service>
                <Guid>{77186EA4-1B84-435c-BEAA-5846069E90B1}</Guid>
                <Name>FMFrontSrv</Name>
                <Priority>2</Priority>
                <ApplicationID>20</ApplicationID>
                <Config>

                    <SystemState>0</SystemState>
                    <LicenseFile>license.dat</LicenseFile>
                    <ParentNodeUpdateCheck>60000</ParentNodeUpdateCheck>
                    <NetConnType>1</NetConnType>

                    <auto_increment_increment>2</auto_increment_increment>

                    <auto_increment_offset>2</auto_increment_offset>
                    <CascadeConfig>CascadeConfig.xml</CascadeConfig>

                    <AccessConfig>AccessConfig.xml</AccessConfig>
                    <IPLibConfig>iplib.db</IPLibConfig>
                    
                    <PhoneAccess>1</PhoneAccess>
                    <MaxDBAccessCount>100</MaxDBAccessCount>

                    <ConfCtlIceServer>
                        <Port>10002</Port>
                    </ConfCtlIceServer>
                    <HttpProxy>
                        <GetCurrentUserInfo>
                            <url>https://192.168.5.58:8443/api/users/myself</url>
                            <language>zh-cn</language>
                        </GetCurrentUserInfo>
                    </HttpProxy>
                </Config>
            </Service>
            <Service>
                <Guid>{0CE5960D-0D77-454a-917D-EE22166B3F52}</Guid>
                <Name>FMVncSrv</Name>
                <Priority>2</Priority>
                <ApplicationID>2</ApplicationID>
                <Config />
            </Service>
             <Service>
                 <Guid>{B25E583F-E4BE-4b2d-AC99-897D3CFFEDC3}</Guid>
                 <Name>FMDocSrv</Name>
                 <Priority>2</Priority>
                 <ApplicationID>4</ApplicationID>
                 <Config />
             </Service>
            <Service>
                <Guid>{D135B8B6-B338-4d79-BA65-26EDB9107361}</Guid>
                <Name>FMFileMgrSrv</Name>
                <Priority>5</Priority>
                <ApplicationID>10</ApplicationID>
                <Config>
                </Config>
            </Service>
            <Service>
                <Guid>{7D47B2F8-AF37-4464-8EDB-FA3F9C55E10C}</Guid>
                <Name>FMFileSrv</Name>
                <Priority>4</Priority>
                <ApplicationID>3</ApplicationID>
                <Config>
                    <FileSavePath>Files</FileSavePath>
                    <CheckUpLoadFile>0</CheckUpLoadFile>
                    <MainService>0</MainService>
                    <DistributeFileSrv>0</DistributeFileSrv>
                    <DiskWarningPercent>80</DiskWarningPercent>
                    <ExtendDisk>
                        <Priority>1</Priority>
                        <FileDisk>E:\</FileDisk>
                    </ExtendDisk>
                    <HttpService>
                        <Run>1</Run>
                        <MimeTypeFile>mime.types</MimeTypeFile>
                    </HttpService>
                </Config>
            </Service>
            <Service>
                <Guid>{CFA241EA-9FA4-49eb-B93F-3A815A7C0512}</Guid>
                <Name>FMConfSrv</Name>
                <Priority>6</Priority>
                <ApplicationID>11</ApplicationID>
                <Config>
                    <TestConfig>
                        <WriteSessionData>0</WriteSessionData>
                        <ReadSessionData>0</ReadSessionData>
                        <ReadSessionDataFrom>0</ReadSessionDataFrom>
                        <ReadLoopCount>1</ReadLoopCount>
                    </TestConfig>
                    <MainService>1</MainService>
                    <ForceAVMix>0</ForceAVMix>
                    <PhoneAccess>1</PhoneAccess>
                    <MixConfig>AVMixConfig.xml</MixConfig>
                    <AVServiceConfig>
                        <Access>$access_url</Access>
                        <LocalAddr>$local_addr</LocalAddr>
                        <AppID>$app_id</AppID>
                        <VerificationCode>$verification_code</VerificationCode>
                        <ConfigIpList>$ConfigIpList</ConfigIpList>
                        <UseIpList>$IsUseIpList</UseIpList>
                    </AVServiceConfig>
                </Config>
            </Service>

            <Service>
                <Guid>{9935DBAB-548E-4F72-B81D-CFBB1A3F59A3}</Guid>
                <Name>TerminalManager</Name>
                <Priority>1</Priority>
                <ApplicationID>65532</ApplicationID>
                <Config>
                </Config>
            </Service>
        </ServiceProcess>
    </ProcessList>
</Root>
"""

'''
"config": {
    "ice_addr": "192.168.5.56:10001",
    "dev_id": "kevin",
    "dev_verify_code":"",
    "access_url": "http://192.168.7.165:8080",
    "app_id": "1234",
    "verification_code": "123456",
    "dev_group": "KevinGroup"
}
'''
items1 = {}
items1["access_url"] = conf["access_url"]

ice_addr = conf["ice_addr"].split(":")
items1["ice_port"] = ice_addr[1]
items1["ice_ip"] = ice_addr[0]
items1["dev_id"] = conf["dev_id"]
items1["dev_verify_code"] = conf["dev_verify_code"]
items1["app_id"] = conf["app_id"]
items1["verification_code"] = conf["verification_code"]
items1["listen_port"] = "10892"

items1["IsUseIpList"] = conf["IsUseIpList"]
items1["ConfigIpList"] = conf["ConfigIpList"]

items1["local_addr"] = "{listen_ip}:{listen_port}".format(listen_ip=sys.argv[2], listen_port=items1["listen_port"])

t1 = string.Template(template1)
content1 = t1.substitute(items1)

with open("{0}/group_as/ServiceConfig.xml".format(destdir), "w") as f:
    f.write(content1)

template2 = """
<?xml version="1.0" encoding="UTF-8" ?>

<ServerGroupSet>
    <ServerGroup GroupName = "Group1">
        <ServerDev>Dev1</ServerDev>
        <ServerDev>Dev2</ServerDev>
    </ServerGroup>
    <ServerGroup GroupName = "Group2">
        <ServerDev>Dev1</ServerDev>
        <ServerDev>Dev3</ServerDev>
        <ServerDev>Dev4</ServerDev>
        <ServerDev>Dev5</ServerDev>
        <ServerDev>Dev6</ServerDev>
    </ServerGroup>
    <ServerGroup GroupName = "ChineseGroup">
        <ServerDev>Dev18</ServerDev>
        <ServerDev>Dev24</ServerDev>
    </ServerGroup>
    <ServerGroup GroupName = "ForeignGroup">
        <ServerDev>Dev13</ServerDev>
    </ServerGroup>
    <ServerGroup GroupName = "$dev_group">
        <ServerDev>$dev_id</ServerDev>
    </ServerGroup>
</ServerGroupSet>

<NotMainServerSet>
    <NotMainServer>Dev99</NotMainServer>
</NotMainServerSet>

<VIPServerSet>
    <VIPServer>Dev10</VIPServer>
</VIPServerSet>

<SingleISPSet>
    <SingleISP>电信通</SingleISP>
</SingleISPSet>

<AccessRuleSet>
    <UserNameRuleSet>
        <UserNameRule>
            <UserName>test1</UserName>
            <UserName>test2</UserName>
            <UserName>test3</UserName>
            <UserName>test4</UserName>
            <GroupName>Group2</GroupName>
            <RoomID>10000</RoomID>
        </UserNameRule>
        <UserNameRule>
            <UserName>sep01</UserName>
            <UserName>sep04</UserName>
            <GroupName>dev61</GroupName>
        </UserNameRule>
        <UserNameRule>
            <UserName>sep00</UserName>
            <UserName>sep02</UserName>
            <GroupName>sep</GroupName>
        </UserNameRule>
        <UserNameRule>
            <UserName>yoga09</UserName>
            <UserName>sep06</UserName>
            <GroupName>$dev_group</GroupName>
        </UserNameRule>
    </UserNameRuleSet>
    <IPRuleSet>
        <IPRule>
            <StartIP>192.168.1.0</StartIP>
            <EndIP>192.168.1.255</EndIP>
            <GroupName>Dev1</GroupName>
        </IPRule>
        <IPRule>
            <StartIP>0.0.0.1</StartIP>
            <EndIP>255.255.255.255</EndIP>
            <GroupName>$dev_group</GroupName>
        </IPRule>
        <IPRule>
            <StartIP>192.168.5.0</StartIP>
            <EndIP>192.168.5.235</EndIP>
            <GroupName>$dev_group</GroupName>
        </IPRule>
        <IPRule>
            <IP>192.168.5.237</IP>
            <IP>192.168.6.218</IP>
            <GroupName>Group2</GroupName>
        </IPRule>
        <IPRule>
            <IP>192.168.5.110</IP>
            <GroupName>Dev2</GroupName>
        </IPRule>
    </IPRuleSet>
    <ISPRuleSet>
        <ISPRule>
            <ISPName>ISP1</ISPName>
            <ISPName>运营商2</ISPName>
            <GroupName>Group2</GroupName>
        </ISPRule>
        <ISPRule>
            <ISPName>电信通</ISPName>
            <GroupName>Dev132</GroupName>
        </ISPRule>
        <ISPRule>
            <ISPName></ISPName>
            <GroupName>dev61</GroupName>
        </ISPRule>
    </ISPRuleSet>
    <RegionRuleSet>
        <RegionRule>
            <RegionName>欧洲</RegionName>
            <GroupName>Dev100</GroupName>
        </RegionRule>
        <RegionRule>
            <RegionName>美国</RegionName>
            <RegionName>加拿大</RegionName>
            <GroupName>Dev110</GroupName>
        </RegionRule>
        <RegionRule>
            <RegionName>西藏</RegionName>
            <GroupName>Dev119</GroupName>
        </RegionRule>
        <!--地域规则(国外)，配置默认地域规则-->
        <RegionRule>
            <RegionName></RegionName>
            <GroupName>$dev_group</GroupName>
        </RegionRule>
    </RegionRuleSet>
    <RegionISPRuleSet>
        <RegionISPRule>
            <RegionName>广东</RegionName>
            <ISPName>电信</ISPName>
            <GroupName>gd_dx</GroupName>
        </RegionISPRule>
    </RegionISPRuleSet>
</AccessRuleSet>
"""


items2 = {}
items2["dev_group"] = conf["dev_group"]
items2["dev_id"] = conf["dev_id"]

t2 = string.Template(template2)
content2 = t2.substitute(items2)

with open("{0}/group_as/AccessConfig.xml".format(destdir), "w") as f:
    f.write(content2)

###### run

os.chdir("{0}/group_as".format(destdir))
pid = subprocess.Popen(["./FM_Server"], env={"LD_LIBRARY_PATH":"{0}/group_as".format(destdir)}).pid

###### record

stream_installer.save_service_status(name="group_as", script="", pid=[pid])

