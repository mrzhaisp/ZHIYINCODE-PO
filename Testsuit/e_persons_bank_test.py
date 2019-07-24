#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Page.Bussiness.persons_bank_business import PersonsBankBusiness
from Page.Bussiness.login_bussiness import LoginBussiness
from Commonlib.base_driver import BaseDriver
from Commonlib.logg import LoggIn
from Commonlib.commonlib import Commonlib
from parameterized import parameterized,param
from Commonlib.read_json import BulidDat
# def bulid_data():
# 	return [
# 		("admin","111111","['知名人物','未知人物a']",True)

builddata = BulidDat("../Data/e_character_bank_test.json")
def bulid_data():
	datalist = builddata.get_value("username","pwd","expect","is_sucess")
	return datalist

class PersonsBank(unittest.TestCase):
	"""登录系统切换到人物库"""

	def setUp(self) -> None:
		self.lo = LoggIn()
		driver = BaseDriver().getdriver()
		self.c = Commonlib(driver)
		self.c.solv_log_waring()
		self.pbb = PersonsBankBusiness(driver)
		self.lob = LoginBussiness(driver)

	def tearDown(self) -> None:
		pass

	@parameterized.expand(bulid_data)
	def test_person_colum(self,username,pwd,expect,is_sucess):
		try:
			if is_sucess:
				text_list = []
				self.lob.logoin(username,pwd)
				self.pbb.person_index()
				famous_text = self.pbb.pbh.get_famouspersion_text()
				text_list.append(famous_text)
				unknow_text = self.pbb.pbh.get_unknownpersion_text()
				text_list.append(unknow_text)
				print("生成列表为---->%s"%text_list)
				self.assertEqual(text_list,expect)
				return text_list
		except Exception as e:
			self.lo.logg_out(e)
			self.c.get_screen_shot("test_person_colum")

if __name__ == '__main__':
    unittest.main()













