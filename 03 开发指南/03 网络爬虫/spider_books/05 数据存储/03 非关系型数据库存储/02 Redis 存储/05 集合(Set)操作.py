"""
sadd(name, *values)
向键为 name 的集合中添加元素
name：键名；values：值，可为多个
redis.sadd('tags', 'Book', 'Tea', 'Coffee')
向键为 tags 的集合中添加 Book、Tea 和 Coffee 这 3 个内容
3，即插入的数据个数

srem(name, *values)
从键为 name 的集合中删除元素
name：键名；values：值，可为多个
redis.srem('tags', 'Book')
从键为 tags 的集合中删除 Book
1，即删除的数据个数

spop(name)
随机返回并删除键为 name 的集合中的一个元素
name：键名
redis.spop('tags')
从键为 tags 的集合中随机删除并返回该元素
b'Tea'

smove(src, dst, value)
从 src 对应的集合中移除元素并将其添加到 dst 对应的集合中
src：源集合；dst：目标集合；value：元素值
redis.smove('tags', 'tags2', 'Coffee')
从键为 tags 的集合中删除元素 Coffee 并将其添加到键为 tags2 的集合
True

scard(name)
返回键为 name 的集合的元素个数
name：键名
redis.scard('tags')
获取键为 tags 的集合中的元素个数
3

sismember(name, value)
测试 member 是否是键为 name 的集合的元素
name：键值
redis.sismember('tags', 'Book')
判断 Book 是否是键为 tags 的集合元素
True

sinter(keys, *args)
返回所有给定键的集合的交集
keys：键列表
redis.sinter(['tags', 'tags2'])
返回键为 tags 的集合和键为 tags2 的集合的交集
{b'Coffee'}

sinterstore(dest, keys, *args)
求交集并将交集保存到 dest 的集合
dest：结果集合；keys：键列表
redis.sinterstore('inttag', ['tags', 'tags2'])
求键为 tags 的集合和键为 tags2 的集合的交集并将其保存为 inttag
1

sunion(keys, *args)
返回所有给定键的集合的并集
keys：键列表
redis.sunion(['tags', 'tags2'])
返回键为 tags 的集合和键为 tags2 的集合的并集
{b'Coffee', b'Book', b'Pen'}

sunionstore(dest, keys, *args)
求并集并将并集保存到 dest 的集合
dest：结果集合；keys：键列表
redis.sunionstore('inttag', ['tags', 'tags2'])
求键为 tags 的集合和键为 tags2 的集合的并集并将其保存为 inttag
3

sdiff(keys, *args)
返回所有给定键的集合的差集
keys：键列表
redis.sdiff(['tags', 'tags2'])
返回键为 tags 的集合和键为 tags2 的集合的差集
{b'Book', b'Pen'}

sdiffstore(dest, keys, *args)
求差集并将差集保存到 dest 集合
dest：结果集合；keys：键列表
redis.sdiffstore('inttag', ['tags', 'tags2'])
求键为 tags 的集合和键为 tags2 的集合的差集并将其保存为 inttag`
3

smembers(name)
返回键为 name 的集合的所有元素
name：键名
redis.smembers('tags')
返回键为 tags 的集合的所有元素
{b'Pen', b'Book', b'Coffee'}

srandmember(name)
随机返回键为 name 的集合中的一个元素，但不删除元素
name：键值
redis.srandmember('tags')
随机返回键为 tags 的集合中的一个元素
"""
from redis import Redis

redis = Redis(host='localhost', port=6379, db=0, password='foobared')

redis.sadd()

redis.srem()

redis.spop()

redis.smove()

redis.scard()

redis.sismember()

redis.sinter()

redis.sinterstore()

redis.sunion()

redis.sunionstore()

redis.sdiff()

redis.sdiffstore()

redis.smembers()

redis.srandmember()

