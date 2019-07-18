#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.logg import LoggIn

lo = LoggIn()

from selenium import webdriver
lo.logg_out("打开浏览器")
dr = webdriver.Chrome()
lo.logg_out("打开百度")
dr.get("http:www.baidu.com")















