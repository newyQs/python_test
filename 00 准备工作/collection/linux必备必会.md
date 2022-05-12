(1) tail

tail [参数]

tail -n 100 <file.name>
tail -f -n 200 <file.name>

(2) less

less [参数] [文件]

less <file.name>
    b：向后翻一页
    y：向前翻一页
    回车键：滚动一页
    空格键：滚动一行


(3) ssh

ssh [参数] [主机]

ssh 202.102.240.88
ssh -l test 202.102.220.88
ssh 202.102.220.88 /sbin/fdisk -l

ssh root@10.61.67.8
ssh -p 8081 10.61.67.8


(4) scp

从远程复制文件到本地目录：
    scp root@192.168.10.10:/opt/soft/rhel-server-7.3-x86_64.tar.gz /opt/soft/

从远程复制目录到本地：
    scp -r root@10.10.10.10:/opt/soft/mysql /opt/soft/

上传本地文件到远程机器指定目录：
    scp /opt/soft/rhel-server-7.3-x86_64.tar.gz root@192.168.10.10:/opt/soft/scptest

上传本地目录到远程机器指定目录：
    scp -r /opt/soft/mysql root@192.168.10.10:/opt/soft/scptest

保留文件的最后修改时间，最后访问时间和权限模式：
    scp -p /root/install.log root@192.168.10.10:/tmp

(5) ps

ps [参数]

显示所有进程：
    ps -aux
    ps -aux | grep 7700
    ps -aux > ps.txt

查看特定进程信息：
    ps -ef | grep ssh
    ps -aux | grep ssh

显示指定用户信息：
    ps -u root

按 CPU 资源的使用量对进程进行排序：
    ps aux | sort -nk 3

按内存资源的使用量对进程进行排序：
    ps aux | sort -rnk 4

(6) netstat

netstat [参数]

-a (all)显示所有选项，默认不显示LISTEN相关
-t (tcp)仅显示tcp相关选项
-u (udp)仅显示udp相关选项
-n 拒绝显示别名，能显示数字的全部转化成数字。
-l 仅列出有在 Listen (监听) 的服务状态
-p 显示建立相关链接的程序名
-r 显示路由信息，路由表
-e 显示扩展信息，例如uid等
-s 按各个协议进行统计
-c 每隔一个固定时间，执行该netstat命令。

1. 列出所有端口 (包括监听和未监听的)
列出所有端口：
    netstat -a

列出所有 tcp 端口：
    netstat -at

列出所有 udp 端口：
    netstat -au

2. 列出所有处于监听状态的 Sockets
只显示监听端口：
    netstat -l

只列出所有监听 tcp 端口
    netstat -lt

只列出所有监听 udp 端口
    netstat -lu

(7) tar

tar [参数] [文件或目录]

将所有.jpg的文件打成一个名为all.tar的包：
    tar -cf all.tar *.jpg

打包文件之后删除源文件：
    tar -cvf linuxcool.tar linuxcool --remove-files

打包文件以后，以 gzip 压缩：
    tar -zcvf log.tar.gz linuxcool.log