#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Bussiness.upload_video_business import UpLoadVideoBusiness
from Commonlib.base_driver import BaseDriver
from Commonlib.commonlib import Commonlib
from Commonlib.logg import LoggIn
from parameterized import parameterized,param
from Commonlib.read_json import BulidDat
import unittest

# def bulid_data():
# 	return [
# 		("admin","111111","本地上传",True),
# 		("admin","111111","上传的视频必须是 MP4/AVI/MPG/WMV/3GP/MOV/ASF/ASX/FLV 格式 !",False)
# 	]

buliddata = BulidDat("../Data/c_upload_video.json")
def bulid_data():
	datalist = buliddata.get_value("username","pwd","expect","is_sucess")
	return datalist


class UpLoadVideoTest(unittest.TestCase):
	"""上传正常格式视频和非正常格式视频"""

	def setUp(self) -> None:
		self.lo = LoggIn()
		self.dr = BaseDriver().getdriver()
		self.c = Commonlib(self.dr)
		self.c.solv_log_waring()
		self.b = UpLoadVideoBusiness(self.dr)

	def tearDown(self) -> None:
		self.c.wait_time(20)
		self.c.quit_broswer()

	@parameterized.expand(bulid_data)
	def test_up_load_video_type(self,username,pwd,expect,is_sucess):
		try:
			self.b.up_load_video(username,pwd)
			if is_sucess:
				self.b.up_load_sucess_type_video()
				loadvideo_sucess_text = self.b.upldhandle.get_sucess_upload_video_text()
				return loadvideo_sucess_text
				#断言为---->本地上传
				self.lo.logg_out("视频上传完毕，上传页面text为---->%s"%loadvideo_sucess_text)
				self.assertEqual(loadvideo_sucess_text,expect)
			else:
				self.b.up_load_erroe_type_video()
				loadvideo_fail_text = self.b.upldhandle.get_fiali_upload_video_text()
				self.lo.logg_out("上传视频格式不正确，弹出弹框文字为--->%s"%loadvideo_fail_text)
				print("上传视频格式不正确，弹出弹框文字为--->%s"%loadvideo_fail_text)
				self.assertEqual(loadvideo_fail_text,expect)
				return loadvideo_fail_text

		except Exception as e:
			self.lo.logg_out(e)
			self.b.common.get_screen_shot("test_up_load_video_type")


if __name__ == '__main__':
    unittest.main()










