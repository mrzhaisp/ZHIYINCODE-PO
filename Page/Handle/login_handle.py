#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Basepage.login_page import LoginPage
import time as t


class LoginHandle:
	"""封装操作层"""

	def __init__(self, driver):
		self.lop = LoginPage(driver)

	def input_username(self, username):
		"""账户框操作"""
		self.lop.find_username_ele().send_keys(username)

	def input_pwd(self, pwd):
		"""密码操作层"""
		self.lop.find_pwd_ele().send_keys(pwd)

	def click_btn(self):
		"""登录按钮点击"""
		self.lop.find_click_btn_ele().click()

	def login_sucess_text(self):
		"""成功后拿到text"""
		# return self.lop.find_text_ele().text
		for i in range(10):
			try:
				textone = self.lop.find_sucess_text_ele().text
				return textone
			except:
				pass
			t.sleep(1)

	def login_fail_text(self):
		"""登录不成，则停留在主页面，拿到主页面的h1标签"""
		for i in range(10):
			try:
				textone = self.lop.find_fail_text_ele().text
				return textone
			except:
				pass
			t.sleep(1)
