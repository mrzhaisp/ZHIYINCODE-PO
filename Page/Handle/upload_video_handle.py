#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Basepage.upload_video_page import UploadVideoPage

class UpLoadVideoHandle:
	def __init__(self):
		self.uplo = UploadVideoPage()

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

	def click_feilei_lanmu(self):
		"""随机选取一个栏目--人工智能、电子对抗、区块链"""
		self.uplo.find_fenlei_ele().click()

	def click_choice_langue_btn(self):
		"""点击语言栏目"""
		self.uplo.find_langue_ele().click()

	def click_langue_btn(self):
		"""选择一个语言"""
		self.uplo.find_choice_landue_ele().click()





















