# Redis 列表 ( Lists )

Redis 列表是按插入顺序排序的字符串列表。可以在列表的头部（左边）或尾部（右边）添加元素。

列表可以包含超过 40 亿 个元素 ( 2**32 - 1 )。

用 LPUSH 命令将三个值插入了名为 language 的列表当中:
```text
redis 127.0.0.1:6379> LPUSH javatpoint sql  
(integer) 1  
redis 127.0.0.1:6379> LPUSH javatpoint mysql  
(integer) 2  
redis 127.0.0.1:6379> LPUSH javatpoint cassandra  
(integer) 3  
redis 127.0.0.1:6379> LRANGE javatpoint 0 10  
1) "cassandra"  
2) "mysql"  
3) "sql"  
redis 127.0.0.1:6379>  
```

## 命令大全

命令	    描述
BLPOP	    移出并获取列表的第一个元素
BRPOP	    移出并获取列表的最后一个元素
BRPOPLPUSH	从列表中弹出一个值，并将该值插入到另外一个列表中并返回它
LINDEX	    通过索引获取列表中的元素
LINSERT	    在列表的元素前或者后插入元素
LLEN	    获取列表长度
LPOP	    移出并获取列表的第一个元素
LPUSH	    将一个或多个值插入到列表头部
LPUSHX	    将一个值插入到已存在的列表头部
LRANGE	    获取列表指定范围内的元素
LREM	    移除列表元素
LSET	    通过索引设置列表元素的值
LTRIM	    对一个列表进行修剪(trim)
RPOP	    移除并获取列表最后一个元素
RPOPLPUSH	移除列表的最后一个元素，并将该元素添加到另一个列表并返回
RPUSH	    在列表中添加一个或多个值
RPUSHX	    为已存在的列表添加值