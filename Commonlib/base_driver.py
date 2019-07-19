#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time as t

class BaseDriver:
	"""实例化webdriver"""
	@classmethod
	def getdriver(self):
		self.driver = webdriver.Chrome()
		t.sleep(3)
		return self.driver










