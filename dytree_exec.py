



import os
import time
from csb_config import *
os.system("python contents_translate_.py")


os.system("python get_pro_template.py")


os.remove(translate_filename)


# html ---->   url
#  project name : gin-gonic/gin
# gin-gonic-gin-contents.html  --->/detail/gin-gonic-gin-context.go.html
# gin-gonic-gin-context.go.html    --->/detail/gin-gonic-gin-context.go.html
#

#  1. sitemap
#  2. 同时阅读起来，还是要能有下一个文件的功能
# 3.问题页面排查解决

# 4. 留言板，可以重复循环留言的功能
# 5.要排除的太多，反向思维，只选取编程语言的文件后缀，不是的话就排除即可。