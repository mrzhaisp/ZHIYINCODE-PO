#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.logg import LoggIn
from Commonlib.base_driver import BaseDriver
from Commonlib.commonlib import Commonlib
from Page.Handle.yinshipin_handle import YinshiPinHandle
from Page.Bussiness.login_bussiness import LoginBussiness

class YinShiPinBusiness:
	"""音视频业务分类"""

	def __init__(self,driver):
		self.lo = LoggIn()
		self.c = Commonlib(driver)
		self.login = LoginBussiness(driver)
		self.yinsp = YinshiPinHandle(driver)

	def yin_shipin_index(self,username,pwd):
		# titlelist = []
		self.lo.logg_out("登录音视频前台")
		self.login.logoin(username,pwd)
		self.c.wait_time(3)

		self.lo.logg_out("打开音视频栏目")
		self.yinsp.click_yinship()
		self.c.wait_time(2)


		# text_shishiredian = self.yinsp.text_shisrd_title()
		# titlelist.append(text_shishiredian)
		#
		# text_neiwangzibian = self.yinsp.text_neiwzb_title()
		# titlelist.append(text_neiwangzibian)
		#
		# text_waiwangziyuan = self.yinsp.text_waiwang_title()
		# titlelist.append(text_waiwangziyuan)
		#
		# text_guanzhu = self.yinsp.text_wodeguanzhu_title()
		# titlelist.append(text_guanzhu)
		#
		# print(titlelist)
		# # ['时事热点', '内网自编', '外网资源', '外网资源']
		# return titlelist

# driver = BaseDriver.getdriver()
# yi  = YinShiPinBusiness(driver)
# yi.yin_shipin_index("admin","111111")
#











