#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#有上面一條後才能在在註釋上用中文
from globalVar import G_V
import threading
import time
import myPing
import logging
import os
from datetime import datetime
logging.debug("pingCheck_gateway Start")

class pingCheck_gateway(threading.Thread):
	def __init__(self,threadID,threadName,delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.delay = delay
		
	def run(self):
		while G_V.G_networkMode == 0:
			time1 = datetime.now()
			time2 = datetime.now()
			re = myPing.myPing(G_V.G_pingIP,"result")
			pingResult = re.getPingResult()
			#pingResult = "ttl"
			if (not pingResult):
				time2 = datetime.now()
				G_V.G_pingResult = False
				#if (time2-time1).seconds > 3 and G_V.G_networkMode == 0: #测试用，直接在掉线状态时启动的，没有之前连接状态，掉线时间为大于3秒
				if G_V.G_isConnected and (time2-time1).seconds > 15 and G_V.G_networkMode == 0:
					logging.debug("connect timeout(15s) restart wlan0")
					downWlan0Str = "ifconfig wlan0 down"
					upWlan0Str = "ifconfig wlan0 " + G_V.G_wirelessNetIp + " netmask " + G_V.G_netmask
					addWlanGwStr = "route add default gw " + G_V.G_pingIP + " wlan0"
					os.system(downWlan0Str)
					os.system(upWlan0Str)
					os.system(addWlanGwStr)
			else:
				time1 = datetime.now()
				G_V.G_pingResult = True
				G_V.G_isConnected = True # 只要有连接成功过就变True
			time.sleep(self.delay)
thread1 = pingCheck_gateway(6,"thread6",0.5)
thread1.start()
