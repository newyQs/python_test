# 数据表数据的增删改查操作

## 插入数据
插入数据，使用 INSERT INTO 语法，通用语法如下：
```sql
-- 插入单条数据：
INSERT INTO 数据表名(field1, field2, field3, ...) VALUES (value1, value2, value3, ...);

-- 插入多条数据：
INSERT INTO 数据表名(field1, field2, field3, ...) VALUES (value1, value2, value3, ...), 
                    (field1, field2, field3, ...) VALUES (value1, value2, value3, ...), 
                    ...;   

-- 插入完整数据：
INSERT INTO 数据表名 VALUES (value1, value2, value3, ...);

-- 其他方法：
INSERT INTO 数据表名 SET field1=value1,
                         field2=value2,
                         field3=value3,
                         ...;          
```
注意：如果数据是字符型，必须使用单引号或者双引号，如："value"。

例如：向 runoob_tbl 表插入三条数据
```sql
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
```sql
DELETE FROM 数据表名 WHERE 筛选条件;
```
+ 如果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。
+ 你可以在 WHERE 子句中指定任何筛选条件
+ 你可以在单个表中一次性删除记录。

当你想删除数据表中指定的记录时 WHERE 子句是非常有用的。

示例如下：
```sql
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
```sql
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
```sql
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
```sql
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

## NULL值的处理
```sql
root@host# mysql -u root -p password;
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> create table runoob_test_tbl
    -> (
    -> runoob_author varchar(40) NOT NULL,
    -> runoob_count  INT
    -> );
Query OK, 0 rows affected (0.05 sec)
mysql> INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('RUNOOB', 20);
mysql> INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values (docker菜鸟教程, NULL);
mysql> INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('Google', NULL);
mysql> INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('FK', 20);
 
mysql> SELECT * from runoob_test_tbl;
+---------------+--------------+
| runoob_author | runoob_count |
+---------------+--------------+
| RUNOOB        | 20           |
| 菜鸟教程      | NULL         |
| Google        | NULL         |
| FK            | 20           |
+---------------+--------------+
4 rows in set (0.01 sec)
```
以下实例中你可以看到 = 和 != 运算符是不起作用的：
```sql
mysql> SELECT * FROM runoob_test_tbl WHERE runoob_count = NULL;
Empty set (0.00 sec)
mysql> SELECT * FROM runoob_test_tbl WHERE runoob_count != NULL;
Empty set (0.01 sec)
```
查找数据表中 runoob_test_tbl 列是否为 NULL，必须使用 IS NULL 和 IS NOT NULL，如下实例：
```sql
mysql> SELECT * FROM runoob_test_tbl WHERE runoob_count IS NULL;
+---------------+--------------+
| runoob_author | runoob_count |
+---------------+--------------+
| 菜鸟教程      | NULL         |
| Google        | NULL         |
+---------------+--------------+
2 rows in set (0.01 sec)
 
mysql> SELECT * from runoob_test_tbl WHERE runoob_count IS NOT NULL;
+---------------+--------------+
| runoob_author | runoob_count |
+---------------+--------------+
| RUNOOB        | 20           |
| FK            | 20           |
+---------------+--------------+
2 rows in set (0.01 sec)
```

## ALTER命令
当我们需要修改数据表名或者修改数据表字段时，就需要使用到MySQL ALTER命令。

先创建一张表，表名为：testalter_tbl。
```sql
root@host# mysql -u root -p password;
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> create table testalter_tbl
    -> (
    -> i INT,
    -> c CHAR(1)
    -> );
