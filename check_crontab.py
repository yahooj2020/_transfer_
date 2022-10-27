
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


for item in range(1,100):
    check_crontab("abc")
