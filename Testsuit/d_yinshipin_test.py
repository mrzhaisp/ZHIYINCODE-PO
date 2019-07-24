#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.commonlib import Commonlib
from Commonlib.base_driver import BaseDriver
from Commonlib.logg import LoggIn
from Page.Bussiness.yinshipin_bussiness import YinShiPinBusiness
from parameterized import parameterized,param
from Commonlib.read_json import BulidDat
import unittest

# def bulid_data():
# 	return [
# 		("admin","111111","['时事热点', '内网自编', '外网资源', '外网资源']",True)
# 	]

buliddata = BulidDat("../Data/d_yinshipin.json")
def bulid_data():
	datalist  = buliddata.get_value("username","pwd","expect","is_sucess")
	return datalist

class YinShiPinTest(unittest.TestCase):
	"""点击音视频栏目，拿到下面子栏目的title"""
	def setUp(self) -> None:
		self.lo = LoggIn()
		driver = BaseDriver().getdriver()
		self.c = Commonlib(driver)
		self.c.solv_log_waring()
		self.b = YinShiPinBusiness(driver)

	def tearDown(self) -> None:
		self.c.wait_time(2)
		self.c.quit_broswer()

	@parameterized.expand(bulid_data)
	def test_yinshi_colum(self,username,pwd,expect,is_sucess):
		"""拿到音视频下的子栏目的三个值"""
		try:
			if is_sucess:
				titlelist = []
				self.b.yin_shipin_index(username,pwd)

				text_shishiredian = self.b.yinsp.text_shisrd_title()
				titlelist.append(text_shishiredian)

				text_neiwangzibian = self.b.yinsp.text_neiwzb_title()
				titlelist.append(text_neiwangzibian)

				text_waiwangziyuan = self.b.yinsp.text_waiwang_title()
				titlelist.append(text_waiwangziyuan)

				text_guanzhu = self.b.yinsp.text_wodeguanzhu_title()
				titlelist.append(text_guanzhu)

				self.assertEqual(titlelist,expect)
				print("点击音视频库后下子栏目为---->%s"%titlelist)
				return titlelist


		except Exception as e:
			self.lo.logg_out(e)
			self.c.get_screen_shot("test_yinshi_colum")

if __name__ == '__main__':
    unittest.main()












