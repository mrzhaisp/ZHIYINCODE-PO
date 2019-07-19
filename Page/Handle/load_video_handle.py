#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Basepage.load_video_page import LoginVideoPage
import time as t
class LoadVideoHandle:
	"""封装上传视频handler"""
	def __init__(self,driver):
		self.lop= LoginVideoPage(driver)

	def input_username(self,username):
		"""找到用户名框输入名字"""
		self.lop.find_user_ele().send_keys(username)

	def input_pwd(self,pwd):
		"""密码框输入密码"""
		self.lop.find_pwd_ele().send_keys(pwd)

	def click_btn(self):
		"""登录按钮"""
		self.lop.find_click_ele().click()


	def log_sucess_text(self):
		"""登录成功拿到页面文字"""
		for i in range(10):
			try:
				sucesstext = self.lop.find_sucess_text_ele().text
				return sucesstext
			except:pass
			t.sleep(1)

	def login_fail_text(self):
		"""登录失败后 停在首页拿到首页文字"""
		for i in range(10):
			try:
				failtext = self.lop.find_fail_text_ele().text
				return failtext
			except:pass
			t.sleep(1)








