# 创建数据表
使用 CREATE 关键字，通用用法，如下：
```
CREATE TABLE 数据表名(
    列名1 列类型1,
    列名2 列类型2,
    ...
)
```
示例如下：
```
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
实例解析：
+ 如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为NULL ，就会报错。
+ AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。
+ PRIMARY KEY关键字用于定义列为主键。 您可以使用多列来定义主键，列间以逗号分隔。
+ ENGINE 设置存储引擎，CHARSET 设置编码。

在命令行中创建：
```
root@host# mysql -u root -p
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> CREATE TABLE runoob_tbl(
   -> runoob_id INT NOT NULL AUTO_INCREMENT,
   -> runoob_title VARCHAR(100) NOT NULL,
   -> runoob_author VARCHAR(40) NOT NULL,
   -> submission_date DATE,
   -> PRIMARY KEY ( runoob_id )
   -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
Query OK, 0 rows affected (0.16 sec)
mysql>
```

# 删除数据表
使用 DROP 关键字，通用语法如下：
```
DROP TABLE 数据表名;
```
示例如下：
```
root@host# mysql -u root -p
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> DROP TABLE runoob_tbl;
Query OK, 0 rows affected (0.8 sec)
mysql>
```

# 修改数据表
当我们需要修改数据表名或者修改数据表字段时，就需要使用到MySQL ALTER命令