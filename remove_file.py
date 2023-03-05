


# 必须得批量处理了。不然手动太慢了。


# 1. 用error 的文件找到 报错的html 文件，然后去寻找 前后的html文件


# 2. 再去找前面的文件，把下一页转成，刚才报错的下一也的内容。


# 3. 再去找下一页的html文件，把上一些，换成报错的上一页的内容


# 4. 最后用删除报错的html文件




# airbnb-knowledge-repo-requests.py


import os
import re
import time


def read_file(file):
    with open(file,encoding="utf-8") as f:
        read_all =f.read()
        f.close()
    return read_all



import os







def rewrite_file(file,data):
    with open(file,"w",encoding="UTF-8") as f:
        f.write(data)
        f.close()


def replace(file,old_c,new_c):
    content = read_file(file)
    content = content.replace(old_c,new_c)
    rewrite_file(file,content)




def remove_file(filename):
    for file in os.listdir("."):
        file_list = file.split(".")
        if len(file_list) != 1 and os.path.exists(filename):
            os.remove(filename)

# if __name__ == "__main__":
def re_previous_next(htmlfile):
    ret = read_file(htmlfile)
    if ">Previous" not in ret:
        remove_file(htmlfile)

    else:

        pattern = re.compile('href="/detail/(.*?)">Previous : (.*?)</a>.*? href="/detail/(.*?)">Next : (.*?)</a></div>',
            re.S)
        items = re.findall(pattern, ret)
        prefile_htmlfile,prefile,nextfile_htmlfile,nextfile = items[0]
        return prefile_htmlfile,prefile,nextfile_htmlfile,nextfile
def readDatafile(filename):
    line_list = []
    call_list = []
    put_list = []
    with open(filename,"r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line_list.append(line)


    return line_list

if __name__ == "__main__":
    error_file_list = readDatafile("checked_ret")



    execfile_list = []
    templatePath = os.path.join(os.getcwd(),"templates")
    for dirname, subdir, subfile in os.walk(templatePath):
        for one_file in subfile:
            execfile_list.append(os.path.join(dirname,one_file))

    for item in execfile_list:


        single_error_file = item.split("\\")[-1].split(".html")[0]
        if single_error_file in error_file_list:
            os.remove(item)










# automl-mf-prior-exp-test_success.py
