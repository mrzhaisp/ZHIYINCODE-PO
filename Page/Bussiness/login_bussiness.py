#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.base_driver import BaseDriver
from Page.Handle.login_handle import LoginHandle
import time as t

class LoginBussiness:
	"""登录的业务层"""

	def __init__(self, driver):
		# self.basedriver = BaseDriver()
		# driver = self.basedriver.getdriver()
		self.loghandle = LoginHandle(driver)

	def logoin(self, username, pwd):
		self.loghandle.input_username(username)
		self.loghandle.input_pwd(pwd)
		self.loghandle.click_btn()
		t.sleep(2)


		# text = self.loghandle.sucess_get_text()
		# print(text)   # 声像情报融合分析平台
		# texttwo = self.loghandle.login_fail_text()
# 		# print(texttwo)
#
# ha = LoginBussiness()
# ha.logoin("admin","asasasasa")