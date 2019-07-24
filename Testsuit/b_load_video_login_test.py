#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.base_driver import BaseDriver
from Commonlib.commonlib import Commonlib
from Page.Bussiness.load_video_bussiness import LoadVideoBussiness
from parameterized import parameterized
from Commonlib.logg import LoggIn
from Commonlib.read_json import BulidDat
import unittest
# def bulid_data():
# 	return [
# 		("admin","111111","视频管理",True),
# 		("admin","11223344","声像情报分析系统",False),
# 	]
buliddata = BulidDat("../Data/b_load_video_login_test.json")
def bulid_data():
	"""读取json数据"""
	datalist = buliddata.get_value("username","pwd","expect","is_sucess")
	return datalist

class LoadVideoLogin(unittest.TestCase):
	"""登录上传视频的正反例"""
	def setUp(self):
		self.dr = BaseDriver().getdriver()
		self.c = Commonlib(self.dr)
		self.b= LoadVideoBussiness(self.dr)

	def tearDown(self):
		self.c.wait_time(2)
		self.c.quit_broswer()

	@parameterized.expand(bulid_data)
	def test_load_video_login(self,username,pwd,expect,is_sucess):
		"""登录成功拿到页面文字' 视频管理',登录失败停留在登录页面拿到文字‘声像情报分析系统’"""
		try:
			LoggIn.logg_out("准备登录上传视频登录页面")
			self.b.loadvideologin(username,pwd)
			if is_sucess:
				textsucess = self.b.loginhandle.log_sucess_text()
				print("登录成功后断言为------>%s"%textsucess)
				return textsucess
				#断言，"视频管理"
				self.assertEqual(textsucess,expect)
			else:
				# textfail = self.busi_loadvd_login.loginhandle.login_fail_text()
				textfail = self.b.loginhandle.login_fail_text()
				print("登录失败后停留在登录页面断言为---->%s"%textfail)
				self.assertEqual(textfail,expect)
				return textfail
				#断言  “声像情报分析系统”
		except Exception as e:
			self.c.get_screen_shot("test_load_video_login")
			print(e)

if __name__ == '__main__':
    unittest.main()