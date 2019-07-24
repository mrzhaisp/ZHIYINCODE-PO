#!/usr/bin/env python
# -*- coding: utf-8 -*-
class YinShiPinPage:
	"""音视频首页title"""

	def __init__(self,driver):
		self.driver = driver

	def find_column_yinhsipin_btn(self):
		"""音视频"""
		return self.driver.find_element_by_xpath(".//body/div[1]/descendant::a[2]")

	def find_shishiredian_btn(self):
		"""事实热点title"""
		return self.driver.find_element_by_xpath(".//body/div[1]/section/descendant::a[4]")

	def find_title_neiwangzibian_btn(self):
		"""内网自编title"""
		return self.driver.find_element_by_xpath(".//body/div[1]/section/descendant::p[1]")

	def find_title_waiwang_btn(self):
		"""外网资源title"""
		return self.driver.find_element_by_xpath(".//body/div[1]/section/descendant::p[2]")

	def find_title_guanzhu_btn(self):
		"""我的关注"""
		return self.driver.find_element_by_xpath(".//body/div[1]/section/descendant::p[3]")
























