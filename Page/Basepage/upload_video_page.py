#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

#视频分类列表
videosourse = ["人工智能", "电子对抗", "下一代网络", "智能制造", "区块链", "其他"]

#语言列表
langue = ["中文", "英语", "日语", "俄语", "法语", "德语", "越南语",
          "意大利语", "丹麦语", "汉语", "韩语", "瑞典语", "芬兰语",
          "波兰语", "荷兰语", "泰语", "阿拉伯语", "捷克语", "罗马尼亚语", "匈牙利语", "其他"]

class UploadVideoPage:
	"""上传视频的页面"""
	def __init__(self):
		self.driver = driver

	def find_upload_btn_ele(self):
		"""登录后台，导入视频的按钮"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'导入视频')]")

	def find_video_file_ele(self):
		"""上传视频选择文件"""
		return self.driver.find_element_by_xpath(".//body/descendant::input[1]")

	def find_neiwang_source_ele(self):
		"""内网自编按钮"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'内网自编')]")

	def find_waiwang_source_ele(self):
		"""外网资源"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'外网资源')]")

	def find_pindao_type(self):
		"""频道分类按钮"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'频道分类')]/following-sibling::div/descendant::input")

	def find_fenlei_ele(self):
		"""随机选取一个栏目--人工智能、电子对抗、区块链"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'%s')]" % random.choice(videosourse))

	def find_langue_ele(self):
		"""点击选取语言"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'语种')]/following-sibling::div/descendant::input")

	def find_choice_landue_ele(self):
		"""随机选取一种语言"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'%s')]" % random.choice(langue))

	def find_makedate_ele(self):
		"""制作日期栏"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'制作日期')]/following-sibling::div/descendant::input")

	def find_upload_ele(self):
		"""上传日期"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'上传日期')]/following-sibling::div/descendant::input")

	def find_kongbai_ele(self):
		"""空白处，输入完日期后点击空白处"""
		return self.driver.find_element_by_xpath(".//*[@class='video-import']")

	def find_content_ele(self):
		"""内容摘要输入框"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'内容摘要')]/following-sibling::div/descendant::textarea")

	def find_import_video_ele(self):
		"""导入按钮"""
		return self.driver.find_element_by_xpath(".//*[text()='导入']")

	def find_alter_ele_ele(self):
		"""上传视频后提示框确定按钮"""
		return self.driver.find_element_by_xpath(".//body/descendant::span[35]/descendant::span")

	def find_sucess_process_ele(self):
		""""查看处理过程按钮"""
		return self.driver.find_element_by_xpath(".//*[contains(text(),'查看处理过程')]")

	def find_import_text_ele(self):
		"""视频上传完成后 拿到过程   本地上传"""
		return self.driver.find_element_by_xpath(".//*[text()='本地上传']")

	def find_videotype_error_ele(self):
		"""视频上传格式不正确弹框"""
		return self.driver.find_element_by_xpath(".//body/descendant::input[1]")

	def find_video_error_text(self):
		"""视频上传格式不正确后弹出框里的文字"""
		return self.driver.find_element_by_xpath(".//body/div[2]/descendant::p")





