Query OK, 0 rows affected (0.05 sec)
mysql> SHOW COLUMNS FROM testalter_tbl;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| i     | int(11) | YES  |     | NULL    |       |
| c     | char(1) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.00 sec)
```
### 删除，添加或修改表字段
如下命令使用了 ALTER 命令及 DROP 子句来删除以上创建表的 i 字段：
```sql
ALTER TABLE testalter_tbl  DROP i;
```
如果数据表中只剩余一个字段则无法使用DROP来删除字段。

MySQL 中使用 ADD 子句来向数据表中添加列，如下实例在表 testalter_tbl 中添加 i 字段，并定义数据类型:
```sql
ALTER TABLE testalter_tbl ADD i INT;
```
执行以上命令后，i 字段会自动添加到数据表字段的末尾。
```sql
mysql> SHOW COLUMNS FROM testalter_tbl;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| c     | char(1) | YES  |     | NULL    |       |
| i     | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.00 sec)
```
如果你需要指定新增字段的位置，可以使用MySQL提供的关键字 FIRST (设定位第一列)， AFTER 字段名（设定位于某个字段之后）。

尝试以下 ALTER TABLE 语句, 在执行成功后，使用 SHOW COLUMNS 查看表结构的变化：
```sql
ALTER TABLE testalter_tbl DROP i;
ALTER TABLE testalter_tbl ADD i INT FIRST;
ALTER TABLE testalter_tbl DROP i;
ALTER TABLE testalter_tbl ADD i INT AFTER c;
```
FIRST 和 AFTER 关键字可用于 ADD 与 MODIFY 子句，所以如果你想重置数据表字段的位置就需要先使用 DROP 删除字段然后使用 ADD 来添加字段并设置位置。

### 修改字段类型及名称
如果需要修改字段类型及名称, 你可以在ALTER命令中使用 MODIFY 或 CHANGE 子句 。

例如，把字段 c 的类型从 CHAR(1) 改为 CHAR(10)，可以执行以下命令:
```sql
ALTER TABLE testalter_tbl MODIFY c CHAR(10);
```
使用 CHANGE 子句, 语法有很大的不同。 在 CHANGE 关键字之后，紧跟着的是你要修改的字段名，然后指定新字段名及类型。尝试如下实例：
```sql
ALTER TABLE testalter_tbl CHANGE i j BIGINT;

ALTER TABLE testalter_tbl CHANGE j j INT;
```

### ALTER TABLE 对 Null 值和默认值的影响
当你修改字段时，你可以指定是否包含值或者是否设置默认值。

以下实例，指定字段 j 为 NOT NULL 且默认值为100 。
```sql
mysql> ALTER TABLE testalter_tbl 
    -> MODIFY j BIGINT NOT NULL DEFAULT 100;
```
如果你不设置默认值，MySQL会自动设置该字段默认为 NULL。

### 修改字段默认值
你可以使用 ALTER 来修改字段的默认值，尝试以下实例：
```sql
mysql> ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
mysql> SHOW COLUMNS FROM testalter_tbl;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| c     | char(1) | YES  |     | NULL    |       |
| i     | int(11) | YES  |     | 1000    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.00 sec)
```
你也可以使用 ALTER 命令及 DROP子句来删除字段的默认值，如下实例：
```sql
mysql> ALTER TABLE testalter_tbl ALTER i DROP DEFAULT;
mysql> SHOW COLUMNS FROM testalter_tbl;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| c     | char(1) | YES  |     | NULL    |       |
| i     | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.00 sec)
Changing a Table Type:
```
修改数据表类型，可以使用 ALTER 命令及 TYPE 子句来完成。尝试以下实例，我们将表 testalter_tbl 的类型修改为 MYISAM ：

注意：查看数据表类型可以使用 SHOW TABLE STATUS 语句。
```sql
mysql> ALTER TABLE testalter_tbl ENGINE = MYISAM;
mysql>  SHOW TABLE STATUS LIKE 'testalter_tbl'\G
*************************** 1. row ****************
           Name: testalter_tbl
           Type: MyISAM
     Row_format: Fixed
           Rows: 0
 Avg_row_length: 0
    Data_length: 0
Max_data_length: 25769803775
   Index_length: 1024
      Data_free: 0
 Auto_increment: NULL
    Create_time: 2007-06-03 08:04:36
    Update_time: 2007-06-03 08:04:36
     Check_time: NULL
 Create_options:
        Comment:
1 row in set (0.00 sec)
```

### 修改表名
如果需要修改数据表的名称，可以在 ALTER TABLE 语句中使用 RENAME 子句来实现。

尝试以下实例将数据表 testalter_tbl 重命名为 alter_tbl：
```sql
ALTER TABLE testalter_tbl RENAME TO alter_tbl;
```
ALTER 命令还可以用来创建及删除MySQL数据表的索引

alter其他用途：
1. 修改存储引擎：修改为myisam
```sql
alter table tableName engine=myisam;
```
2. 删除外键约束：keyName是外键别名
```sql
alter table tableName drop foreign key keyName;
```
3. 修改字段的相对位置：这里name1为想要修改的字段，type1为该字段原来类型，
   first和after二选一，这应该显而易见，first放在第一位，after放在name2字段后面
```sql
alter table tableName modify name1 type1 first|after name2;
```