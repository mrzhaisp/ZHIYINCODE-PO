#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os,sys
import time as t
from Commonlib.logg import LoggIn
from Commonlib.create_reporter import CreateReporter
from Commonlib.send_email import SendEmail
from Commonlib.find_new_file import FindNewFile
createrport = CreateReporter()
logout = LoggIn()
send_to_email = SendEmail()
find_newfile = FindNewFile()

class RunallCase(unittest.TestCase):

	def discover_case_to_createrrepo(self):
		# 测试案例的路径
		case_dir = '../Testsuit/'
		discover = unittest.defaultTestLoader.discover(case_dir, pattern="*.py", top_level_dir=None)
		# 所有的案例传给createreport
		# print(discover)
		logout.logg_out("生成测试报告存入%s"%case_dir)
		createrport.createreport(discover)

		report_file = find_newfile.find_file("../Repoter/")
		logout.logg_out("发送最新报告文件为-->%s"%report_file)
		send_to_email.send_mail(report_file)

		for i in range(100):
			k = i + 1
			str = '/' * i + '' * (100 - k)
			sys.stdout.write('\r' + str + '[%s%%]' % (i + 1))
			sys.stdout.flush()
			t.sleep(0.05)
		print(u"Emal send----->%100")
		logout.logg_out("测试跑完一圈，测试报告邮件发送完毕")
	# def runTest(self):
	# 	# 原因是因为sub_class里缺少runTest方法，不加上该方法，上边的tetsT会报错，直接在Tsuit的类中增加
	# 	pass

r = RunallCase()
r.discover_case_to_createrrepo()

