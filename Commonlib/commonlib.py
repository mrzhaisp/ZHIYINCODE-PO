#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as t
class Commonlib:
	def __init__(self,driver):
		self.driver = driver

	def get_screen_shot(self,value):
		"""异常截图"""
		self.driver.get_screenshot_as_file(value)

	def close_alert(self):
		"""关闭弹框"""
		alter = self.driver.switch_to.alter
		msg = alter.text
		alter.accept()
		return msg

	def quit_broswer(self):
		"""关闭浏览器"""
		self.driver.quit()

	def wait_time(self,value):
		"""等待"""
		t.sleep(value)

	def move_element(self,value):
		"""移动到某个元素不做操作"""
		self.driver.find_element_by_xpath(value)


	def move_to_keywords(self,value):
		"""全屏寻找关键字，移动到关键字这里"""
		for i in range(10):
			try:
				target = self.driver.find_element_by_xpath(value)
				self.driver.execute_script("arguments[0].scrollIntoView();", target)
				break
			except:pass
			t.sleep(1)










