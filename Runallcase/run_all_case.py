#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os,sys,time
from Commonlib.logg import LoggIn
from Commonlib.create_reporter import CreateReporter
from Commonlib.send_email import SendEmail
# createrport = CreateReporter()
logout = LoggIn()
sendtoemail = SendEmail()

class RunallCase(unittest.TestCase):

	def discover_case_to_createrrepo(self):
		# 测试案例的路径
		case_dir = '../Testsuit/'
		discover = unittest.defaultTestLoader.discover(case_dir, pattern="*.py", top_level_dir=None)
		# 所有的案例传给createreport
		# print(discover)
		CreateReporter.createreport(discover)
		logout.logg_out("生成测试报告存入%s"%case_dir)
		#发送测试报告
		# sendtoemail.sendEmail("../Reporter/151_selenium_UI_report.htm")
		# for i in range(100):
		# 	k = i + 1
		# 	str = '/' * i + '' * (100 - k)
		# 	sys.stdout.write('\r' + str + '[%s%%]' % (i + 1))
		# 	sys.stdout.flush()
		# 	time.sleep(0.05)
		# logout.logg_out("发送测试报告邮件！已完成")
		# print(u"Emal send----->%100")

	def runTest(self):
		# 原因是因为sub_class里缺少runTest方法，不加上该方法，上边的tetsT会报错，直接在Tsuit的类中增加
		pass

r = RunallCase()
r.discover_case_to_createrrepo()

