#! -*- utf-8 -*-
import copy
import re
import json
import time
from lxml import etree
from selenium import webdriver
import csv
import os
ch_options = webdriver.ChromeOptions()
# 为Chrome配置无头模式
ch_options.add_argument("--headless")
ch_options.add_argument('--no-sandbox')
ch_options.add_argument('--disable-gpu')
ch_options.add_argument('--disable-dev-shm-usage')
# 在启动浏览器时加入配置
driver = webdriver.Chrome(options=ch_options)


def use_selenium_headless_getdt(url):
    driver.get(url)
    html = driver.page_source
    return html





def list_null(list_content):
    if list_content !=[]:
        result = list_content
    else:
        result = ["null"]
    return result



def writeinto_jsonfile(filename,list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)


def writeintoTSV_file(filename,data):
    with open(filename,'a', newline='\n', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)
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
# 1 检测 文件，有就不动：没有就创建创建
# 2 一次写入文件，包括文件名，时间，msg

import os
from inspect import currentframe, getframeinfo
from datetime import datetime
import csv

def writeinto_detail(filename,data):
    with open(filename,"a",newline="",encoding="utf-8") as f:
        f.writelines(data)
        f.writelines("\n")

def check_crontab(filename):
    isExists = os.path.exists(filename)
    if not isExists:
        open(filename,"w",encoding="utf-8")
    frameinfo = getframeinfo(currentframe())
    current_filename = os.path.basename(frameinfo.filename)
    print(current_filename)

    time_  =datetime.now().strftime("%Y-%m-%d")
    print(type(time_))
    msg = os.getcwd()
    result = "--- time: {0} filename: {1} ---- msg: {2}".format(time_,current_filename,msg)
    writeinto_detail(filename,result)
if __name__=="__main__":

    json_list_3months =[]
    json_list_6months =[]
    url_list= []
    # device_path_windows = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),"device")
    json_file_3months = os.path.join("sbi_trust_since_3months_ago.json")
    json_file_6months = os.path.join("sbi_trust_since_6months_ago.json")


    url ="https://site0.sbisec.co.jp/marble/fund/powersearch/fundpsearch.do?"
    html = use_selenium_headless_getdt(url)
    driver.find_element_by_xpath('//*[@id="tab_values_base"]/table/thead/tr/th[4]/a[2]/span').click()

    selector = etree.HTML(html)
    url_code = selector.xpath('//*[@id="tab_values_base"]/table/tbody/tr/td/a/@href')
    f_url = ["https://site0.sbisec.co.jp/{0}".format(x) for x in url_code]
    for item in f_url:
        print(item)
        url_list.append(item)
    # 开始翻页 20页吧
    for onepage in range(25):
        driver.find_element_by_xpath('//*[@id="pageHolderLower"]/div/div[2]/p[3]/a').click()
        time.sleep(10)
        html = driver.page_source
        selector = etree.HTML(html)
        url_code = selector.xpath('//*[@id="tab_values_base"]/table/tbody/tr/td/a/@href')
        f_url = ["https://site0.sbisec.co.jp/{0}".format(x) for x in url_code]
        for item in f_url:
            print(item)
            url_list.append(item)

    for oneurl in url_list:
        driver.get(oneurl)
        html = driver.page_source
        time.sleep(10)


        selector = etree.HTML(html)
        try:

            date_of_established = selector.xpath('//*[@id="MAINAREA02_780"]/div[5]/div[1]/table/tbody/tr[39]/td/text()')
            pattern_6months = re.compile('<th class="alC">6カ月</th>.*?<td .*?>(.*?)</td>', re.S)
            items = re.findall(pattern_6months, html)
            change_r_6months = items[0].split()

            pattern_3months = re.compile('<th class="alC">3カ月</th>.*?<td .*?>(.*?)</td>', re.S)
            items = re.findall(pattern_3months, html)

            change_r_3months = items[0].split()
            print(change_r_6months)

            print(change_r_3months)



            title = selector.xpath('//*[@id="MAINAREA02_780"]/div[1]/div[1]/div/h3/text()')
            pattern = re.compile('<p class="fl01" style="margin-left:24px;">(.*?)</p>', re.S)
            items = re.findall(pattern,html)
            firm = items[0].split()[0]

            pattern = re.compile("運用方針.*?<td>(.*?)</td>", re.S)
            items = re.findall(pattern,html)
            strategy = items[0].split()

            community_code = selector.xpath('//*[@id="MAINAREA02_780"]/div[5]/div[1]/table/tbody/tr[7]/td/text()')
            pattern = re.compile("税込.*?<td>(.*?)</td>", re.S)
            items = re.findall(pattern,html)
            fee = items[1].split()[0]
            last_day = selector.xpath('//*[@id="MAINAREA02_780"]/div[5]/div[1]/table/tbody/tr[41]/td/text()')
            pattern = re.compile('<td class="alR">(.*?)</td>', re.S)
            items = re.findall(pattern,html)
            assert_ = items[0].split()
            result_3months = {}
            result_6months = {}


            result_3months["title"] = "".join(list_null(title)).split()[0]
            result_3months["firm"] = "".join(list_null(firm)).split()[0]
            result_3months["strategy"] = "".join(list_null(strategy)).split()[0]
            result_3months["change_r"] = "".join(list_null(change_r_3months)).split()[0]
            result_3months["change_r_float"] =  float(result["change_r"].split("%")[0])
            result_3months["date_of_established"] = "".join(list_null(date_of_established)).split()[0]
            result_3months["last_day"] = "".join(list_null(last_day)).split()[0]
            result_3months["community_code"] = "".join(list_null(community_code)).split()[0]
            result_3months["fee"] = "".join(list_null(fee)).split()[0]
            result_3months["assert_"] = "".join(list_null(assert_)).split()[0]
            result_3months["url"] = oneurl
            result_3months["short_name_html"] ="<a href=\"{0}\">{1}</a>".format(oneurl,"".join(list_null(title)).split()[0])





            result_6months["title"] = "".join(list_null(title)).split()[0]
            result_6months["firm"] = "".join(list_null(firm)).split()[0]
            result_6months["strategy"] = "".join(list_null(strategy)).split()[0]
            result_6months["change_r"] = "".join(list_null(change_r_6months)).split()[0]
            result_6months["change_r_float"] =  float(result["change_r"].split("%")[0])
            result_6months["date_of_established"] = "".join(list_null(date_of_established)).split()[0]
            result_6months["last_day"] = "".join(list_null(last_day)).split()[0]
            result_6months["community_code"] = "".join(list_null(community_code)).split()[0]
            result_6months["fee"] = "".join(list_null(fee)).split()[0]
            result_6months["assert_"] = "".join(list_null(assert_)).split()[0]
            result_6months["url"] = oneurl
            result_6months["short_name_html"] ="<a href=\"{0}\">{1}</a>".format(oneurl,"".join(list_null(title)).split()[0])


            print(result_6months)
            print(result_3months)
            json_result_3months = copy.deepcopy(result_3months)
            json_result_6months = copy.deepcopy(result_6months)
            json_list_3months.append(json_result_3months)
            json_list_6months.append(json_result_6months)

        except:
            pass

    writeinto_jsonfile(json_file_3months,json_list_3months)
    writeinto_jsonfile(json_file_6months,json_list_6months)
    print(__file__,"----->OK")
