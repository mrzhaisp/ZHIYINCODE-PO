#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time as t
class BaseDriver:
	"""实例化webdriver"""
	def getdriver(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		# self.driver.implicitly_wait(30)
		self.driver.get("http://10.168.103.151/web/#/login")
		t.sleep(5)
		return self.driver










