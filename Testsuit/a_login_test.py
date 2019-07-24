#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized,param
from Commonlib.commonlib import Commonlib
from Commonlib.logg import LoggIn
from Commonlib.base_driver import BaseDriver
from Page.Bussiness.login_bussiness import LoginBussiness
from Commonlib.read_json import BulidDat

buliddata = BulidDat("../Data/a_login_test.json")
def bulid_data():
	"""定义读取json数据应用到测试案例里"""
	datas = buliddata.get_value("username","pwd","expect","is_sucess")
	return datas

# def bulid_data():
# 	return [
# 		("admin","111111","声像情报融合分析平台",True),
# 		("admin","11223344","声像情报分析系统",False),
# 	]

class LoginTest(unittest.TestCase):
	"""登录测试案例正例反例"""
	def setUp(self) -> None:
		self.dr = BaseDriver().getdriver()
		self.common = Commonlib(self.dr)
		self.lo = LoggIn()
		self.lo.logg_out("------------->打开浏览器运行--%s--这个类"%LoginTest)
		self.common.solv_log_waring()
		self.businesslogin = LoginBussiness(self.dr)

	def tearDown(self) -> None:
		self.common.wait_time(5)
		self.common.quit_broswer()
		self.lo.logg_out(">-----------关闭浏览器")

	@parameterized.expand(bulid_data)
	def test_login(self,username,pwd,expect,is_sucess):
		"""登录"知音晓视"正例和反例  登录成功，拿到"声像情报融合分析平台"，不成功则停留在主页 '声像情报分析系统'"""
		try:
			self.businesslogin.logoin(username,pwd)
			if is_sucess:
				"""登录成功就返回主页信息"""
				text = self.businesslogin.loghandle.login_sucess_text()
				self.lo.logg_out("登录成功后进入主页面，主页面标题为---->%s"%text)
				print("登录成功后进入主页面，主页面标题为---->%s"%text)
				self.assertEqual(text,expect )
				return text
				#断言  "声像情报融合分析平台"
			else:
				# """登录失败，就停在登录主页"""
				texttwo = self.businesslogin.loghandle.login_fail_text()
				self.lo.logg_out("密码错误登录失败停留在登录页面文字为--->%s"%texttwo)
				print("密码错误登录失败停留在登录页面文字为--->%s"%texttwo)
				self.assertEqual(texttwo,expect)
				return texttwo
				#断言    "声像情报分析系统"
		except Exception  as e:
			self.common.get_screen_shot("test_login")

if __name__ == '__main__':
	unittest.main()
