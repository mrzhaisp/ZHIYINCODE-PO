#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized,param
from Commonlib.commonlib import Commonlib
from Commonlib.base_driver import BaseDriver
from Page.Bussiness.login_bussiness import LoginBussiness
from Commonlib.read_json import BulidDat

buliddata = BulidDat("../Data/login_data.json")
def bulid_data():
	"""定义读取json数据应用到测试案例里"""
	datas = buliddata.get_value("username","pwd","expect","is_sucess")
	return datas


class LoginTest(unittest.TestCase):
	"""登录测试案例正例反例"""
	def setUp(self) -> None:
		self.dr = BaseDriver().getdriver()
		self.common = Commonlib(self.dr)
		self.businesslogin = LoginBussiness(self.dr)

	def tearDown(self) -> None:
		self.common.wait_time(2)
		self.common.quit_broswer()

	@parameterized.expand(bulid_data)
	def test_login(self,username,pwd,expect,is_sucess):
		"""登录正例和反例  登录成功，拿到"声像情报融合分析平台"，不成功则停留在主页 '声像情报分析系统'"""
		self.businesslogin.logoin(username,pwd)
		if is_sucess:
			"""登录成功就返回主页信息"""
			text = self.businesslogin.loghandle.login_sucess_text()
			print("登录成功后进入主页面，主页面标题为---->%s"%text)
			return text
			#断言  "声像情报融合分析平台"
			self.assertEqual(text,expect )
		else:
			# """登录失败，就停在登录主页"""
			texttwo = self.businesslogin.loghandle.login_fail_text()
			print("密码错误登录失败停留在登录页面文字为--->%s"%texttwo)
			return texttwo
			#断言    "声像情报分析系统"
			self.assertEqual(texttwo,expect)

if __name__ == '__main__':
	unittest.main()
