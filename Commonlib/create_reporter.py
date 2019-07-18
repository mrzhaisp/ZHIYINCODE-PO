#!/usr/bin/env python
# -*- coding: utf-8 -*-
import HTMLTestRunnerNew

class CreateReporter:
	"""制作测试报告"""
	def createreport(self,mysuit):
		filepath = "../Reporter/151_selenium_UI_report.htm"
		# pathname = "../Reporter/"
		# poretername = "151_selenium_UI_report.htm"
		# filepath = pathname+'__'+poretername
		with open(filepath,"wb") as f:
			HTMLTestRunnerNew.HTMLTestRunner(
				stream=f,
				verbosity=2,
				title="151--声像情报分析系统测试报告",
				description="声像情报分析系统UI自动化测试"
			).run(mysuit)




















