"""
set(name, value)
给数据库中键为 name 的 string 赋予值 value
name: 键名；value: 值
redis.set('name', 'Bob')
给 name 这个键的 value 赋值为 Bob
True

get(name)
返回数据库中键为 name 的 string 的 value
name：键名
redis.get('name')
返回 name 这个键的 value
b'Bob'

getset(name, value)
给数据库中键为 name 的 string 赋予值 value 并返回上次的 value
name：键名；value：新值
redis.getset('name', 'Mike')
赋值 name 为 Mike 并得到上次的 value
b'Bob'

mget(keys, *args
返回多个键对应的 value
keys：键的列表
redis.mget(['name', 'nickname'])
返回 name 和 nickname 的 value
[b'Mike', b'Miker']

setnx(name, value)
如果不存在这个键值对，则更新 value，否则不变
name：键名
redis.setnx('newname', 'James')
如果 newname 这个键不存在，则设置值为 James
第一次运行结果是 True，第二次运行结果是 False

setex(name, time, value)
设置可以对应的值为 string 类型的 value，并指定此键值对应的有效期
name: 键名；time: 有效期； value：值
redis.setex('name', 1, 'James')
将 name 这个键的值设为 James，有效期为 1 秒
True

setrange(name, offset, value)
设置指定键的 value 值的子字符串
name：键名；offset：偏移量；value：值
redis.set('name', 'Hello') redis.setrange('name', 6, 'World')
设置 name 为 Hello 字符串，并在 index 为 6 的位置补 World
11，修改后的字符串长度

mset(mapping)
批量赋值
mapping：字典
redis.mset({'name1': 'Durant', 'name2': 'James'})
将 name1 设为 Durant，name2 设为 James
True

msetnx(mapping)
键均不存在时才批量赋值
mapping：字典
redis.msetnx({'name3': 'Smith', 'name4': 'Curry'})
在 name3 和 name4 均不存在的情况下才设置二者值
True

incr(name, amount=1)
键为 name 的 value 增值操作，默认为 1，键不存在则被创建并设为 amount
name：键名；amount：增长的值
redis.incr('age', 1)
age 对应的值增 1，若不存在，则会创建并设置为 1
1，即修改后的值

decr(name, amount=1)
键为 name 的 value 减值操作，默认为 1，键不存在则被创建并将 value 设置为 \-amount
name：键名； amount：减少的值
redis.decr('age', 1)
age 对应的值减 1，若不存在，则会创建并设置为 - 1
-1，即修改后的值

append(key, value)
键为 name 的 string 的值附加 value
key：键名
redis.append('nickname', 'OK')
向键为 nickname 的值后追加 OK
13，即修改后的字符串长度

substr(name, start, end=-1)
返回键为 name 的 string 的子串
name：键名；start：起始索引；end：终止索引，默认为 - 1，表示截取到末尾
redis.substr('name', 1, 4)
返回键为 name 的值的字符串，截取索引为 1~4 的字符
b'ello'

getrange(key, start, end)
获取键的 value 值从 start 到 end 的子字符串
key：键名；start：起始索引；end：终止索引
redis.getrange('name', 1, 4)
返回键为 name 的值的字符串，截取索引为 1~4 的字符
b'ello'
"""
from redis import Redis

redis = Redis(host='localhost', port=6379, db=0, password='foobared')

redis.set()

redis.get()

redis.getset()

redis.mget()

redis.setnx()

redis.setex()

redis.setrange()

redis.mset()

redis.msetnx()

redis.incr()

redis.decr()

redis.append()

redis.substr()

redis.getrange()
