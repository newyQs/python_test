"""
rpush(name, *values)
在键为 name 的列表末尾添加值为 value 的元素，可以传多个
name：键名；values：值
redis.rpush('list', 1, 2, 3)
向键为 list 的列表尾添加 1、2、3
3，列表大小

lpush(name, *values)
在键为 name 的列表头添加值为 value 的元素，可以传多个
name：键名；values：值
redis.lpush('list', 0)
向键为 list 的列表头部添加 0
4，列表大小

llen(name)
返回键为 name 的列表的长度
name：键名
redis.llen('list')
返回键为 list 的列表的长度
4

lrange(name, start, end)
返回键为 name 的列表中 start 至 end 之间的元素
name：键名；start：起始索引；end：终止索引
redis.lrange('list', 1, 3)
返回起始索引为 1 终止索引为 3 的索引范围对应的列表
[b'3', b'2', b'1']

ltrim(name, start, end)
截取键为 name 的列表，保留索引为 start 到 end 的内容
name：键名；start：起始索引；end：终止索引
ltrim('list', 1, 3)
保留键为 list 的索引为 1 到 3 的元素
True

lindex(name, index)
返回键为 name 的列表中 index 位置的元素
name：键名；index：索引
redis.lindex('list', 1)
返回键为 list 的列表索引为 1 的元素
b’2’

lset(name, index, value)
给键为 name 的列表中 index 位置的元素赋值，越界则报错
name：键名；index：索引位置；value：值
redis.lset('list', 1, 5)
将键为 list 的列表中索引为 1 的位置赋值为 5
True

lrem(name, count, value)
删除 count 个键的列表中值为 value 的元素
name：键名；count：删除个数；value：值
redis.lrem('list', 2, 3)
将键为 list 的列表删除两个 3
1，即删除的个数

lpop(name)
返回并删除键为 name 的列表中的首元素
name：键名
redis.lpop('list')
返回并删除名为 list 的列表中的第一个元素
b'5'

rpop(name)
返回并删除键为 name 的列表中的尾元素
name：键名
redis.rpop('list')
返回并删除名为 list 的列表中的最后一个元素
b'2'

blpop(keys, timeout=0)
返回并删除名称在 keys 中的 list 中的首个元素，如果列表为空，则会一直阻塞等待
keys：键列表；timeout： 超时等待时间，0 为一直等待
redis.blpop('list')
返回并删除键为 list 的列表中的第一个元素
[b'5']

brpop(keys, timeout=0)
返回并删除键为 name 的列表中的尾元素，如果 list 为空，则会一直阻塞等待
keys：键列表；timeout：超时等待时间，0 为一直等待
redis.brpop('list')
返回并删除名为 list 的列表中的最后一个元素
[b'2']

rpoplpush(src, dst)
返回并删除名称为 src 的列表的尾元素，并将该元素添加到名称为 dst 的列表头部
src：源列表的键；dst：目标列表的 key
redis.rpoplpush('list', 'list2')
将键为 list 的列表尾元素删除并将其添加到键为 list2 的列表头部，然后返回
b'2'
"""
from redis import Redis

redis = Redis(host='localhost', port=6379, db=0, password='foobared')

redis.rpush()

redis.lpush()

redis.llen()

redis.lrange()

redis.ltrim()

redis.lindex()

redis.lset()

redis.lrem()

redis.lpop()

redis.rpop()

redis.blpop()

redis.brpop()

redis.rpoplpush()


