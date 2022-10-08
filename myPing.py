#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文

import os

class myPing:
	def __init__(self,ip,type):
		self.ip = ip
		self.type = type
		
	def getPingResult(self):
		if self.type == "msg":
			pingBash = "ping -W 3 -c 1 " + self.ip
		elif self.type == "result":
			pingBash = "ping -W 3 -c 1 " + self.ip + " | grep ttl="
		process = os.popen(pingBash)
		pingResult = process.read()
		process.close()
		if self.type == "msg":
			return pingResult
		elif self.type == "result":
			return bool(pingResult)


