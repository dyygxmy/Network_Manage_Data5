#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文
from globalVar import G_V
import myConfigParser
import threading
import sys
import commands
import os
import time
import logging
from datetime import datetime
logging.debug("configCheck Start")

#监控配置文件，对部分IP等配置变化实时更新
class configCheck(threading.Thread):
	def __init__(self, threadID, threadName, delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.delay = delay

	def run(self):
		hotspotIPTemp = "222.222.222.222"
		networkModeTemp = 9 # 初始桥接选择有变化
		isBrctlTemp = 9 # 初始桥接选择有变化
		while 1:
			G_V.config.read(G_V.G_networkPath)
			for sections in G_V.config.sections():#获取配置文件数据
				if sections == G_V.G_sections1:
					for items in G_V.config.items(sections):
						if items[0] == G_V.G_wirelessGateway_name:
							G_V.G_pingIP = items[1]  # 获取 wlan0 网关IP信息
						if items[0] == G_V.G_EthernetGateway1_name:
							G_V.G_gatewayIP_eth0 = items[1]  # 获取 eth0 网关IP信息
						if items[0] == G_V.G_EthernetGateway2_name:
							G_V.G_gatewayIP_eth1 = items[1]  # 获取 eth1 网关IP信息
						if items[0] == G_V.G_connectGateway_name:
							G_V.G_connectGateway = items[1]  # 哪个网卡去连接网关
						if items[0] == G_V.G_wirelessNetmask_name:
							G_V.G_netmask = items[1]  # 获取 wlan0 子网掩码IP信息
						if G_V.G_isNewVersion: #任务栏版本独立设置2个本地网卡的子网掩码
							if items[0] == G_V.G_EthernetNetmask1_name:
								G_V.G_netmask_eth0 = items[1]  # 获取 eth0 子网掩码IP信息
							if items[0] == G_V.G_EthernetNetmask2_name:
								G_V.G_netmask_eth1 = items[1]  # 获取 eth1 子网掩码IP信息
						else: #非任务栏新版本的2个本地网卡的子网掩码固定为"255.255.255.0"
							G_V.G_netmask_eth0 = "255.255.255.0"
							G_V.G_netmask_eth1 = "255.255.255.0"
						if items[0] == G_V.G_DataServerIp_name:
							G_V.G_serverIp = items[1]  # 获取服务器IP信息
						if items[0] == G_V.G_RfidIp_name:
							G_V.G_rfidIp = items[1]  # 获取RFID设备的IP信息
						if items[0] == G_V.G_wirelessIP_name:
							G_V.G_wirelessNetIp = items[1]  # 获取无线IP信息
						if items[0] == G_V.G_EthernetIP1_name:
							G_V.G_EthernetIp1 = items[1]  # 获取本地1 IP信息
						if items[0] == G_V.G_EthernetIP2_name:
							G_V.G_EthernetIp2 = items[1]  # 获取本地2 IP信息
						if items[0] == G_V.G_wirelessSSID_name:
							G_V.G_APSSID = items[1]  # 获取无线连接的SSID信息
						if items[0] == G_V.G_wirelessPsk_name:
							G_V.G_APpsk = items[1]  # 获取无线连接的密码
						if items[0] == G_V.G_networkMode_name:
							G_V.G_networkMode = int(items[1])  # 获取网络使用模式 0:wifi 1:热点
						if items[0] == G_V.G_hotspotName_name:
							G_V.G_hotspotName = items[1]  # 获取热点名称
						if items[0] == G_V.G_hotspotPsk_name:
							G_V.G_hotspotPsk = items[1]  # 获取热点密码
						if items[0] == G_V.G_hotspotIP_name:
							G_V.G_hotspotIP = items[1]  # 获取热点IP信息
						if items[0] == G_V.G_hotspotIP_head_name:
							G_V.G_hotspotIP_head = items[1]  # 获取热点的起始IP
						if items[0] == G_V.G_hotspotIP_end_name:
							G_V.G_hotspotIP_end = items[1]  # 获取热点的最大IP
						if items[0] == G_V.G_hotspotTime_name:
							G_V.G_hotspotTime = int(items[1])  # 获取热点开启时间
						if items[0] == G_V.G_isBrctl_name:
							G_V.G_isBrctl = int(items[1])  # 是否桥接
			#print(datetime.now())
			#checkIp = str(networkModeTemp) + "," + str(G_V.G_networkMode)
			#logging.debug(checkIp)
			if networkModeTemp != G_V.G_networkMode:#  networkMode 有变化才处理
				networkModeTemp = G_V.G_networkMode
				if G_V.G_networkMode == 0 :# 热点模式变成WIFI模式 关闭热点
					hotspotStopStr = "ap-hotspot stop"
					logging.debug(hotspotStopStr)
					os.system(hotspotStopStr)
				else:# 热点模式 检测到 networkMode 的时候 hotspotIP 也已经保存到配置文件 启动热点的时候直接调取该IP，不需要另外设置
					setHotspotNameStr = "sed -i \"s/ssid=.*/ssid=" + G_V.G_hotspotName + "/g\" /etc/ap-hotspot.conf"
					logging.debug(setHotspotNameStr)
					os.system(setHotspotNameStr)
					setHotspotPskStr = "sed -i \"s/wpa_passphrase=.*/wpa_passphrase=" + G_V.G_hotspotPsk + "/g\" /etc/ap-hotspot.conf"
					logging.debug(setHotspotPskStr)
					os.system(setHotspotPskStr)
					setHotspotStr_dhcpRange = "sed -i \"s/dhcp-range=.*/dhcp-range=" + G_V.G_hotspotIP_head + "," + G_V.G_hotspotIP_end + "," + str(G_V.G_hotspotTime) + "h/g\" /etc/dnsmasq.d/ap-hotspot.rules"
					logging.debug(setHotspotStr_dhcpRange)
					os.system(setHotspotStr_dhcpRange)
					closeWifiStr = "killall wpa_supplicant"
					logging.debug(closeWifiStr)
					os.system(closeWifiStr)
					openHotspotStr = "ap-hotspot start"
					logging.debug(openHotspotStr)
					os.system(openHotspotStr)
			else:
				if G_V.G_networkMode == 0 :# 在稳定WIFI模式下wlan0的IP设置有变化即刻生效
					selectWlan0IPStr = "ifconfig | grep -A 1 wlan0 |awk '{print $2}' | grep : | awk -F : '{print $2}'"
					(selectWlan0IP_status, selectWlan0IP_output) = commands.getstatusoutput(selectWlan0IPStr)
					if selectWlan0IP_output != G_V.G_wirelessNetIp:#wlan0的IP 实际与配置不一致则按配置同步
						ifconfigSetStr = "ifconfig wlan0 " + G_V.G_wirelessNetIp + " netmask " + G_V.G_netmask
						os.system(ifconfigSetStr)
			if isBrctlTemp != G_V.G_isBrctl: # 桥接选择有变化
				isBrctlTemp = G_V.G_isBrctl
				if G_V.G_isBrctl: # 打开桥接
					os.system("ifconfig eth0 up") # 开启网卡eth0
					os.system("ifconfig eth1 up") # 开启网卡eth1
					os.system("ip addr flush dev eth0") # 清除网卡IP防止冲突
					os.system("ip addr flush dev eth1") # 清除网卡IP防止冲突
					os.system("brctl addbr br0") # 建立网桥连接（这里我们取名为br0）
					setBr0Bash = "ifconfig br0 " + G_V.G_EthernetIp1
					os.system(setBr0Bash) # 设置br0 IP
					os.system("brctl addif br0 eth0 eth1") # 将eth0 eth1添加到桥接br0中
				else: # 不打开桥接
					os.system("brctl delif br0 eth0 eth1") #删除br0中的eth0 eth1桥接
					os.system("ip addr flush dev br0") # 清除网卡IP防止冲突
					selectEth0IPStr = "ifconfig | grep -A 1 eth0 |awk '{print $2}' | grep : | awk -F : '{print $2}'"
					(selectEth0IP_status, selectEth0IP_output) = commands.getstatusoutput(selectEth0IPStr)
					if selectEth0IP_output != G_V.G_EthernetIp1:#eth0的IP 实际与配置不一致则按配置同步
						ifconfigSetStr = "ifconfig eth0 " + G_V.G_EthernetIp1 + " netmask " + G_V.G_netmask_eth0
						os.system(ifconfigSetStr)
					selectEth1IPStr = "ifconfig | grep -A 1 eth1 |awk '{print $2}' | grep : | awk -F : '{print $2}'"
					(selectEth1IP_status, selectEth1IP_output) = commands.getstatusoutput(selectEth1IPStr)
					if selectEth1IP_output != G_V.G_EthernetIp2:#eth1的IP 实际与配置不一致则按配置同步
						ifconfigSetStr = "ifconfig eth1 " + G_V.G_EthernetIp2 + " netmask " + G_V.G_netmask_eth1
						os.system(ifconfigSetStr)
			time.sleep(self.delay)
thread6 = configCheck(6, "thread6", 5)
thread6.start()