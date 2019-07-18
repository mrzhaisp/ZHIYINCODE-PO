#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import os,time,datetime
# report_dir = '../Reporter/'
# allreports = os.listdir(report_dir)
# # print(allreports)
# allreports.sort(
# 				key=lambda
# 					fn: os.path.getatime(report_dir+'/'+fn)
# 					if not os.path.isdir(report_dir+'/'+fn)
# 					else 0
# 				)
# newfile = os.path.join(report_dir,allreports[-1])
# print(newfile)
# from Commonlib.send_email import SendEmail
# s = SendEmail()
# s.send_mail("../Reporter/151_selenium_UI_report.htm")
#
