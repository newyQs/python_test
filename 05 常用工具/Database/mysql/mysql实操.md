https://www.yiibai.com/mysql

系统内置的数据库有：
+ information_schema
+ mysql
+ performance_schema
+ sys

1. 查看mysql中有哪些数据库？
```sql
show databases;

show databases like "my%";
```

2. 选择一个数据库，查看该数据库的结构，该数据库里有哪些表？
```sql
use mysql;

show tables;

show tables from mysql;
```

3. 查看表的结构
```sql

```

4, 创建数据库与删除数据库
```sql
create database db_test(
  id int auto_increment primary key,
  user varchar(20) not null,
  age int not null,
  gengder varchar(20) not null,
)engine='innodb';


drop database db_test;
```