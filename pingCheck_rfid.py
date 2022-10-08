#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#有上面一條後才能在在註釋上用中文
from globalVar import G_V
import threading
import time
import myPing
import logging
logging.debug("pingCheck_rfid Start")

class pingCheck_rfid(threading.Thread):
	def __init__(self,threadID,threadName,delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.delay = delay
		
	def run(self):
		while G_V.G_networkMode == 0:
			reRfid = myPing.myPing(G_V.G_rfidIp,"result")
			pingRfidResult = reRfid.getPingResult()
			#pingRfidResult = "ttl"
			if (not pingRfidResult):
				G_V.G_pingRfidResult = False
			else:
				G_V.G_pingRfidResult = True
			time.sleep(self.delay)
thread2 = pingCheck_rfid(2,"thread2",0.5)
thread2.start()
