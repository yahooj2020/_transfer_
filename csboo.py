#
#
# # 1. read the folder , to output json file ,
#
#
#
import requests

get_rid_list = [".github",".md"]
#
#
#
# class CSBookOnePage(object):
#
#     def __init__(self):
#         pass
#
#
#     def read_folder_output_template(self):
#
#         """
#
#         return:  1.urls_list , 2.output pro_template.html
#         """
#         # 1 读取文件目录，生成json格式的层级内容。同时剔除一些比如 .md 的内容，同时生成template
#         # pro_template.html
#         pass
#
#
#     def pro_topContents_html(self):
#         # 2 继承模板页面，生成项目目录contents的首页
#         pass
#
#     def recursive_(self):
#         pass
#
#         # 3 读取目录的文件内容，生成单页面的URL，请求后整理，并生成继承模板的单一文件的html文件。
#
#     @staticmethod
#     def read_folder(folderpath):
#
pro_url = ""
folder_list = []
file_list = []
def recursive_(url):

    ret = requests.get(url)
    for item in ret:
        if "tree" not in item:
            file_list.append(item)
        elif "tree" in item and item not in folder_list:
            recursive_(item)
