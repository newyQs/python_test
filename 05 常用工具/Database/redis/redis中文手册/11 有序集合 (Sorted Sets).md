# Redis 有序集合 ( Sorted Sets )

Redis 有序集合和集合一样也是 string 类型元素的集合，且不允许重复的成员。

不同的是每个元素都会关联一个 double 类型的分数。Redis 正是通过分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的,但分数 ( score ) 却可以重复。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

集合中最大的成员数为 2**32 – 1 ( 4294967295 ) , 每个集合可存储 40 多亿个成员。

通过 ZADD 命令向 Redis 的有序集合中添加了三个值并关联分数:
```text
redis 127.0.0.1:6379> ZADD rediscomcn 1 redis  
(integer) 0  
redis 127.0.0.1:6379> ZADD rediscomcn 2 cassandra  
(integer) 1  
redis 127.0.0.1:6379> ZADD rediscomcn 3 cassandra  
(integer) 0  
redis 127.0.0.1:6379> ZADD rediscomcn 3 mysql  
(integer) 1  
redis 127.0.0.1:6379> ZADD rediscomcn 4 mysql  
(integer) 0  
redis 127.0.0.1:6379> ZRANGE rediscomcn 0 10 WITHSCORES  
1) "redis"  
2) "1"  
3) "cassandra"  
4) "3"  
5) "mysql"  
6) "4" 
```

## 命令大全

命令	            描述
ZADD	            向有序集合添加一个或多个成员，或者更新已存在成员的分数
ZCARD	            获取有序集合的成员数
ZCOUNT	            计算在有序集合中指定区间分数的成员数
ZINCRBY	            有序集合中对指定成员的分数加上增量 increment
ZINTERSTORE	        计算给定的一个或多个有序集的交集并将结果集存储在新的有序集合 key 中
ZLEXCOUNT	        在有序集合中计算指定字典区间内成员数量
ZRANGE	            通过索引区间返回有序集合成指定区间内的成员
ZRANGEBYLEX	        通过字典区间返回有序集合的成员
ZRANGEBYSCORE	    通过分数返回有序集合指定区间内的成员
ZRANK	            返回有序集合中指定成员的索引
ZREM	            移除有序集合中的一个或多个成员
ZREMRANGEBYLEX	    移除有序集合中给定的字典区间的所有成员
ZREMRANGEBYRANK	    移除有序集合中给定的排名区间的所有成员
ZREMRANGEBYSCORE	移除有序集合中给定的分数区间的所有成员
ZREVRANGE	        返回有序集中指定区间内的成员，通过索引，分数从高到底
ZREVRANGEBYSCORE	返回有序集中指定分数区间内的成员，分数从高到低排序
ZREVRANK	        返回有序集合中指定成员的排名，有序集成员按分数值递减(从大到小)排序
ZSCORE	            返回有序集中，成员的分数值
ZUNIONSTORE	        计算一个或多个有序集的并集，并存储在新的 key 中
ZSCAN	            迭代有序集合中的元素（包括元素成员和元素分值）