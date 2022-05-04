"""
hset(name, key, value)
向键为 name 的散列表中添加映射
name：键名；key：映射键名；value：映射键值
hset('price', 'cake', 5)
向键为 price 的散列表中添加映射关系，cake 的值为 5
1，即添加的映射个数

hsetnx(name, key, value)
如果映射键名不存在，则向键为 name 的散列表中添加映射
name：键名；key：映射键名；value：映射键值
hsetnx('price', 'book', 6)
向键为 price 的散列表中添加映射关系，book 的值为 6
1，即添加的映射个数

hget(name, key)
返回键为 name 的散列表中 key 对应的值
name：键名；key：映射键名
redis.hget('price', 'cake')
获取键为 price 的散列表中键名为 cake 的值
5

hmget(name, keys, *args)
返回键为 name 的散列表中各个键对应的值
name：键名；keys：映射键名列表
redis.hmget('price', ['apple', 'orange'])
获取键为 price 的散列表中 apple 和 orange 的值
[b'3', b'7']

hmset(name, mapping)
向键为 name 的散列表中批量添加映射
name：键名；mapping：映射字典
redis.hmset('price', {'banana': 2, 'pear': 6})
向键为 price 的散列表中批量添加映射
True

hincrby(name, key, amount=1)
将键为 name 的散列表中映射的值增加 amount
name：键名；key：映射键名；amount：增长量
redis.hincrby('price', 'apple', 3)
key 为 price 的散列表中 apple 的值增加 3
6，修改后的值

hexists(name, key)
键为 name 的散列表中是否存在键名为键的映射
name：键名；key：映射键名
redis.hexists('price', 'banana')
键为 price 的散列表中 banana 的值是否存在
True

hdel(name, *keys)
在键为 name 的散列表中，删除键名为键的映射
name：键名；keys：映射键名
redis.hdel('price', 'banana')
从键为 price 的散列表中删除键名为 banana 的映射
True

hlen(name)
从键为 name 的散列表中获取映射个数
name： 键名
redis.hlen('price')
从键为 price 的散列表中获取映射个数
6

hkeys(name)
从键为 name 的散列表中获取所有映射键名
name：键名
redis.hkeys('price')
从键为 price 的散列表中获取所有映射键名
[b'cake', b'book', b'banana', b'pear']

hvals(name)
从键为 name 的散列表中获取所有映射键值
name：键名
redis.hvals('price')
从键为 price 的散列表中获取所有映射键值
[b'5', b'6', b'2', b'6']

hgetall(name)
从键为 name 的散列表中获取所有映射键值对
name：键名
redis.hgetall('price')
从键为 price 的散列表中获取所有映射键值对
{b'cake': b'5', b'book': b'6', b'orange': b'7', b'pear': b'6'}
"""
from redis import Redis

redis = Redis(host='localhost', port=6379, db=0, password='foobared')

redis.hset()

redis.hsetnx()

redis.hget()

redis.hmget()

redis.hmset()

redis.hincrby()

redis.hexists()

redis.hdel()

redis.hlen()

redis.hkeys()

redis.hvals()

redis.hgetall()
