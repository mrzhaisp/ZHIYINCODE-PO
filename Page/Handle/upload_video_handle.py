#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Basepage.upload_video_page import UploadVideoPage
import time,datetime

class UpLoadVideoHandle:
	"""上传视频的操作层"""
	def __init__(self,driver):
		self.uplo = UploadVideoPage(driver)

	def click_index(self):
		"""点击空白页"""
		self.uplo.find_index_ele().click()

	def click_loadvideo_btn(self):
		"""点击导入视频按钮"""
		self.uplo.find_upload_btn_ele().click()

	def click_choice_video(self):
		"""上传视频选择文件"""
		self.uplo.find_video_file_ele().click()

	def click_neiwang_btn(self):
		"""选择内网"""
		self.uplo.find_neiwang_source_ele().click()

	def click_waiwang_btn(self):
		"""选择外网"""
		self.uplo.find_waiwang_source_ele().click()

	def click_pindao_btn(self):
		""""选择频道分类"""
		self.uplo.find_pindao_type().click()

	def click_fenlei_lanmu(self):
		"""随机选取一个栏目--人工智能、电子对抗、区块链"""
		element_text = self.uplo.find_fenlei_ele()
		# self.uplo.find_fenlei_ele().click()
		element_text.click()


	def click_langue_btn(self):
		"""点击语言栏目"""
		self.uplo.find_langue_ele().click()

	def click_choice_langue_btn(self):
		"""随机选择一个语言"""
		self.uplo.find_choice_langue_ele().click()

	def clear_make_data_btn(self):
		"""清除制作日期"""
		self.uplo.find_makedate_ele().clear()

	def send_make_data_btn(self):
		"""输入制作日期"""
		self.uplo.find_makedate_ele().send_keys(str(datetime.date.today()))

	def clear_upload_data(self):
		"""清除上传日期"""
		self.uplo.find_upload_ele().click()

	def send_upload_data_btn(self):
		"""输入上传日期"""
		self.uplo.find_upload_ele().send_keys(str(datetime.date.today()))

	def input_content(self):
		self.uplo.find_content_ele().send_keys("这是一个selenium自动化测试")

	def import_video_btn(self):
		"""视频导入按钮"""
		self.uplo.find_import_video_ele().click()

	def click_alter_ele(self):
		"""上传视频后提示框确定按钮"""
		self.uplo.find_alter_ele().click()

	def click_sucess_process(self):
		""""查看处理过程按钮"""
		self.uplo.find_sucess_process_ele().click()

	def get_sucess_upload_video_text(self):
		"""视频上传完成后 拿到过程   本地上传"""
		for i in range(10):
			try:
				textone = self.uplo.find_import_text_ele().text
				return textone
			except:pass
			time.sleep(1)

	def get_fiali_upload_video_text(self):
		"""视频上传格式不正确后弹出框里的文字"""
		for i in range(10):
			try:
				texttwo = self.uplo.find_video_error_text().text
				return texttwo
			except:pass
			time.sleep(1)






