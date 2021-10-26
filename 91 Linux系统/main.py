'''
https://www.linuxcool.com/
yum - rpm
apt -

输入下面配置：
sudo service network-manager stop
sudo rm /var/lib/NetworkManager/NetworkManager.state
sudo service network-manager start
sudo gedit /etc/NetworkManager/NetworkManager.conf     —— 打开配置文件后把false改成true
sudo service network-manager restart

文件和目录的操作：

创建目录
 mkdir <dir_name>

创建多级目录
 mkdir -p <dir_name01/dir_name02>

删除空目录
 rmdir <dir_name>

删除多级空目录
 rmdir -p <dir_name01/dir_name02>

删除非空目录
 rm -rf <目录/文件>

删除当前目录下所有文件
 rm -rf *

删除系统中所有文件
 rm -rf /*

创建文件
 touch <file_name>

重命名文件
 mv <file_name1> <file_name2>
 cp -f <file_name1> <file_name2>

重命名目录
 mv </dir_name1 > </dir_name2>

复制文件

复制目录

6.查看文件，文件内容
7.查找制定目录，查找指定文件位置

'''
