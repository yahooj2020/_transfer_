
#
#
# # 1. read the folder , to output json file ,
#
#
#
import requests
from lxml import etree




class CSBookOnePage(object):

    def __init__(self):
        pass


    def read_folder_output_template(self):

        """

        return:  1.urls_list , 2.output pro_template.html
        """
        # 1 读取文件目录，生成json格式的层级内容。同时剔除一些比如 .md 的内容，同时生成template
        # pro_template.html
        pass


    def pro_topContents_html(self):
        # 2 继承模板页面，生成项目目录contents的首页
        pass
        # 3 读取目录的文件内容，生成单页面的URL，请求后整理，并生成继承模板的单一文件的html文件。

    @staticmethod
    def read_folder(folderpath):
        pass

    def remove_get_rid_list(self,list_content):
        ret_list = []
        for item in list_content:
            for remove_item in get_rid_list:
                if remove_item in item:
                    ret_list.append(item)
                    # list_content.remove(item)
        [list_content.remove(x) for x in ret_list]
        return list_content

    def __recursive(self,url):
        ret = requests.get(url)
        element = etree.HTML(ret.text)

        urls = element.xpath('//div[2]/span/a/@href')

        for item in urls:

            if "tree" not in item:
                file_list.append("https://github.com{0}".format(item))
                print(item)
            elif "tree" in item and item not in folder_list:
                self.__recursive("https://github.com{0}".format(item))

    def last_name_htmlfile(self,url):
        # 借鉴其他的网站，只保留最后的文件即可
        htmlfile = url.split("/")[-1]+".html"

        return htmlfile




#  1. floder---> pro_template.html  , pro_contents.html
#  2. pro_url---->pro_file1.html pro_file2.html .....
#  3. pro_template.html a. pro_contents.html----url---->   b. pro_file1.html--->url




#

# def recursive_(url):
#     ret = requests.get(url)
#     element = etree.HTML(ret.text)
#
#     urls = element.xpath('//div[2]/span/a/@href')
#
#     for item in urls:
#
#         if "tree" not in item:
#             file_list.append("https://github.com{0}".format(item))
#             print(item)
#         elif "tree" in item and item not in folder_list:
#             recursive_("https://github.com{0}".format(item))



if __name__ == "__main__":
    pro_url = "https://github.com/yahooj2020/test_res"
    get_rid_list = [".github", ".md","LICENSE"]
    folder_list = []
    file_list = []
