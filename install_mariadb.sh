#坑一：CentOS 7不能再用开源的MySql了，应该安装Mariadb
#
#解决办法：
#
#        一顿操作猛如虎，发现我是250，买了个华为云服务器（CentOS 7），直接下载mysql包，解压，安装，按照网上的帖子一步步操作，直到最后卸载了mysql，因为CentOS 7上不能再安装开源的mysql了（也就是不能用免费的了o(*￣︶￣*)o），你想要的可能是安装mariadb！
#
#【mariadb安装步骤】：
#
#1、准备工作
#
#1.1、确保你的linux服务器外网是通的，方法很简单，ping www.baidu.com
#
#
#
#1.2、查看已安装的包
rpm -qa | grep mysql;

#
#        命令：
#
#
#
# 1.3、如果存在已安装，逐个卸载掉这些包
#
#        命令：rpm -e --nodeps mariadb-xxxx。。。。
#
#2、安装mariadb
#
#2.1、安装


yum install mariadb-server -y ;

#        全部卸载完后执行1.2的命令确认卸载干净。
#

#
#        命令：
#
#2.2、 如果下载不成功，清理安装文件
#
#        命令：yum clean all
#
#2.3、 确认下载安装
#
#
#
# 2.4、安装完成
#
#   source  /mnt/create_tb.sql;


#

systemctl start mariadb;
systemctl enable mariadb;

# 此时执行1.2的命令，可以查看安装的内容！
#
#3、 数据库常用命令
#        命令：
#        1. 启动命令  systemctl start mariadb
#        2. 重启命令  systemctl restart mariadb
#        3. 关闭命令  systemctl stop mariadb
#        4. 开机自起  systemctl enable mariadb
#        5. 关闭自起  systemctl disable mariadb
#
#4、初始化数据库
#
#        4.1、执行命令：mysql_secure_installation
#
#        提示输入root用户密码
#
#
#
#安装后初次进入，密码为空，直接回车就可以了 ！
#
#        4.2、设置root用户密码
#
#        然后弹出是否设置root用户密码，输入y，然后回车
#
#
#
# 输入新密码，回车后在重复输入确认密码，回车完成密码设置，然后弹出是否删除匿名用户，输入y，回车完成匿名用户删除
#
#        4.3、删除匿名用户
#
#
#
#        4.4、允许root远程登录
#
#
#
#        输入y，回车，允许root远程登录，然后选择是否删除test测试库
#
#        4.5、删除test测试库
#
#
#
# 输入y，回车，删除test库，然后选择是否新加载权限
#
#        4.6、重新加载权限
#
#
#
# 输入y，回车，安装完成！
#
#坑二、数据库远程连接需要的两个配置（数据库允许用户远程访问、防护墙上要将数据库端口3306设置成ACCEPT）
#
#解决办法：
#
#一、解决用户远程登录
#
#（一）、执行命令：mysql -u root -p
#提示输入root用户密码，输入后回车，成功登录Mariadb，
#
#（二）、执行命令：GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '你的root密码' WITH GRANT OPTION;
#
#二、解决防火墙问题
#
#在网上查询到需要修改/etc/sysconfig/iptables配置文件，文件中默认放开了22端口，复制后粘贴在这条配置的下面（有网友说只能在下面，上面不行，我没验证），并修改端口为3306，如下：
#
#-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
#-A INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT
#！！！！可实际我们在我们打开/etc/sysconfig目录后就迷路了，因为没有找到iptables这个文件，有一个iptables-config的文件，我想到是不是操作系统版本问题，打开后发现配置和网友的帖子完全对不上，这是坑的关键，CentOS 7的默认防火墙是firewall 防火墙，不是ptables防火墙，我的解决办法是先修改防火墙为iptables，步骤如下：
#
#1、停止 firewall 服务
#systemctl stop firewalld
#2、注销 firewall 服务
#systemctl mask firewalld
#3、安装 iptables 服务
#yum install -y iptables
#yum install iptables-services
#4、启动 iptables 服务
#systemctl start iptables
#或者
#service iptables start
#5、设置 iptables 开机自启动
#systemctl enable iptables
#6、查看 iptables 状态
#systemctl status iptables
#或者
#service iptables status
#7、此时/etc/sysconfig/iptables已经存在了
#
#按上面的办法修改/etc/sysconfig/iptables，如下
#
#。。。省略其他内容。。。
#-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
#-A INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT
#。。。省略其他内容。。。
#
#坑三、云服务器需要防火墙端口穿透
#
#经过上面一顿折腾，理论上已经可以在自己电脑上用Navicat等工具连接数据库了，遗憾的是仍然连不上，找了半天，突然灵光一现，想到我最开始说的场景，我是买的一个云服务器，应该是云上的端口没有穿透进去，登录云管理平台的管理端，做一个端口映射，让外面能穿透到3306端口完美解决！
#
#
# 以上是我在CentOS 7 上想要安装mysql，最后安装了Mariadb的过程，做笔记备查，希望能给跟我一样的小白提供一定帮助，如有错漏，欢迎指正！！！
#
#文章知识点与官方知识档案匹配，可进一步学习相关知识
#CS入门技能树Linux入门在线安装软件20918 人正在系统学习中



