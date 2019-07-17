#!/usr/bin/env python
# -*- coding: utf-8 -*-
class LoginPage:
	def __init__(self, driver):
		"""对象库层"""
		self.driver = driver

	def find_username_ele(self):
		"""用户名输入框定位信息"""
		return self.driver.find_element_by_xpath(
			".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input")

	def find_pwd_ele(self):
		"""密码输入框定位"""
		return self.driver.find_element_by_xpath(
			".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input")

	def find_click_btn_ele(self):
		"""登录按钮定位"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'立即登录')]")

	def find_sucess_text_ele(self):
		"""登录页面成功后找到标题"""
		return self.driver.find_element_by_xpath(".//body/div[1]/descendant::a[1]")

	def find_fail_text_ele(self):
		"""登陆不成功，卡在登录主界面“声像情报分析系统”"""
		return self.driver.find_element_by_xpath(".//body/descendant::h1")