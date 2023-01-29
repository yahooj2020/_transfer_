# 二、利用os.listdir递归获取所有的目录路径和文件路径
# def get_file_path(root_path,file_list,dir_list):
#     #获取该目录下所有的文件名称和目录名称
#     dir_or_files = os.listdir(root_path)
#     for dir_file in dir_or_files:
#         #获取目录或者文件的路径
#         dir_file_path = os.path.join(root_path,dir_file)
#         #判断该路径为文件还是路径
#         if os.path.isdir(dir_file_path):
#             dir_list.append(dir_file_path)
#             #递归获取所有文件和目录的路径
#             get_file_path(dir_file_path,file_list,dir_list)
#         else:
#             file_list.append(dir_file_path)
#
# if __name__ == "__main__":
#     #根目录路径
#     root_path = r"D:\test"
#     #用来存放所有的文件路径
#     file_list = []
#     #用来存放所有的目录路径
#     dir_list = []
#     get_file_path(root_path,file_list,dir_list)
#     print(file_list)
#     print(dir_list)
import os
from csb_config import *
import markdown

# 各种编程语言的后缀  https://gist.github.com/ppisarczyk/43962d06686722d26d176fad46879d41

def get_file_path(root_path,file_list,dir_list):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)


def remove_get_rid_list(list_content):
    ret_list = []
    for item in list_content:
        for remove_item in get_rid_list:
            if remove_item in item:
                ret_list.append(item)
                # list_content.remove(item)
    [list_content.remove(x) for x in ret_list]
    return list_content

def get_pro_contents(file_list,new_title):
    ret_list = []
    exec_file_list = []
    for item in file_list:
        file_string = item.split(path_info)[1].split("\\")[-1]

        # file_suffix = None
        if "."  in file_string:
            file_suffix_ret = "." +file_string.split(".")[1]
            if len([x for x in Programming_Languages_suffix_list if x ==file_suffix_ret]) == 1:
                file_url = "/detail" + new_title + "-" + file_string + ".html"
                ret_contents = '<div class="navto-nav"><a href="{0}"><i class=""></i>{1}</a></div> \n'.format(file_url,file_string)
                ret_list.append(ret_contents)
                exec_file_list.append(item)
    return ret_list,exec_file_list

def writeinto_htmlfile(filename,data):
    with open(filename,"a",newline="",encoding="utf-8") as f:
        f.write(data)
        f.write("\n")

def readDatafile(filename):
    line_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line_list.append(line)
    return line_list
def get_md_text(filename):
    try:

        cs_md_top = "``` \n"
        cs_md_body = ""
        cs_md_footer = "\n```"
        with open(filename,"r",encoding="utf-8") as f:
            data = f.readlines()
            cs_md_body = "".join(data)

        ret_string = cs_md_top + cs_md_body +cs_md_footer
        return ret_string
    except BaseException as e:
        pass




def get_only_oneArgs_list(exec_file_list):
    execed_file_list = []
    execed_htmlfile_list = []
    for onefile in exec_file_list:

        one_filename = onefile.split("\\")[-1]

        if one_filename not in execed_file_list:
            execed_file_list.append(one_filename)

            onefile_html_name = "-".join(pro_name_to_show.split("/")) + "-{0}".format(one_filename) + ".html"
            execed_htmlfile_list.append(onefile_html_name)
    return execed_file_list,execed_htmlfile_list,exec_file_list


