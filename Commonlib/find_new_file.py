#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# from Commonlib.send_email import SendEmail
# s = SendEmail()
class FindNewFile:
	@classmethod
	def find_file(self,file_path_dir):
		report_dir = file_path_dir
		allreports = os.listdir(report_dir)
		# print

		allreports.sort(
							key=lambda
								fn: os.path.getatime(report_dir + '/' + fn)
							if not os.path.isdir(report_dir + '/' + fn)
							else 0
		)
		newfile = os.path.join(report_dir,allreports[-1])
		print(newfile)
		return newfile
