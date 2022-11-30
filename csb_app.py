#! -*- coding:utf-8 -*-



# app.config.from_object(__name__)
# app.config["JSON_AS_ASCII"] = False


from flask import Flask,request,render_template
from flask_paginate import Pagination,get_page_parameter
from flask_bootstrap import Bootstrap
import pymysql

bootstrap = Bootstrap()

# Flask学习之旅--分页功能：分别使用 flask--pagination 和分页插件 layPage
# https://article.itxueyuan.com/lXw67k

app = Flask(__name__)
bootstrap.init_app(app)

@app.route("/<onetype>",methods=["GET","POST"])
def pagination_index(onetype):
    # onetype_ret = None
    # if onetype == "=Golang":
    #     onetype_ret = "='Go'"
    # elif onetype == "C/C++":
    #     onetype_ret = "in ('C','C++')"
    if onetype == "Others":
        onetype_ret = "not in ('Python','Java','Go','JavaScript','PHP','C#','Rust','R','Shell','lua','Ruby','Perl','Swift','Julia','TypeScript','Vue','C','C++')"
    else:
        onetype_ret = "='{0}'".format(onetype)


# 1. stars 排序 ok
# 2.  infos，
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='github_info',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    # sql 语句
    count_sql = "select infos,language_,weight,stars_num from github_info_checked where language_  {0}  ; ".format(onetype_ret)

    cur.execute(count_sql)
    # #获取所有记录列表
    data = cur.fetchall()
    ## 按照星级排序
    # data = list(set(data))
    data_list = []
    for item in data:
        item["new_infos"] = item["infos"].split("https://github.com/")[1]
        data_list.append(item)
#  <td href="http://baidu.com">{{ row.new_infos }}</td>
    # [{'infos': 'https://github.com/pallets/jinja', 'language_': 'Python', 'weight': '100.0%', 'stars_num': '89000', 'new_infos': 'pallets/jinja'},
    set_list = []
    for item in data_list:
        if item not in set_list:
            set_list.append(item)
    [set_list.append(x) for x in data if x not in set_list]
    print(set_list)
    set_list.sort(key=lambda x: (int(x["stars_num"])), reverse=True)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    res = set_list[(page - 1) * 45: page * 45]
    pagination = Pagination(page=page, total=len(set_list), per_page=45, css_framework='bootstrap4')
    return render_template('pag_test.html', rows=res, pagination=pagination)



# ok
@app.route("/")
def homepage():
    return render_template("homepage.html")

# 单一语言页面


# 单个项目页面的，一个文件展示页面





### 路由管理
if __name__ == '__main__':
    app.run(debug=True,port=8888,threaded=True)