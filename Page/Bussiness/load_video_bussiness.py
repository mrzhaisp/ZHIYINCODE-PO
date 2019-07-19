#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commonlib.commonlib import Commonlib
from Page.Handle.load_video_handle import LoadVideoHandle
import time as t

class LoadVideoBussiness:
		"""创建视频上传的登录业务"""
		def __init__(self,driver):
			self.common = Commonlib(driver)
			self.loginhandle = LoadVideoHandle(driver)

		def loadvideologin(self,username,pwd):
			"""登录上传视频业务的代码"""
			self.common.open_browser("http://10.168.103.151/admin/#/")
			self.loginhandle.input_username(username)
			self.loginhandle.input_pwd(pwd)
			self.loginhandle.click_btn()
			t.sleep(3)



