#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

class BulidDat:
	def __init__(self, file_path=None):
		if file_path == None:
			self.file_path = "../Data/login_data.jsons"
		else:
			self.file_path = file_path
		self.data = self.read_json()

	def read_json(self):
		"""得到所有json数据"""
		with open(self.file_path, encoding="utf-8") as f:
			data = json.load(f)
		return data

	def get_value(self, one=None, two=None, sec=None, fou=None):
		"""拿到所有的json数据"""
		resultlist = []
		for obj in self.data.values():
			resultlist.append((obj.get(one), obj.get(two), obj.get(sec), obj.get(fou)))
		return resultlist

