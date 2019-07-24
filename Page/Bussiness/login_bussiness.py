#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.base_driver import BaseDriver
from Commonlib.commonlib import Commonlib
from Page.Handle.login_handle import LoginHandle
import time as t

class LoginBussiness:
	"""登录的业务层"""

	def __init__(self, driver):
		# self.basedriver = BaseDriver()
		# driver = self.basedriver.getdriver()
		self.common = Commonlib(driver)
		self.loghandle = LoginHandle(driver)

	def logoin(self, username, pwd):
		self.common.open_browser("http://10.168.103.151/web/#/login")
		self.common.wait_time(1)
		self.loghandle.input_username(username)
		self.common.wait_time(1)
		self.loghandle.input_pwd(pwd)
		self.common.wait_time(1)
		self.loghandle.click_btn()
		t.sleep(5)

