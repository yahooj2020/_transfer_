

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
def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)






def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper


def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        ff_str = f_str +"00"
        f_l.append(ff_str)

    return f_l

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        f = " ".join(it.split())
        new_items.append(f)
    return new_items
def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def use_requests(url):

    response = requests.get(url)
    return response.text

ch_options = webdriver.ChromeOptions()
ch_options.add_argument("--headless")
ch_options.add_argument('--no-sandbox')
ch_options.add_argument('--disable-gpu')
ch_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=ch_options)
def use_selenium_headless_getdt(url):

    # 为Chrome配置无头模式

    # 在启动浏览器时加入配置

    driver.get(url)
    html = driver.page_source
    # driver.quit()
    return html


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='ForLynne',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        cursor.executemany('insert into SpPlusNas_industryInfo_fromGoogleFinance (code,title_zh_cn,infos_zh_cn) values (%s,%s,%s)', content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass

def readjsonfile(filename):
   with open(filename, 'r', encoding='utf-8') as fw:
      s = json.load(fw)
      return s

def getinfos_fromYhaooFinance(code):
    url = "https://finance.yahoo.com/quote/{0}/profile?p={0}".format(code)
    html = use_selenium_headless_getdt(url)
    selector = etree.HTML(html)
    industry_infos = selector.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div/div/p[2]/span[4]/text()')
    sector_infos = selector.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div/div/p[2]/span[2]/text()')
    return industry_infos,sector_infos

# ['Consumer Electronics'] ['Technology']

def writeinto_jsonfile(filename, list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)



from fabric import Connection
import os

def scaner_file (window_path):
    path_list = []
    file = os.listdir(window_path)
    for f in file:
        read_path = os.path.join(window_path,f)
        path_list.append(read_path)
    return path_list


# 1. 遍历目录下的所有文件
# 2. 再遍历上传

def from_Windows_upload_to_linux(window_path,username,Linux_ip,password,Linux_path):

    c = Connection(host=f'{username}@{Linux_ip}',connect_kwargs={'password': password})
    c.put(window_path, remote=Linux_path)

import datetime
import sys
import time


# "15:32:55"
# 在特定时间停止函数的装饰器和函数


def at_sometime_exit(parameter):
    print(parameter)
    def wrapper(func):
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)
            while True:
                print("ssss")
                now_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
                stop_timeline = datetime.datetime.strptime(parameter, "%H:%M:%S")
                print(now_time)
                print(stop_timeline)
                time.sleep(1)
                if now_time > stop_timeline:
                    print("ok")
                    sys.exit(0)
                return ret
        return inner
    return wrapper

def regular_time_exit(stop_time):
    while True:
        print("ssss")
        now_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")
        stop_timeline = datetime.datetime.strptime(stop_time, "%H:%M:%S")
        print(now_time)
        print(stop_timeline)
        time.sleep(1)
        if now_time>stop_timeline:
            print("ok")
            sys.exit(0)

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



def f_func():

    big_list = []

    json_file = "/home/mk_m/device/nasdap100_info.json"
    json_result = readjsonfile(json_file)
    url = "https://www.slickcharts.com/nasdaq100"
    result = use_selenium_headless_getdt(url)

    selector = etree.HTML(result)
    code = selector.xpath('/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[3]/a/text()')
    price = selector.xpath('/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[5]/text()')
    change_v = selector.xpath('/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[6]/text()')
    change_r = selector.xpath('/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr/td[7]/text()')
    change_r_float = [float(re.findall(re.compile('\((.*?)%\)',re.S),x)[0]) for x in change_r]

    for i1,i2,i3,i4,i5 in zip(code,price,change_v,change_r,change_r_float):
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
                i1 = i1.replace(".","-")
                if i1 == item["code"]:
                    item["last_price"] = i2
                    item["change_v"] = i3
                    item["change_r"] = i4
                    item["change_r_float"] = i5
                    print(i1, i2, i3, i4, i5, item)
                    big_list.append(item)

        writeinto_jsonfile(json_file,big_list)
    print(__file__,"----->OK")

if __name__ == "__main__":


    f_func()
    f_us_only_list()

































# create table SpPlusNas_industryInfo_fromGoogleFinance(id int not null primary key auto_increment,code  text,title_zh_cn text,infos_zh_cn  text, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;

#
# drop table SpPlusNas_industryInfo_fromGoogleFinance;
