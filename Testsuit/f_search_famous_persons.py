#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Bussiness.persons_bank_business import PersonsBankBusiness
from Commonlib.base_driver import BaseDriver
from Commonlib.logg import LoggIn
from Commonlib.commonlib import Commonlib
from Page.Bussiness.login_bussiness import LoginBussiness
from parameterized import parameterized,param
import unittest

def bulid_data():
	return [
		("admin","111111","金正恩",True),
		("admin","111111","阿勒沙特",True),
		("admin","111111","@！#￥！@#@！#！",False),
		("admin","111111","AAAAABBBB",False)
	]


class SearchFamousPersonsInfo(unittest.TestCase):
	"""名人详细信息"""
	def setUp(self) -> None:
		self.lo = LoggIn()
		driver = BaseDriver.getdriver()
		self.c = Commonlib(driver)
		self.c.solv_log_waring()
		self.pbb = PersonsBankBusiness(driver)
		self.lgin = LoginBussiness(driver)

	def tearDown(self) -> None:
		pass

	@parameterized.expand(bulid_data)
	def test_get_famousperson_info(self,username,pwd,value,is_sucess):
		"""拿到著名人物的信息"""
		try:
			self.lgin.logoin(username,pwd)
			self.pbb.search_name_person(value)
			if is_sucess:
				search_list = []
				search_name = self.pbb.pbh.get_famoussion_name_text()
				search_list.append(search_name)
				search_china_name = self.pbb.pbh.get_china_name_text()
				search_list.append(search_china_name)
				search_foreign_name = self.pbb.pbh.get_forgin_name_text()
				search_list.append(search_foreign_name)
				search_gender = self.pbb.pbh.get_famous_gender_text()
				search_list.append(search_gender)
				search_nation = self.pbb.pbh.get_famous_nation_text()
				search_list.append(search_nation)
				search_party = self.pbb.pbh.get_famous_party_text()
				search_list.append(search_party)
				search_university = self.pbb.pbh.get_university_name_text()
				search_list.append(search_university)
				search_homeaddr = self.pbb.pbh.get_homeaddres_text()
				search_list.append(search_homeaddr)
				search_persion = self.pbb.pbh.get_position_text()
				search_list.append(search_persion)


				# self.assertEqual(expect,search_list)
				print("输入搜索值为---->%s，搜索到结果为%s" %(value,search_list))
			else:
				error_info = self.pbb.pbh.get_send_errorkeywords_text()
				print("输入搜索值---->%s后搜索到结果为--->%s" %(value ,error_info))

		except Exception as e:
			self.lo.logg_out(e)
			self.c.get_screen_shot("test_get_famousperson_info")

if __name__ == '__main__':
    unittest.main()



















