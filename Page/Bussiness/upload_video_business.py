#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.base_driver import BaseDriver
from Commonlib.commonlib import Commonlib
from Page.Handle.upload_video_handle import UpLoadVideoHandle
from Commonlib.logg import LoggIn
from Page.Bussiness.load_video_bussiness import LoadVideoBussiness
import os,random


#本地视频列表，
videolist = ["seleniumtest1.mp4","selenium--ParagGupta.mp4","selenium--Markhampionship2018.mp4","selenium--Initiativesety.mp4","selenium--Decision.mp4",
             "seleniumCures-Faster.mp4","selenium--CSCI262-IDS).mp4","selenium--Blockc2.mp4","selenium--BigNetworks.mp4","selenium-AWS.mp4","selenium001BitoinDoneCrE.mp4"]

#本地的路径
filepath = r"C:\Users\Test\loadvideofile\selenium"
filepathone = r"C:\Users\Test\ruanjian\Autoitupload-filr\upload.exe"

class UpLoadVideoBusiness:
	"""上传视频业务层"""

	def __init__(self,driver):
		# self.basedriver = BaseDriver()
		# driver = self.basedriver.getdriver()
		self.lo = LoggIn()
		self.common = Commonlib(driver)
		self.loginbusi = LoadVideoBussiness(driver)
		self.upldhandle = UpLoadVideoHandle(driver)

	def up_load_video(self,username,pwd):
		"""登录后台"""
		self.lo.logg_out("打开浏览器，登录后台上传视频")
		self.loginbusi.loadvideologin(username,pwd)
		self.common.wait_time(3)
		#点击导入视频按钮
		self.upldhandle.click_loadvideo_btn()
		self.lo.logg_out("点击上传视频")
		self.upldhandle.click_choice_video()
		self.common.wait_time(2)

	def up_load_erroe_type_video(self):
		# 上传不正确的视频格式，
		# 非input标签，第三方工具制作参数   +   上传文件的路径
		self.lo.logg_out("加载上传视频路径")
		os.system(r"C:\Users\Test\ruanjian\Autoitupload-filr\upload.exe %s" % filepathone)
		self.common.wait_time(2)
		# loadvideo_fail_text = self.upldhandle.get_fiali_upload_video_text()
		# print(failtext)

	def up_load_sucess_type_video(self):
		"""上传正确的视频格式"""
		videoname = random.choice(videolist)
		allpath = filepath + '\\' +videoname
		#第三方上传视频工具  + 正常视频上传路径
		os.system(r"C:\Users\Test\ruanjian\Autoitupload-filr\upload.exe  %s" %allpath)
		self.common.wait_time(2)

		LoggIn.logg_out("选择外网资源")
		self.upldhandle.click_waiwang_btn()

		LoggIn.logg_out("选择频道分类")
		self.common.wait_time(2)
		self.upldhandle.click_pindao_btn()

		LoggIn.logg_out("随机选取一个栏目--人工智能、电子对抗、区块链")
		self.common.wait_time(3)
		self.upldhandle.click_fenlei_lanmu()

		LoggIn.logg_out("选择语言栏目")
		self.common.wait_time(2)
		self.upldhandle.click_langue_btn()

		LoggIn.logg_out("随机选择语言")
		self.common.wait_time(2)
		self.upldhandle.click_choice_langue_btn()

		LoggIn.logg_out("清除制作日期，重新输入当期日期")
		self.common.wait_time(2)
		self.upldhandle.clear_make_data_btn()
		self.common.wait_time(2)
		self.upldhandle.send_make_data_btn()
		self.common.wait_time(1)
		self.upldhandle.click_index()

		LoggIn.logg_out("清除上传日期，重新上传当天日期")
		self.common.wait_time(2)
		self.upldhandle.clear_upload_data()
		self.common.wait_time(2)
		self.upldhandle.send_upload_data_btn()
		self.upldhandle.click_index()

		LoggIn.logg_out("点击index首页切换,点击摘要输入框，输入内容摘要")
		self.common.wait_time(2)
		self.upldhandle.click_index()
		self.common.wait_time(2)
		self.upldhandle.click_index()
		self.upldhandle.input_content()

		LoggIn.logg_out("导入视频按钮")
		self.common.wait_time(2)
		self.upldhandle.import_video_btn()

		LoggIn.logg_out("关闭上传视频弹窗按钮")
		self.common.wait_time(2)
		self.upldhandle.click_alter_ele()

		#查看处理过程按钮
		self.common.wait_time(2)
		self.upldhandle.click_sucess_process()

		LoggIn.logg_out("视频上传完毕")
		self.common.wait_time(2)
		# loadvideo_sucess_text = self.upldhandle.get_sucess_upload_video_text()
		# print(loadvideo_sucess_text)

# driver = BaseDriver().getdriver()
# ub = UpLoadVideoBusiness(driver)
# ub.up_load_video("admin","111111")
# ub.up_load_erroe_type_video()
#











