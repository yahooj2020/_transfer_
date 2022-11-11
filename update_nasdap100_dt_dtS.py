
# python3   update_nhk_news_Server.py

import scrapy
from scrapy_splash import SplashRequest
from urllib import parse
import json
import datetime
import time
import re
import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException

from selenium import webdriver


from retrying import retry
import os

big_list = []

json_file = "/home/mk_m/device/nasdap100_info.json"





def writeinto_jsonfile(filename, list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)

def readjsonfile(filename):
   with open(filename, 'r', encoding='utf-8') as fw:
      s = json.load(fw)
      return s
json_result = readjsonfile(json_file)

def us_only_list_func(result):
    seen = set()
    only_list = []
    for item in result:
        if item["code"] not in seen:
            only_list.append(item)
            seen.add(item["code"])
    type_dict = {}

    for item in only_list:
        if item["industry_infos"] not in type_dict:
            type_dict[item["industry_infos"]] = [item]
        else:
            type_dict[item["industry_infos"]].append(item)

    return only_list
def f_us_only_list():


    nasdap100_path = "/home/mk_m/device/nasdap100_info.json"
    sp500_path = "/home/mk_m/device/sp500_info.json"

    result_nasdap100 = readjsonfile(nasdap100_path)
    result_sp500 = readjsonfile(sp500_path)
    result_us = result_nasdap100 + result_sp500
    us_only_list = us_only_list_func(result_us)
    us_only_list_file = "/home/mk_m/device/us_only_list.json"
    writeinto_jsonfile(us_only_list_file, us_only_list)

    print(__file__, "----->OK")



class Spider(scrapy.Spider):
    name = ''
    allowed_domains = []
    start_urls = ['https://www.slickcharts.com/nasdaq100']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                args={'wait':1}, endpoint='render.html')

    def parse(self, response):

        code = response.xpath('/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[3]/a/text()').extract()
        price = response.xpath('/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[5]/text()').extract()
        change_v = response.xpath('/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[6]/text()').extract()
        change_r = response.xpath('/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[7]/text()').extract()
        change_r_float = [float(re.findall(re.compile('\((.*?)%\)', re.S), x)[0]) for x in change_r]
        for i1, i2, i3, i4, i5 in zip(code, price, change_v, change_r, change_r_float):
            one_stock_info = {}
            for item in json_result:
                if i1 == item["code"]:
                    item["last_price"] = i2
                    item["change_v"] = i3
                    item["change_r"] = i4
                    item["change_r_float"] = i5
                    big_list.append(item)
                    print(item)

                    # print(i1,i2,i3,i4,i5,item)
                elif "." in i1:
                    i1 = i1.replace(".", "-")
                    if i1 == item["code"]:
                        item["last_price"] = i2
                        item["change_v"] = i3
                        item["change_r"] = i4
                        item["change_r_float"] = i5
                        print(i1, i2, i3, i4, i5, item)
                        big_list.append(item)

            writeinto_jsonfile(json_file, big_list)
        print(__file__, "----->OK")

        f_us_only_list()
