# -*-coding: utf-8 -*-
# 用 Python 脚本批量检测网页是否能有效访问
# 新建一个url.txt的记事本文件，将需要检测的网址写在记事本里，每行一个网址，网址要用http://或者https://开头。
# 保存脚本后，记得将.txt文件和.py文件放在同一个文件目录下，打开终端执行以下命令：
#
# python go2url.py -f url.txt
# 测试完记事本里的所有网址后，脚本会自动创建一个名为result.tsv的表格文件，所有的测试结果都保存在这个表格文件里。

# https://chaisw.cn/blog/1919.html
import requests, re
import urllib3
import logging
import pymysql
logging.captureWarnings(True)
from concurrent.futures import ThreadPoolExecutor
import argparse
import time
# import ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='nw_msg',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into check_domain (url,redirect_url,status_code,title) values (%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass
def parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="指定domain文件")
    return parser.parse_args()


f = open("result.tsv", "a", encoding='utf-8')
f.write("源地址" + "," + "跳转地址" + "," + "状态码" + "," + "标题" + '\n')
f = f.close()

start = time.time()


def getTitle(url):
    f = open("result.tsv", "a", encoding='utf-8')
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }

    try:
        res = requests.get(url, headers=header, verify=False, allow_redirects=True, timeout=10)
        code = res.status_code
    except Exception as error:
        code = "无法访问"

    code1 = str(code)
    result_list = []

    if code1 != "无法访问":
        try:
            urllib3.disable_warnings()
            res = requests.get(url, headers=header, verify=False, allow_redirects=True, timeout=10)
            res.encoding = res.apparent_encoding
            title = re.findall("(?<=\<title\>)(?:.|\n)+?(?=\<)", res.text, re.IGNORECASE)[0].strip()
        except:
            title = "[ ]"
        f.write(url + "," + res.url + "," + code1 + "," + title + '\n')
        result_list.append(url)
        result_list.append(res.url)
        result_list.append(code1)
        result_list.append(" ".join(title))
        print(url + "," + res.url + "," + code1 + "," + title)
        f_tup = tuple(result_list)
        print(len(f_tup))
        insertDB([f_tup])
    else:
        title = " "
        f.write(url + "," + " " + "," + code1 + "," + title + '\n')
        result_list.append(url)
        result_list.append(res.url)
        result_list.append(code1)
        result_list.append(" ".join(title))
        print(url + "," + " " + "," + code1 + "," + title)
        f_tup = tuple(result_list)
        print(len(f_tup))

        insertDB([f_tup])
    f = f.close()


a = vars(parser_args())
file = a['file']
try:
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in open(file, errors="ignore").readlines():
            executor.submit(getTitle, i.strip().strip('\\'))
except:
    print('-f 指定domain文件')
end = time.time()
print("总耗时:", end - start, "秒")



# create table check_domain (id int not null primary key auto_increment,
# url  varchar(255),
# redirect_url  varchar(255),
# status_code  varchar(255),
# title  varchar(255),
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;