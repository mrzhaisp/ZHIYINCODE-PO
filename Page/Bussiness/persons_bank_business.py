#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Handle.persons_bank_handle import PersonsBankHandle
from Commonlib.logg import LoggIn
from Page.Bussiness.login_bussiness import LoginBussiness
from Commonlib.commonlib import Commonlib
from Commonlib.base_driver import BaseDriver

class PersonsBankBusiness:
	"""人物库业务层"""

	def __init__(self,driver):
		# self.driver = driver
		self.lo = LoggIn()
		self.c = Commonlib(driver)
		self.login = LoginBussiness(driver)   #登录
		self.pbh = PersonsBankHandle(driver)

	def  person_index(self):
		"""切换到人物库"""
		# self.login.logoin("admin","111111")
		self.lo.logg_out("点击人物库，切换到人物库首页,")
		self.pbh.click_persion_bank()
		self.c.wait_time(2)

	def search_name_person(self,value):
		#输入名称，搜索知名人物
		# search_list = []
		self.person_index()
		self.pbh.input_person_name(value)
		self.c.wait_time(5)
		self.pbh.click_search_btn_ele()
		self.c.wait_time(5)

		# #拿到搜索到的人物详细页的名称
		# search_name = self.pbh.get_famoussion_name_text()
		# search_list.append(search_name)
		# search_china_name = self.pbh.get_china_name_text()
		# search_list.append(search_china_name)
		# search_gender = self.pbh.get_famous_gender_text()
		# search_list.append(search_gender)
		# search_nation = self.pbh.get_famous_nation_text()
		# search_list.append(search_nation)
		# search_party = self.pbh.get_famous_party_text()
		# search_list.append(search_party)
		# print(search_list)

		# famous_text = self.pbh.get_famouspersion_text()
		# print(famous_text)   #知名人物
		#
		#
		# unknow_text = self.pbh.get_unknownpersion_text()
		# print(unknow_text)   #未知人物
# driver = BaseDriver().getdriver()
# pb = PersonsBankBusiness(driver)
# pb.search_name_person("特朗普")












