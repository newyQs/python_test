# MySQL 索引

优势：
- MySQL索引的建立对于MySQL的高效运行是很重要的，索引可以大大提高MySQL的检索速度。
- 索引分单列索引和组合索引。单列索引，即一个索引只包含单个列，一个表可以有多个单列索引，但这不是组合索引。组合索引，即一个索引包含多个列。
- 创建索引时，需要确保该索引是应用在 SQL 查询语句的条件(一般作为 WHERE 子句的条件)。
- 实际上，索引也是一张表，该表保存了主键与索引字段，并指向实体表的记录。

劣势：
- 虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行INSERT、UPDATE和DELETE。
- 因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。
- 建立索引会占用磁盘空间的索引文件。

## 普通索引

创建索引:
```sql
CREATE INDEX indexName ON table_name (column_name);
```

修改表结构(添加索引):
```sql
ALTER table tableName ADD INDEX indexName(columnName);
```

创建表的时候直接指定:
```sql
CREATE TABLE mytable(  
    ID INT NOT NULL,   
    username VARCHAR(16) NOT NULL,  
    INDEX [indexName] (username(length))  
);  
```

```sql
DROP INDEX [indexName] ON mytable; 
```

## 唯一索引
与前面的普通索引类似，不同的就是：索引列的值必须唯一，但允许有空值。
如果是组合索引，则列值的组合必须唯一。它有以下几种创建方式：
```sql
CREATE UNIQUE INDEX indexName ON mytable(username(length));
```

```sql
ALTER table mytable ADD UNIQUE [indexName] (username(length));
```

```sql
CREATE TABLE mytable(  
    ID INT NOT NULL,   
    username VARCHAR(16) NOT NULL,  
    UNIQUE [indexName] (username(length))  
);  
```

## 使用ALTER 命令添加和删除索引

有四种方式来添加数据表的索引：
- ALTER TABLE tbl_name ADD PRIMARY KEY (column_list): 该语句添加一个主键，这意味着索引值必须是唯一的，且不能为NULL。
- ALTER TABLE tbl_name ADD UNIQUE index_name (column_list): 这条语句创建索引的值必须是唯一的（除了NULL外，NULL可能会出现多次）。
- ALTER TABLE tbl_name ADD INDEX index_name (column_list): 添加普通索引，索引值可出现多次。
- ALTER TABLE tbl_name ADD FULLTEXT index_name (column_list):该语句指定了索引为 FULLTEXT ，用于全文索引。

在表中添加索引:
```sql
ALTER TABLE testalter_tbl ADD INDEX (c);
```

使用 DROP 子句来删除索引:
```sql
ALTER TABLE testalter_tbl DROP INDEX c;
```

## 使用 ALTER 命令添加和删除主键

主键作用于列上（可以一个列或多个列联合主键），添加主键索引时，你需要确保该主键默认不为空（NOT NULL）:
```sql
ALTER TABLE testalter_tbl MODIFY i INT NOT NULL;

ALTER TABLE testalter_tbl ADD PRIMARY KEY (i);
```

也可以使用 ALTER 命令删除主键：
```sql
ALTER TABLE testalter_tbl DROP PRIMARY KEY;
```

## 显示索引信息

使用 SHOW INDEX 命令来列出表中的相关的索引信息。可以通过添加 \G 来格式化输出信息:
```sql
SHOW INDEX FROM table_name\G
```