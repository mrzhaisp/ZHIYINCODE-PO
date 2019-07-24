#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Basepage.yinshipin_page import YinShiPinPage

class YinshiPinHandle:
	"""登录音视频前台栏目操作层"""

	def __init__(self,driver):
		self.ysp = YinShiPinPage(driver)

	def click_yinship(self):
		"""音视频title"""
		self.ysp.find_column_yinhsipin_btn().click()

	def text_shisrd_title(self):
		"""事实热点title"""
		return self.ysp.find_shishiredian_btn().text

	def text_neiwzb_title(self):
		"""内网自编title"""
		return self.ysp.find_title_neiwangzibian_btn().text

	def text_waiwang_title(self):
		"""外网资源"""
		return self.ysp.find_title_waiwang_btn().text

	def text_wodeguanzhu_title(self):
		return self.ysp.find_title_waiwang_btn().text











