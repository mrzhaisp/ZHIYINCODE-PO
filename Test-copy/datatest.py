#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.read_json import BulidDat

buliddata = BulidDat("../Data/c_upload_video.json")
def bulid_data():
	listone = []
	datalist = buliddata.get_value("username","pwd","is_sucess")
	# print(datalist)
	for i in datalist:
		# print(type(i),tuple(i))
		listone.append(tuple(i))
	print(type(listone),'---------',listone)
	return datalist
bulid_data()