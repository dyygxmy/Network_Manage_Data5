#!/usr/bin/python
# -*- coding: UTF-8 -*-
#有上面一条后才能在注释上使用中文
import ConfigParser

#自定义.conf文件获取
class myConfigParser(ConfigParser.ConfigParser):
	def __init__(self,defaults=None):
		ConfigParser.ConfigParser.__init__(self,defaults=defaults)
	def optionxform(self,optionstr):
		return optionstr
