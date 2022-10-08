#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文
import myConfigParser
from globalVar import G_V
import os
import re
import sys
import time
import logging
thisPath = sys.path[0] + "/wpa/wpa_supplicant.conf"

class wrConf():
	@staticmethod
	def myWrite():
		#读取数据编辑
		fileRe = open(thisPath,"r+")
		date = fileRe.read()
		date = date.strip()
		lineList = date.split("\n")
		for line in range(0,len(lineList)):
			#print lineList[line]
			if lineList[line].__contains__("ssid=\""):
				lineList[line] = "ssid=\"" + G_V.G_APSSID + "\""
			if lineList[line].__contains__("psk="):
				lineList[line] = "psk=\"" + G_V.G_APpsk + "\""
		fileRe.close()
		#print("lineList:",lineList)
		#写入到程序
		fileWr = open(thisPath,"w+")
		for lineMsg in lineList:
			fileWr.write(lineMsg + "\n")
		thisConf = ""
		logging.debug("wpa_supplicant.conf:"+G_V.G_APSSID+ " " + G_V.G_APpsk)
		fileWr.close()
