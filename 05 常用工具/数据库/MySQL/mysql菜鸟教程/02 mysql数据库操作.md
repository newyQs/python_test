# 创建数据库
在登录mysql服务后，使用create语法创建一个数据库，基本语法如下：
```
CREATE DATABASE 数据库名;
```
示例如下：
```
mysql -uroot -p
CREATE DATABASE runoob;
```
或者更全面的创建一个数据库：
```
CREATE DATABASE IF NOT EXISTS RUNOOB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
即创建前先检查数据库是否存在，不存在则创建，并且添加CHARSET和COLLATE的默认配置。


# 删除数据库
删除数据库操作会将数据库中的所有数据都会删除，谨慎操作。这里使用drop关键字删除数据库，语法如下：
```
DROP DATABASE 数据库名;
```
示例如下：
```
DROP DATABASE runoob;
```


# 选择数据库
创建完数据库之后，我们需要选择到该数据库再进行下一步操作。使用use关键词可以选择一个已经存在的数据库，语法如下：
```
USE 数据库名;
```