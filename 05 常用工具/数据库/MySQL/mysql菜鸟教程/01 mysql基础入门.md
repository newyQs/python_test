# mysql 介绍，原理，安装，管理，连接

## 术语
+ 数据库: 数据库是一些关联表的集合。
+ 数据表: 表是数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格。
+ 列: 一列(数据元素) 包含了相同类型的数据, 例如邮政编码的数据。
+ 行：一行（=元组，或记录）是一组相关的数据，例如一条用户订阅的数据。
+ 冗余：存储两倍数据，冗余降低了性能，但提高了数据的安全性。
+ 主键：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
+ 外键：外键用于关联两个表。
+ 复合键：复合键（组合键）将多个列作为一个索引键，一般用于复合索引。
+ 索引：使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录。
+ 参照完整性: 参照的完整性要求关系中不允许引用不存在的实体。与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。


## 安装
https://dev.mysql.com/downloads/mysql/
```
# 检测系统是否自带安装 MySQL:
rpm -qa | grep mysql

# 如果你系统有安装，那可以选择进行卸载:
rpm -e mysql　　// 普通删除模式
rpm -e --nodeps mysql　　// 强力删除模式，如果使用上面命令删除时，提示有依赖的其它文件，则用该命令可以对其进行强力删除

# 下载并安装：
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum update
yum install mysql-server

# 权限设置
chown -R mysql:mysql /var/lib/mysql

# 初始化mysql：
mysqld --initialize

# 启动mysql:
systemctl start mysqld

# 检查mysql运行状态：
systemctl status mysqld
```

## 登录
```
mysql -h 主机名 -u 用户名 -p
```
参数说明：
+ -h : 指定客户端所要登录的 MySQL 主机名, 登录本机(localhost 或 127.0.0.1)该参数可以省略;
+ -u : 登录的用户名;
+ -p : 告诉服务器将会使用一个密码来登录, 如果所要登录的用户名密码为空, 可以忽略此选项。