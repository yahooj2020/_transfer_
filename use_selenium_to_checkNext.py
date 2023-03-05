#!/usr/bin/env python
#-*-coding:utf8-*-
"""
分析Nginx等Web应用访问IP信息 并将其访问数量从大到小排序
"""
ip_list=[] #定义空列表 所有的访问IP放置在该列表中
ip_count={}#定义一个空字典 将IP和访问的次数放置到该字典中



import copy
import re
import json
import time

import requests
from lxml import etree
import datetime
import csv
import copy
import re
import json
import time
from lxml import etree
from selenium import webdriver
import csv
import os
import os
ch_options = webdriver.ChromeOptions()
# 为Chrome配置无头模式


# 在启动浏览器时加入配置   Lib-argparse.py  Lib-image.py.html
driver = webdriver.Chrome(options=ch_options)
url ="http://127.0.0.1:8888/detail/docker-ce-cobra_test.go.html"
ignore_list= ["argparse.py","image.py"]
driver.get(url)
while True:

    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/a[2]').click()





