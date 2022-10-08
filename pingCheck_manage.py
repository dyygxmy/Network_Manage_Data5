#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文
from globalVar import G_V
import threading
import time
import myPing
import logging
logging.debug("pingCheck_manage Start")

class pingCheck_manage(threading.Thread):
	def __init__(self,threadID,threadName,delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.delay = delay
		
	def run(self):
		while G_V.G_networkMode == 0:
			pingResult = "0"
			pingServerResult = "0"
			pingRfidResult = "0"
			fileWr = open(G_V.G_test_wifiPath,"w+")
			if G_V.G_pingResult:
				pingResult = "1"
			if G_V.G_pingServerResult:
				pingServerResult = "1"
			if G_V.G_pingRfidResult:
				pingRfidResult = "1"
			writeMsg =pingResult + " "+ pingServerResult + " " + pingRfidResult
			fileWr.write(writeMsg)
			fileWr.close()
			time.sleep(self.delay)
thread1 = pingCheck_manage(5,"thread5",0.5)
thread1.start()
