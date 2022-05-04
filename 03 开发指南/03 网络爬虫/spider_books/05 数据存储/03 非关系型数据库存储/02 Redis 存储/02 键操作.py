"""
exists(name)
判断一个键是否存在
name：键名
redis.exists('name')
是否存在 name 这个键
True

delete(name)
删除一个键
name：键名
redis.delete('name')
删除 name 这个键
1

type(name)
判断键类型
name：键名
redis.type('name')
判断 name 这个键类型
b'string'

keys(pattern)
获取所有符合规则的键
pattern：匹配规则
redis.keys('n*')
获取所有以 n 开头的键
[b'name']

randomkey()
获取随机的一个键
b'name'

rename(src, dst)
重命名键
src：原键名；dst：新键名
redis.rename('name', 'nickname')
将 name 重命名为 nickname
True

dbsize()
获取当前数据库中键的数目
dbsize()
获取当前数据库中键的数目
100

expire(name, time)
设定键的过期时间，单位为秒
name：键名；time：秒数
redis.expire('name', 2)
将 name 键的过期时间设置为 2 秒
True

ttl(name)
获取键的过期时间，单位为秒，-1 表示永久不过期
name：键名
redis.ttl('name')
获取 name 这个键的过期时间
-1

move(name, db)
将键移动到其他数据库
name：键名；db：数据库代号
move('name', 2)
将 name 移动到 2 号数据库
True

flushdb()
删除当前选择数据库中的所有键
True

flushall()
删除所有数据库中的所有键
True
"""
from redis import Redis

redis = Redis(host='localhost', port=6379, db=0, password='foobared')

redis.exists()

redis.delete()

redis.type()

redis.keys()

redis.randomkey()

redis.rename()

redis.dbsize()

redis.expire()

redis.ttl()

redis.move()

redis.flushdb()

redis.flushall()
