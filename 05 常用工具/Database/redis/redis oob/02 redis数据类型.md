# Redis 数据类型
Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

## String（字符串）
string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。
```
set name lqs
get name

del name
```

## Hash（哈希）
Redis hash 是一个键值(key=>value)对集合。

Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。
```
hmset name f1 lqs f2 lyf
hmset name f1
hmset name f2

del name
```
每个 hash 可以存储 232 -1 键值对（40多亿）。

## List（列表）
Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。
```
lpush name redis
lpush name mongodb
lpush name mysql

lrange name 0 10
```
列表最多可存储 232 - 1 元素 (4294967295, 每个列表可存储40多亿)。

## Set（集合）
Redis 的 Set 是 string 类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。
```
sadd name redis
sadd name mongodb
sadd name mysql
sadd name mysql

smembers name
```
注意：以上实例中 rabbitmq 添加了两次，但根据集合内元素的唯一性，第二次插入的元素将被忽略。

集合中最大的成员数为 232 - 1(4294967295, 每个集合可存储40多亿个成员)。

## zset(sorted set：有序集合)
Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。
不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

zset的成员是唯一的,但分数(score)却可以重复。
```
zadd name 0 mysql
zadd name 0 redis
zadd name 0 mongodb

zrangebyscore name 0 1000
```
