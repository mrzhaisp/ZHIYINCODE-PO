#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.read_json import BulidDat
buliddata = BulidDat("../Data/a_login_test.json")
def bulid_data():
	"""定义读取json数据应用到测试案例里"""
	datas = buliddata.get_value("username","pwd","expect","is_sucess")
	print(datas)
	return datas

bulid_data()