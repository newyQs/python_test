# Redis 哈希 ( Hashes )

Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。

每个哈希键中可以存储多达 40 亿个字段值对。

```text
127.0.0.1:6379> HMSET rediscomcn name "redis" url "http://www.redis.com.cn" rank 1 visitors 240000000
OK
127.0.0.1:6379> HGETALL rediscomcn
1) "name"
2) "redis"
3) "url"
4) "http://www.qq.com"
5) "rank"
6) "1"
7) "visitors"
8) "230000000"
```
在上面的例子中，“rediscomcn” 是 Redis 哈希，它包含详细信息（name，url，rank，visitors）属性。

## 命令大全
命令	        描述
HDEL	        删除一个或多个哈希表字段
HEXISTS	        查看哈希表 key 中，指定的字段是否存在
HGET	        获取存储在哈希表中指定字段的值
HGETALL	        获取在哈希表中指定 key 的所有字段和值
HINCRBY	        为哈希表 key 中的指定字段的整数值加上增量 increment
HINCRBYFLOAT	为哈希表 key 中的指定字段的浮点数值加上增量 increment
HKEYS	        获取所有哈希表中的字段
HLEN	        获取哈希表中字段的数量
HMGET	        获取所有给定字段的值
HMSET	        同时将多个 field-value (域-值)对设置到哈希表 key 中
HSET	        将哈希表 key 中的字段 field 的值设为 value
HSETNX	        只有在字段 field 不存在时，设置哈希表字段的值
HVALS	        获取哈希表中所有值
HSCAN	        迭代哈希表中的键值对
HSTRLEN	        返回哈希表 key 中， 与给定域 field 相关联的值的字符串长度
