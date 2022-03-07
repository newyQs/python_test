# MySQL 正则表达式

![](img/MySQL%20正则表达式.png)

查找name字段中以'st'为开头的所有数据：
```sql
SELECT name FROM person_tbl WHERE name REGEXP '^st';
```

查找name字段中以'ok'为结尾的所有数据：
```sql
SELECT name FROM person_tbl WHERE name REGEXP 'ok$';
```

查找name字段中包含'mar'字符串的所有数据：
```sql
SELECT name FROM person_tbl WHERE name REGEXP 'mar';
```

查找name字段中以元音字符开头或以'ok'字符串结尾的所有数据：
```sql
SELECT name FROM person_tbl WHERE name REGEXP '^[aeiou]|ok$';
```