def to_get_pro_template_contents_details(contents_html_name,pro_html_name):

    get_file_path(path_info,file_list,dir_list)

    pro_url = "/" +pro_name_to_show.replace("/","-")
    # print("file_list-->",file_list)
    # print("pro_url-->",pro_url) # pro_url--> /tornado



    # output pro_tempalte
    pro_template_detail_list,exec_file_list = get_pro_contents(file_list, pro_url)


    #   <div><a class="previous"  style="text-align: left;" href="/Ruby">Previous : handler.go</a>&nbsp<a class="next"   style="text-align: right;" href="/Ruby">Next : handler.go</a></div>

    pro_template_top = '<!DOCTYPE html> \n <html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system"> \n    <head> \n     <meta charset="utf-8">\n   <link rel="stylesheet" href="../static/monokai.css">  \n<link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/font-awesome.css" />    <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/style.css" />\n  <style>\n      .previous{ \n         float:left; \n     } \n    .next { \n         float:right;\n     } \n </style> \n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c1.css" /> \n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c2.css" />  \n     <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c3.css" /> \n    <link rel="stylesheet" href="https://cdn.staticfile.org/font-awesome/4.7.0/css/font-awesome.css" media="all" /> \n   <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://svgsilh.com/svg/33581.svg"> \n   </head> \n    <body class="logged-in env-production page-responsive page-blob" style="word-wrap: break-word;"> \n      <div class="position-relative js-header-wrapper "> \n            \n  <header class="Header js-details-container Details px-3 px-md-4 px-lg-5 flex-wrap flex-md-nowrap" role="banner"> \n<div class="Header-item mt-n1 mb-n1  d-none d-md-flex">      \n <a class="Header-link" href="http://127.0.0.1:8888" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">   \n<svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark- v-align-middle">   \n  <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-2.82.64-.18 12.44 1.1.16 1.92.08 2.12.5115.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>\n</svg> \n</a>   \n  </div>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Python">Python</a> \n  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Java">Java</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Go">Go</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/JavaScript">JavaScript</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/PHP">PHP</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/C">C</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/C++">C++</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/C#">C#</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/R">R</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Shell">Shell</a>  \n<a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Rust">Rust</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/lua">lua</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Ruby">Ruby</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Perl">Perl</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Swift">Swift</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Julia">Julia</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/TypeScript">TypeScript</a>  \n <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Vue">Vue</a>   \n<a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/Others">Others</a> \n </div> \n <div class="page main">  \n   <div class="horizon">    \n     <div class="col left-column">    \n         <div class="sidebar-box gallery-list">    \n       <div class="design"> \n'



    pro_template_name = '<div class="programe_name"><a href="/detail/{0}"><i class=""></i>Programe Name : {1}</a></div> \n'.format(contents_html_name.split("\\")[-1],pro_name_to_show)


    pro_template_contents = '<div class="contents"><a href="{0}/contents"><i class=""></i>Contents</a></div>\n'.format(pro_url)
    pro_template_footer = '\n </div>     \n        </div>   \n      </div>  \n  <div class="col middle-column-home"> \n{% block body %} \n{% endblock %}\n </div>   \n      <div class="right-column right-home">     \n        <div class="sidebar-box re-box">        \n         <div class="tab">           \n                    <a href="/">\n                                      <i class="fa fa-reorder" aria-hidden="true"></i> Rank \n         </div>         \n       <div class="design">            \n       <div class="navto-nav"><a href=""><i class=""></i> JavaScript - material-ui</a></div> \n<div class="navto-nav"><a href=""><i class=""></i> Python - flask</a></div> \n<div class="navto-nav"><a href=""><i class=""></i> C - redis</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> C# - shadowsocks-windows</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Vue - element</a></div> \n<div class="navto-nav"><a href=""><i class=""></i> TypeScript - nest</a></div> \n<div class="navto-nav"><a href=""><i class=""></i> Python - requests</a></div> \n<div class="navto-nav"><a href=""><i class=""></i> Java - RxJava</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> C++ - grpc</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - terraform</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Swift - ShadowsocksX-NG</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - beego</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - compose</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - vault</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - consul</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Java - selenium</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Ruby - vagrant</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Ruby - gitlabhq</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Swift - RxSwift</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Swift - SwiftyJSON</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Python - tornado</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> TypeScript - vue</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> TypeScript - graphql-js</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - websocket</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - colly</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - mux</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> C - nginx</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Vue - ant-design-vue</a></div>\n \n<div class="navto-nav"><a href=""><i class=""></i> Vue - mint-ui</a></div> \n<div class="navto-nav"><a href=""><i class=""></i> Vue - iview-admin</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> TypeScript - react-sketchapp</a></div>\n <div class="navto-nav"><a href=""><i class=""></i> Go - kops</a></div>  \n               </div>    \n         </div>     \n    </div>       \n      </div>        \n </div>    \n </div>\n </div>  \n </body> \n</html>'

    pro_html_name = os.path.join(templates_path, pro_html_name)
    writeinto_htmlfile(pro_html_name,pro_template_top)
    writeinto_htmlfile(pro_html_name,pro_template_name)
    # writeinto_htmlfile(pro_html_name,pro_template_contents)
    for item in pro_template_detail_list:
        writeinto_htmlfile(pro_html_name,item)
    writeinto_htmlfile(pro_html_name,pro_template_footer)






    # add contents  ok
    contents_pro_html_name = pro_html_name.split(templates_path)[1].replace("\\","")


    inherit_pro_template_str = '{{% extends "{0}" %}} \n{{% block body %}} \n'.format(contents_pro_html_name)
    writeinto_htmlfile(contents_html_name, inherit_pro_template_str)


    css_template_str = "<style>    #dir1    {background-color:#54aeff;}#dir2{color:#cf222e;}#dir3{color:#000000;}#dir4{color:#0969da;}</style>"
    writeinto_htmlfile(contents_html_name, css_template_str)
    big_list = []
    if os.path.exists(translate_filename):
        list_ret = readDatafile(translate_filename)

        for item in list_ret:
            if item.count("|") == 1:
                ret = "<h4 id='dir1'>{0}</h4>".format(item)
                big_list.append(ret)
            elif item.count("|") == 2:
                ret = "<h4 id='dir2'>{0}</h4>".format(item.replace("     ", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"))
                big_list.append(ret)

            elif item.count("|") == 3:
                ret = "<h4 id='dir3'>{0}</h4>".format(item)
                big_list.append(ret)
            else:
                ret = "<h4 id='dir4'>{0}</h4>".format(item)
                big_list.append(ret)

        for item in big_list:
            writeinto_htmlfile(contents_html_name, item)

        writeinto_htmlfile(contents_html_name, "\n")
        writeinto_htmlfile(contents_html_name, "{% endblock %}")


    # add details

    # 出现了重复的现象，为了最大限度保证整齐。 剔除重复的文件内容

    pro_one_file_top_inherit = '{{% extends "{0}" %}} \n{{% block body %}} \n'.format(contents_pro_html_name)
    execed_file_list,execed_htmlfile_list,exec_file_list = get_only_oneArgs_list(exec_file_list)
    for i1,i2,i3 in zip(execed_file_list,execed_htmlfile_list,exec_file_list):
        if execed_file_list.index(i1) == 0:
            previous_next_string = '<div><a class="previous"  style="text-align: left;" href=""></a>&nbsp<a class="next"   style="text-align: right;" href="/detail/{0}">Next : {1}</a></div> <br>'.format(
                execed_htmlfile_list[execed_file_list.index(i1) + 1],
                execed_file_list[execed_file_list.index(i1) + 1])
        elif execed_file_list.index(i1) == len(execed_file_list) - 1:
            # print(i1,i2,i3)
            # previous_next_string = ""

            previous_next_string = '<div><a class="previous"  style="text-align: left;" href="/detail/{0}">Previous : {1}</a>&nbsp<a class="next"   style="text-align: right;" href=""></a></div><br>'.format(
                execed_htmlfile_list[execed_file_list.index(i1) - 1],
                execed_file_list[execed_file_list.index(i1) - 1])
        elif 0<execed_file_list.index(i1)<len(execed_file_list) - 1:
            previous_next_string = '<div><a class="previous"  style="text-align: left;" href="/detail/{0}">Previous : {1}</a>&nbsp<a class="next"   style="text-align: right;" href="/detail/{2}">Next : {3}</a></div><br>'.format(
                execed_htmlfile_list[execed_file_list.index(i1) - 1],
                execed_file_list[execed_file_list.index(i1) - 1],
                execed_htmlfile_list[execed_file_list.index(i1) + 1],
                execed_file_list[execed_file_list.index(i1) + 1])

        pro_one_file_top_update = previous_next_string
        writeinto_htmlfile(os.path.join(templates_path, i2), pro_one_file_top_inherit)
        writeinto_htmlfile(os.path.join(templates_path, i2), pro_one_file_top_update)

        #  以下内容出现了问题
        ret_file = get_md_text(i3)
        print("ret_file-->",ret_file)

        html = markdown.markdown(ret_file, extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
        ])

        writeinto_htmlfile(os.path.join(templates_path, i2), html)

        pro_one_file_footer = "\n{% endblock %}"
        writeinto_htmlfile(os.path.join(templates_path, i2), pro_one_file_footer)

    #
    # for onefile in exec_file_list:
    #
    #     one_filename = onefile.split("\\")[-1]
    #
    #
    #     if one_filename not in execed_file_list:
    #         # execed_file_list.append(one_filename)
    #
    #         onefile_html_name = "-".join(pro_name_to_show.split("/")) + "-{0}".format(one_filename) + ".html"
    #         # execed_htmlfile_list.append(onefile_html_name)
    #         print("one_filename-->", one_filename)
    #         print("onefile_html_name-->", onefile_html_name)
#
#
# #previous_next_string

#
# # #   <div><a class="previous"  style="text-align: left;" href="/Ruby">Previous : handler.go</a>&nbsp<a class="next"   style="text-align: right;" href="/detail/{01}">Next : handler.go</a></div>
#             # <a href="/detail/chatgo-main.go.html"><i class=""></i>main.go</a>
#



def sitemap():
    pass


if __name__ == "__main__":
    file_list = []
    dir_list = []
    get_rid_list = [".github", ".md", "LICENSE", ".jpg", ".JPG", ".svg", ".SVG", ".JPEG", ".jpeg", ".png", ".PNG",
                    ".gitignore",".pem",".MD"]
    pro_folder = pro_name_to_show
    contents_html_name = "-".join(pro_name_to_show.split("/")) + "-contents" + ".html"
    pro_html_name = "-".join(pro_name_to_show.split("/")) + "-template" + ".html"
    templates_path = os.path.join(os.getcwd(), "../templates")
    contents_html_name = os.path.join(templates_path,contents_html_name)
    pro_html_name = os.path.join(templates_path,pro_html_name)

    path_info = os.path.join(os.getcwd(), pro_folder)
    # to_get_pro_template_contents_details(contents_html_name,pro_html_name)



