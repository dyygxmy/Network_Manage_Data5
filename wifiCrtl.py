#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文
from globalVar import G_V
from writeConfig import wrConf
import threading
import time
import os
import logging
import sys
import commands
logging.debug("wifiCrtl Start")

class wifiCrtl(threading.Thread):
	def __init__(self,threadID,threadName,delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.delay = delay
		
	def run(self):
		while 1:
			#logging.debug(G_V.G_pingResult)
			if not G_V.G_pingResult and G_V.G_networkMode == 0:
				wrConf.myWrite()#保存到 wpa_supplicant 配置文件
				os.system("killall wpa_supplicant")
				os.system("rfkill unblock all")
				#os.system("ifconfig wlan0 down")
				#os.system("ip link set wlan0 address 28:c6:3f:f7:f9:a9")
				os.system("ifconfig wlan0 up")
				logging.debug("wpa_supplicant Start")
				os.system("wpa_supplicant -Dnl80211 -iwlan0 -c" + G_V.G_wpaPath + " &")
				logging.debug("wpa_supplicant run")
				ifconfigSetStr = "ifconfig wlan0 " + G_V.G_wirelessNetIp + " netmask " + G_V.G_netmask
				logging.debug(ifconfigSetStr)
				os.system(ifconfigSetStr)
				myWait = 0
				while myWait < 31:#联网等待30s，如果连接成功则不需要等待
					if G_V.G_pingResult:
						break
					time.sleep(1)
					myWait += 1
				if G_V.G_connectGateway == "wlan0":# 网关选的 wlan0 则启用
					(routeDel_status, routeDel_output) = commands.getstatusoutput("route del default")
					while routeDel_status == 0:
						(routeDel_status, routeDel_output) = commands.getstatusoutput("route del default")
					gwSetStr = "route add default gw " + G_V.G_pingIP + " wlan0"
					logging.debug(gwSetStr)
					#os.system(gwSetStr)
					routeSet_status,routeSet_output = commands.getstatusoutput(gwSetStr)
					logging.debug("routeSet:"+str(routeSet_status)+" "+routeSet_output)
				logging.debug("wpa_supplicant end:"+str(G_V.G_pingResult))
			time.sleep(self.delay)
thread1 = wifiCrtl(1,"thread1",5)
thread1.start()
