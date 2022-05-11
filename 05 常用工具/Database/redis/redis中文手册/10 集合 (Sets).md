# Redis 集合 ( Sets )

Redis 的 Set 是 string 类型的无序集合。

集合成员是唯一的，这就意味着集合中没有重复的数据。

在 Redis 中，添加、删除和查找的时间复杂都是 O(1)（不管 Set 中包含多少元素）。

集合中最大的成员数为 232 – 1 (4294967295), 每个集合可存储 40 多亿个成员。

通过 SADD 命令向名为 rediscomcn 的集合插入的三个元素:
```text
redis 127.0.0.1:6379> SADD rediscomcn db2  
(integer) 1  
redis 127.0.0.1:6379> SADD rediscomcn mongodb  
(integer) 1  
redis 127.0.0.1:6379> SADD rediscomcn db2  
(integer) 0  
redis 127.0.0.1:6379> SADD rediscomcn cassandra  
(integer) 1  
redis 127.0.0.1:6379> SMEMBERS rediscomcn  
1) "cassandra"  
2) "db2"  
3) "mongodb"  
```

## 命令大全

命令	        描述
SADD	        向集合添加一个或多个成员
SCARD	        获取集合的成员数
SDIFF	        返回给定所有集合的差集
SDIFFSTORE	    返回给定所有集合的差集并存储在 destination 中
SINTER	        返回给定所有集合的交集
SINTERSTORE	    返回给定所有集合的交集并存储在 destination 中
SISMEMBER	    判断 member 元素是否是集合 key 的成员
SMEMBERS	    返回集合中的所有成员
SMOVE	        将 member 元素从 source 集合移动到 destination 集合
SPOP	        移除并返回集合中的一个随机元素
SRANDMEMBER	    返回集合中一个或多个随机数
SREM	        移除集合中一个或多个成员
SUNION	        返回所有给定集合的并集
SUNIONSTORE	    所有给定集合的并集存储在 destination 集合中
SSCAN	        迭代集合中的元素