#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文
import myConfigParser
import os
import re
import sys
import time
import threading


thisPath = sys.path[0] + "/confTest.conf"
config = myConfigParser.myConfigParser()#提取配置文件数据
NetCard = ""
NetCardSignal = ""
WlanName = ""

class savWlan(threading.Thread):
	def __init__(self,threadID,threadName,delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.delay = delay

	def run(self):
		while 1:
			global NetCard,NetCardSignal,WlanName
			iwconfigBash = "iwconfig"
			#print iwconfigBash.find("aafig")
			#print iwconfigBash.index("aafig")
			process = os.popen(iwconfigBash)
			iwconfigResult = process.read()
			process.close()
			lineList = iwconfigResult.split("\n")
			for lineData in lineList:
				lineData = lineData.strip()
				if lineData.__contains__("ESSID:"):
					NetCard = lineData[0:5]
					WlanName = lineData[lineData.find("ESSID:"):]
					WlanName = re.sub("\"","",re.sub("ESSID:",'',WlanName))
				if lineData.__contains__("Signal level="):
					NetCardSignal = lineData[lineData.find("Signal level="):lineData.find("dBm")]
					NetCardSignal = re.sub(" ","",re.sub("Signal level=","",NetCardSignal))
				#print lineData
	
			config.read(thisPath)
			#先将原配置数据保存下来
			for sections in config.sections():
				for items in config.items(sections):
					config.set(sections,items[0],items[1])
	
			#section不存在就新建一个
			if "key1" not in config.sections():
				config.add_section("key1")
		
			#数据有变化的另再修改下
			config.set("key1","NetCard",NetCard)#给section中option赋值（新增，或者是修改）
			config.set("key1","NetCardSignal",NetCardSignal)
			config.set("key1","WlanName",WlanName)
			CurrentTime = time.strftime("%Y-%m-%d %H:%M:%S")
			config.set("key1","CurrentTime",CurrentTime)
			#config.write(thisPath)
			with open(thisPath,"w+") as f:
				config.write(f)
			time.sleep(self.delay)
	#print(iwconfigResult)
thread3 = savWlan(3,"thread3",1)
thread3.start()
