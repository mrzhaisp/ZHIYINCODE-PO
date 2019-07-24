#!/usr/bin/env python
# -*- coding: utf-8 -*-
class PersonsBankPage:
	"""登录后查看人物库Page"""

	def __init__(self,driver ):
		self.driver = driver


	def find_person_bank_ele(self):
		#人物库按钮
		# return self.driver.find_element_by_xpath(".//body/descendant::a[3]")
		return self.driver.find_element_by_xpath(".//body/descendant::a[2]")

	def find_text_famousperson_ele(self):
		"""知名人物"""
		return self.driver.find_element_by_xpath(".//section/descendant::h2[1]")

	def find_text_unknownperson_ele(self):
		'''未知人物'''
		return self.driver.find_element_by_xpath(".//section/descendant::h2[2]")

	def  find_input_serarch_ele(self):
		#输入知名人物的名称
		return self.driver.find_element_by_xpath(".//section/descendant::input")

	def find_search_btn_ele(self):
		"""搜索按钮"""
		return self.driver.find_element_by_xpath(".//section/descendant::input/following-sibling::div")

	def find_text_searchperson_ele(self):
		#找到知名人物的名称"""
		return self.driver.find_element_by_xpath(".//section/descendant::h3[1]")

	def find_text_ch_name_ele(self):
		#中文名称
		return self.driver.find_element_by_xpath(".//section/descendant::p[1]")

	def find_text_foreign_name_ele(self):
		#外文名称
		return self.driver.find_element_by_xpath(".//section/descendant::p[2]")

	def find_text_serch_gender_ele(self):
		#性别
		return  self.driver.find_element_by_xpath(".//section/descendant::p[4]")

	def find_text_serach_country_ele(self):
		#国籍
		return self.driver.find_element_by_xpath(".//section/descendant::p[8]")

	def find_text_search_nation_ele(self):
		#民族
		return self.driver.find_element_by_xpath(".//section/descendant::p[5]")

	def find_text_serach_party_ele(self):
		#党派
		return self.driver.find_element_by_xpath(".//section/descendant::p[9]")

	def find_text_search_university_ele(self):
		#学校
		return self.driver.find_element_by_xpath(".//section/descendant::p[6]")

	def find_text_search_hometon(self):
		#家庭住址
		return self.driver.find_element_by_xpath(".//section/descendant::p[9]")

	def find_text_search_position(self):
		#职业
		return self.driver.find_element_by_xpath(".//section/descendant::p[9]")

	def find_send_errorkeywords_ele(self):
		#输入特殊值搜索出来的结果的信息
		return self.driver.find_element_by_xpath(".//section/descendant::p")