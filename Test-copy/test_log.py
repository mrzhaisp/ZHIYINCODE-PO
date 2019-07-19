#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.logg import LoggIn
from selenium import webdriver
class Testlog:
	def openbaidu(self):
		LoggIn.logg_out("打开浏览器")
		self.dr = webdriver.Chrome()
		LoggIn.logg_out("打开百度")
		self.dr.get("http:www.baidu.com")

t = Testlog()
t.openbaidu()













