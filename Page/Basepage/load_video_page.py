#!/usr/bin/env python
# -*- coding: utf-8 -*-
class LoginVideoPage:
	"""登录后台上传视频"""

	def __init__(self, driver):
		self.driver = driver

	def find_user_ele(self):
		"""登录密码框"""
		return self.driver.find_element_by_xpath(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input")

	def find_pwd_ele(self):
		"""密码输入框"""
		return self.driver.find_element_by_xpath(".//body/descendant::input[2]")

	def find_click_ele(self):
		"""点击框"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'立即登录')]")

	def find_sucess_text_ele(self):
		"""登录成功拿到固定的文字    视频管理"""
		return self.driver.find_element_by_xpath(".//body/descendant::section[2]/descendant::span[1]")

	def find_fail_text_ele(self):
		"""登录失败停留在登录页面，拿到固定的文字   声像情报分析系统"""
		return self.driver.find_element_by_xpath(".//body/div/descendant::h1")




