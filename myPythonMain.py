#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文
import os
import time
import sys
from datetime import datetime
from myPrint import myPrint
import logging
logging.debug("myPythonMain Start")
from globalVar import G_V
print(datetime.now())
from configCheck import configCheck #启动configCheck线程
#测试在调用configCheck前2020-12-09 14:10:57.540098，到所有值取完2020-12-09 14:10:59.072144 
#为了保险，延时2秒，保证后面用到全局变量是已经在配置文件中取值过的
time.sleep(2)

print G_V.G_pingIP
print G_V.G_wirelessNetIp
print G_V.G_EthernetIp1
print G_V.G_EthernetIp2
print G_V.G_netmask
print G_V.G_APSSID
print G_V.G_APpsk


if G_V.G_connectGateway == "eth0":  # 网关选的 eth0
    gwSetStr = "route add default gw " + G_V.G_gatewayIP_eth0 + " eth0"
    logging.debug(gwSetStr)
    os.system(gwSetStr)
if G_V.G_connectGateway == "eth1":  # 网关选的 eth1
    gwSetStr = "route add default gw " + G_V.G_gatewayIP_eth1 + " eth1"
    logging.debug(gwSetStr)
    os.system(gwSetStr)

from wifiCrtl import wifiCrtl	#启动wifiCrtl线程
from pingCheck_manage import pingCheck_manage #启动pingCheck_manage线程
from pingCheck_gateway import pingCheck_gateway	#启动pingCheck_gateway线程
from pingCheck_dataServer import pingCheck_dataServer	#启动pingCheck_dataServer线程
from pingCheck_rfid import pingCheck_rfid	#启动pingCheck_rfid线程
from saveWlanState import savWlan #ֱ启动saveWlanState线程

#setEthernetIp1Bash="ifconfig eth0 " + G_V.G_EthernetIp1
#print setEthernetIp1Bash
#os.system(setEthernetIp1Bash)

#setEthernetIp2Bash="ifconfig eth1 " + G_V.G_EthernetIp2
#print setEthernetIp2Bash
#os.system(setEthernetIp2Bash)


time.sleep(10)
os.system("xset s 0 dpms 0 0 0")#屏保不启用


