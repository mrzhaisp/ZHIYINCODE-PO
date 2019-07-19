#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as t
import warnings


class Commonlib:
	"""定义工具类"""

	def __init__(self, driver):
		self.driver = driver

	def open_browser(self,myurl):
		"""打开浏览器最大化浏览器"""
		self.driver.get(myurl)
		self.driver.maximize_window()

	
	def get_screen_shot(self, value):
		"""异常截图"""
		nowtime = t.strftime("%Y%m%d.%H.%M.%S")
		# pictfile = "C:\\Users\\Test\\ErrorPict"
		pictfile = '../Errorpict/'
		pictname = nowtime + '--' + value + '.png'
		allname = pictfile + pictname
		self.driver.get_screenshot_as_file(allname)

	
	def solv_log_waring(self):
		"""输出日志后未关闭文件，报异常，只需要在此类初始化的时候调用该方法"""
		warnings.simplefilter("ignore", ResourceWarning)

	
	def close_alert(self):
		"""关闭弹框"""
		alter = self.driver.switch_to.alter
		msg = alter.text
		alter.accept()
		return msg

	def quit_broswer(self):
		"""关闭浏览器"""
		self.driver.quit()

	def wait_time(self, value):
		"""等待"""
		t.sleep(value)

	
	def move_element(self, value):
		"""移动到某个元素不做操作"""
		self.driver.find_element_by_xpath(value)

	
	def move_to_keywords(self, value):
		"""全屏寻找关键字，移动到关键字这里"""
		for i in range(10):
			try:
				target = self.driver.find_element_by_xpath(value)
				self.driver.execute_script("arguments[0].scrollIntoView();", target)
				break
			except:
				pass
			t.sleep(1)
