#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文
import myConfigParser
import sys
class G_V():
	G_isConnected = False #是否有连接成功过
	G_isNewVersion = False # 是否为新版本 新版本（任务栏开始用的） 旧版本（以前就用的）
	G_isBrctl = 0 # 0 不用桥接  1 使用桥接
	G_pingResult = False # ping 网关的结果
	G_pingServerResult = False # ping 服务器的结果
	G_pingRfidResult = False # ping RFID 的结果
	G_pingIP="111.111.111.111" # 记录无线的网关
	G_gatewayIP_eth0 = "111.111.111.111" # 记录有线1的网关
	G_gatewayIP_eth1 = "111.111.111.111" # 记录有线2的网关
	G_connectGateway = "wlan0" # 当前哪个网卡设置网关 默认wlan0
	G_wirelessNetIp="111.111.111.111" # 记录无线的IP地址
	G_EthernetIp1="111.111.111.111" # 记录有线1的IP地址
	G_EthernetIp2="111.111.111.111" # 记录有线2的IP地址
	G_wirelessNetIpTemp = "111.111.111.111" # 记录本次读取的无线IP地址
	G_EthernetIp1Temp = "111.111.111.111" # 记录本次读取的有线1的IP地址
	G_EthernetIp2Temp = "111.111.111.111" # 记录本次读取的有线2的IP地址
	G_serverIp = "111.111.111.111" # 记录服务器的IP地址
	G_rfidIp = "111.111.111.111" # 记录rfid的IP地址
	G_netmask = "0.0.0.0" # 记录无线的子网掩码
	G_netmask_eth0 = "0.0.0.0" # 记录有线1的子网掩码
	G_netmask_eth1 = "0.0.0.0" # 记录有线2的子网掩码
	G_APSSID = "" # 记录准备连接AP的SSID
	G_APpsk = "" # 记录准备连接AP的密码
	G_networkMode = 0 # 记录网络模式 0：wifi 1：热点  默认为wifi模式
	G_hotspotName = "" # 热点账户名
	G_hotspotPsk = "" # 热点密码
	G_hotspotIP = "111.111.111.111" # 热点IP
	G_hotspotIP_head = "111.111.111.111" # 热点分配的最小IP
	G_hotspotIP_end = "111.111.111.111" # 热点分配的最大IP
	G_hotspotTime = 24 # 热点开放时间
	G_test_wifiPath = "/var/test_wifi"#该文件记录ping网关/服务器/RFID的结果
	G_wpaPath = sys.path[0] + "/wpa/wpa_supplicant.conf"#wpa_supplicant工具连网配置文件位置
	G_sections1 = "baseinfo"#网络配置文件内的节点名
	G_openHotspot="true" # 是否开启热点
	config = myConfigParser.myConfigParser()#提取配置文件数据
	G_networkPath = "/config.ini"
	G_wirelessGateway_name = "wirelessGateway"
	G_EthernetGateway1_name = "EthernetGateway1"
	G_EthernetGateway2_name = "EthernetGateway2"
	G_connectGateway_name = "connectGateway"
	G_wirelessIP_name = "wirelessIP"
	G_EthernetIP1_name = "EthernetIP1"
	G_EthernetIP2_name = "EthernetIP2"
	G_wirelessNetmask_name = "wirelessNetmask"
	G_EthernetNetmask1_name = "EthernetNetmask1"
	G_EthernetNetmask2_name = "EthernetNetmask2"
	G_wirelessSSID_name = "wirelessSSID"
	G_wirelessPsk_name = "wirelessPsk"
	G_DataServerIp_name = "DataServerIp"
	G_RfidIp_name = "RfidIp"
	G_networkMode_name = "networkMode"
	G_hotspotName_name = "hotspotName"
	G_hotspotPsk_name = "hotspotPsk"
	G_hotspotIP_name = "hotspotIP"
	G_hotspotIP_head_name = "hotspotIP_head"
	G_hotspotIP_end_name = "hotspotIP_end"
	G_hotspotTime_name = "hotspotTime"
	G_isBrctl_name = "isBrctl"

	if G_isNewVersion:
		G_networkPath = "/allMyConfig/network.ini"#主配置文件
	else:
		G_networkPath = "/config.ini"  # 主配置文件
		G_wirelessGateway_name = "gateway"
		G_wirelessIP_name = "WirelessIp"
		G_EthernetIP1_name = "LocalIp"
		G_EthernetIP2_name = "LocalIp2"
		G_wirelessNetmask_name = "netmask"
		G_wirelessSSID_name = "SSID"
		G_wirelessPsk_name = "psk"