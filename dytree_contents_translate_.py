import copy
import io
import os
import os.path
import sys
import time



from csb_config import *

class CSBookProject(object):


    def linux_tree_list_dir_demo1(self,path, depth=0):
        if depth == 0:
            print(path)
        items = os.listdir(path)
        for item in items:
            # 输出文件夹中的文件和子文件夹名
            # ：为end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。
            print('|    '*depthma, end='')
            print('|----', item)
            item = os.path.join(path, item)
            if os.path.isdir(item):
                # 递归遍历子目录
                self.linux_tree_list_dir_demo1(item, depth+1)





    def linux_tree_list_dir_demo2(self,dir_name, deepth=0):
        os.chdir(dir_name)
        # text1 =
        print("|" + "----" * deepth, os.getcwd())
        child_dirs = []
        for item in os.listdir(".."):
            if os.path.isdir(item):
                child_dirs.append(item)
            else:
                print("|    " * (deepth + 1), "|---- ", item, "    [ Size: ", os.path.getsize(item), "]")
        for child_dir in child_dirs:
            self.linux_tree_list_dir_demo2(child_dir, deepth + 1)
        os.chdir("../..")


    def linux_tree_list_dir(self,dir_name, deepth=0):
        os.chdir(dir_name)
        print("|" + "----" * deepth, os.getcwd())
        child_dirs = []
        for item in os.listdir(".."):
            if os.path.isdir(item):
                child_dirs.append(item)
            else:
                print("|    " * (deepth + 1), "|---- ", item, "    [ Size: ", os.path.getsize(item), "]")
        for child_dir in child_dirs:
            self.linux_tree_list_dir_demo2(child_dir, deepth + 1)
        os.chdir("../..")
    def make_print_to_file(self,path="./"):
        class Logger(object):
            def __init__(self,filename="d.log",path="./"):
                sys.stdout= io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
                self.terminal = sys.stdout
                self.log = open(os.path.join(path,filename),"a",encoding="utf-8")

            def write(self,message):
                self.terminal.write(message)
                self.log.write(message)

            def flush(self):
                pass

        sys.stdout = Logger(translate_filename,path=path)











    def read_txtfile_to_html(self,htmlname,textname):

        css_template_str = "<style>    #dir1    {background-color:#54aeff;}#dir2{color:#cf222e;}#dir3{color:#000000;}#dir4{color:#0969da;}</style>"
        time.sleep(0.2)
        self.__writeinto_htmlfile(htmlname, css_template_str)
        big_list = []
        list_ret = self.__readDatafile(textname)
        for item in list_ret:
            if item.count("|") == 1:
                ret = "<h4 id='dir1'>{0}</h4>".format(item)
                big_list.append(ret)
            elif item.count("|") == 2:
                ret = "<h4 id='dir2'>{0}</h4>".format(item.replace("     ","&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"))
                big_list.append(ret)

            elif item.count("|") == 3:
                ret = "<h4 id='dir3'>{0}</h4>".format(item)
                big_list.append(ret)
            else:
                ret = "<h4 id='dir4'>{0}</h4>".format(item)
                big_list.append(ret)

        for item in big_list:
            self.__writeinto_htmlfile(htmlname,item)




    def exec(self):
        self.make_print_to_file(path=os.getcwd())
        self.linux_tree_list_dir(path_info)


    def __writeinto_htmlfile(self,filename, data):
        with open(filename, "a", newline="", encoding="utf-8") as f:
            f.write(data)
            f.write("\n")

    def __readDatafile(self,filename):
        line_list = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip("\n")
                line_list.append(line)
        return line_list




if __name__ == "__main__":
    # read dir--->file---->read----> write into html
    path_info = os.path.join(os.getcwd(),pro_name_to_show) #r"C:\CSBook\gin"
    dd_ = copy.deepcopy(translate_filename)
    csb_project_instance = CSBookProject()
    csb_project_instance.make_print_to_file(path=os.getcwd())
    csb_project_instance.linux_tree_list_dir(path_info)


