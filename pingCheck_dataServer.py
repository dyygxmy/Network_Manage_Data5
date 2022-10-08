#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#有上面一條後才能在在註釋上用中文
from globalVar import G_V
import threading
import time
import myPing
import logging
logging.debug("pingCheck_dataServer Start")

class pingCheck_dataServer(threading.Thread):
	def __init__(self,threadID,threadName,delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.delay = delay
		
	def run(self):
		while G_V.G_networkMode == 0:
			reServer = myPing.myPing(G_V.G_serverIp,"result")
			pingServerResult = reServer.getPingResult()
			#pingServerResult = "ttl"
			if (not pingServerResult):
				G_V.G_pingServerResult = False
			else:
				G_V.G_pingServerResult = True
			time.sleep(self.delay)
thread1 = pingCheck_dataServer(7,"thread7",0.5)
thread1.start()
