#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time as t

class LoggIn:
	"""输出日志内容"""
	@classmethod
	def logg_out(self, logincontent):
		"""输出日志的类"""
		# 定义文件
		# logFile = logging.FileHandler(r"ZHIYINCODE-PO/Logs/system.log", 'a', encoding='utf-8')
		logFile = logging.FileHandler("C:\\Users\\Test\\ZHIYINCODE-PO\\Logs\\system.log", 'a', encoding='utf-8')

		# log格式
		fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
		logFile.setFormatter(fmt)

		# 定义log
		logger1 = logging.Logger('logTest', level=logging.DEBUG)
		logger1.addHandler(logFile)
		logger1.info(logincontent)
