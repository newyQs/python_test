# 数据表数据的增删改查操作

## 插入数据
插入数据，使用 INSERT INTO 语法，通用语法如下：
```
插入单条数据：
INSERT INTO 数据表名(field1, field2, field3, ...) VALUES (value1, value2, value3, ...);

插入多条数据：
INSERT INTO 数据表名(field1, field2, field3, ...) VALUES (value1, value2, value3, ...), 
                    (field1, field2, field3, ...) VALUES (value1, value2, value3, ...), 
                    ...;   

插入完整数据：
INSERT INTO 数据表名 VALUES (value1, value2, value3, ...);

其他方法：
INSERT INTO 数据表名 SET field1=value1,
                         field2=value2,
                         field3=value3,
                         ...;          
```
如果数据是字符型，必须使用单引号或者双引号，如："value"。

示例如下：向 runoob_tbl 表插入三条数据
```
root@host# mysql -u root -p password;
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> INSERT INTO runoob_tbl 
    -> (runoob_title, runoob_author, submission_date)
    -> VALUES
    -> ("学习 PHP", "菜鸟教程", NOW());
Query OK, 1 rows affected, 1 warnings (0.01 sec)
mysql> INSERT INTO runoob_tbl
    -> (runoob_title, runoob_author, submission_date)
    -> VALUES
    -> ("学习 MySQL", "菜鸟教程", NOW());
Query OK, 1 rows affected, 1 warnings (0.01 sec)
mysql> INSERT INTO runoob_tbl
    -> (runoob_title, runoob_author, submission_date)
    -> VALUES
    -> ("JAVA 教程", "RUNOOB.COM", '2016-05-06');
Query OK, 1 rows affected (0.00 sec)
mysql>
```

## 删除数据
删除数据使用 DELETE FROM 语法，通用语法如下：
```
DELETE FROM 数据表名 WHERE 筛选条件;
```
+ 如果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。
+ 你可以在 WHERE 子句中指定任何筛选条件
+ 你可以在单个表中一次性删除记录。

当你想删除数据表中指定的记录时 WHERE 子句是非常有用的。

示例如下：
```
mysql> use RUNOOB;
Database changed
mysql> DELETE FROM runoob_tbl WHERE runoob_id=3;
Query OK, 1 row affected (0.23 sec)
```

delete，drop，truncate 都有删除表的作用，区别在于：
1. delete 和 truncate 仅仅删除表数据，drop 连表数据和表结构一起删除，打个比方，delete 是单杀，truncate 是团灭，drop 是把电脑摔了。
2. delete 是 DML 语句，操作完以后如果没有不想提交事务还可以回滚，truncate 和 drop 是 DDL 语句，操作完马上生效，不能回滚，打个比方，delete 是发微信说分手，后悔还可以撤回，truncate 和 drop 是直接扇耳光说滚，不能反悔。
3. 执行的速度上，drop>truncate>delete，打个比方，drop 是神舟火箭，truncate 是和谐号动车，delete 是自行车。

## 更新数据
更新数据使用 UPDATE SET 语法，通用语法如下：
```
UPDATE 数据表名 SET field1=new_value1,
                    field2=new_value2,
                    field3=new_value3,
                    ...
WHERE 筛选条件;
```
+ 你可以同时更新一个或多个字段。
+ 你可以在 WHERE 子句中指定任何条件。
+ 你可以在一个单独表中同时更新数据。

当你需要更新数据表中指定行的数据时 WHERE 子句是非常有用的。

示例如下：
```
mysql> UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3;
Query OK, 1 rows affected (0.01 sec)
 
mysql> SELECT * from runoob_tbl WHERE runoob_id=3;
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
| 3         | 学习 C++   | RUNOOB.COM    | 2016-05-06      |
+-----------+--------------+---------------+-----------------+
1 rows in set (0.01 sec)
```

## 查询数据
查询数据使用 SELECT FROM 语法，通用语法如下：
```
SELECT field1, field2, ... FROM 数据表名
WHERE 筛选条件
LIMIT N
OFFSET M;
```
+ 查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。
+ SELECT 命令可以读取一条或者多条记录。
+ 你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据
+ 你可以使用 WHERE 语句来包含任何条件。
+ 你可以使用 LIMIT 属性来设定返回的记录数。
+ 你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。