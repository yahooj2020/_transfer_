# 附录：批量转换网址脚本
# 有时候我们拿到的网址缺少http://或者https://开头的信息，用以下 Python 脚本就可以批量给网址加上必要的开头。
#
# 先新建一个名为ip.txt的记事本文件，将缺少头部信息的网址填进去，每行一个网址。
#
# 然后新建一个名为ip2url.py的 Python 脚本，复制粘贴以下代码：

# 保存后打开终端执行以下命令：
#
# python ip2url.py
# 命令执行完后重新打开ip.txt的记事本文件，就可以看到网址前面加上了必要的信息了 。


with open("ip.txt", "r") as f:
    line = f.readlines()

with open("ip.txt", "w") as f2:
    for i in line:
        f2.write('http://' + i)

# 是否另起一行生成 https 开头的地址

with open("ip.txt", "a+") as f3:
    f3.write('\n')

with open("ip.txt", "a+") as f4:
    for i in line:
        f4.write('https://' + i)
