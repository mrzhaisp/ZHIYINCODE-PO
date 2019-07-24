#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Basepage.persons_bank_page import PersonsBankPage

class PersonsBankHandle:
	"""人物库操作层"""

	def __init__(self,driver):
		self.driver=driver
		self.pbp = PersonsBankPage(driver)

	def click_persion_bank(self):
		#点击人物库
		self.pbp.find_person_bank_ele().click()

	def get_famouspersion_text(self):
		#知名人物库
		return self.pbp.find_text_famousperson_ele().text

	def get_unknownpersion_text(self):
		#未知人物库
		return self.pbp.find_text_unknownperson_ele().text

	def input_person_name(self,value):
		#找到搜索框输入名字
		self.pbp.find_input_serarch_ele().send_keys(value)

	def click_search_btn_ele(self):
		#搜索按钮
		self.pbp.find_search_btn_ele().click()

	def get_famoussion_name_text(self):
		#拿到搜索后结果的名人的名称
		return self.pbp.find_text_searchperson_ele().text

	def get_china_name_text(self):
		#中文名称
		return self.pbp.find_text_ch_name_ele().text

	def get_forgin_name_text(self):
		#外文名
		return self.pbp.find_text_foreign_name_ele().text

	def get_university_name_text(self):
		#毕业学校
		return self.pbp.find_text_search_university_ele().text

	def get_homeaddres_text(self):
		#家乡
		return self.pbp.find_text_search_hometon().text

	def get_position_text(self):
		#职业
		return self.pbp.find_text_search_position().text

	def get_famous_gender_text(self):
		#性别
		return self.pbp.find_text_serch_gender_ele().text

	def get_famous_country_text(self):
		#国籍
		return self.pbp.find_text_serach_country_ele().text

	def get_famous_nation_text(self):
		#民族
		return self.pbp.find_text_search_nation_ele().text

	def get_famous_party_text(self):
		#党派
		return self.pbp.find_text_serach_party_ele().text

	def get_send_errorkeywords_text(self):
		#搜索不到此人的信息
		return self.pbp.find_send_errorkeywords_ele().text











