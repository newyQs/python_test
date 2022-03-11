from redis import StrictRedis, ConnectionPool

# StrictRedis(host='localhost', port=6379, db=0, password='foobared')
# 这里我们传入了Redis的地址、运行端口、使用的数据库和密码信息。在默认不传的情况下，这4个参数分别为localhost、6379、0和None。

# redis的构建方式一：
rds1 = StrictRedis(host="localhost", port=6379, db=0)
rds1.set("name", "lqs")
print("rds1:", rds1.get("name"))

# redis的构建方式二：
pool = ConnectionPool(host="localhost", port=6379, db=0)
rds2 = StrictRedis(connection_pool=pool)
rds2.set("name", "jack")
print("rds2:", rds2.get("name"))

# redis的构建方式三：
# url = 'redis://:foobared@localhost:6379/0'
url = "redis://localhost:6379/0"
pool = ConnectionPool.from_url(url)
rds3 = StrictRedis(connection_pool=pool)
rds3.set("name", "lucy")
print("rds3:", rds3.get("name"))


"""
https://blog.csdn.net/liuzuoping/article/details/100119201

1. 键(key) 操作：
exists(name)
delete(name)
type(name)
keys(pattern, kwargs)
randomkey(kwargs)
rename(src, dst)
dbsize(kwargs)
expire(name, time)
ttl(name)
move(name, db)
flushdb(asynchronous, kwargs)
flushall(asynchronous, kwargs)

2. 字符串(string) 操作：
set(name, value)
get(name)
getset(name, value)
mget(keys, kwargs)
setnx(name, value)
setex(name, time, value)

3. 列表(list) 操作：
rpush(name, values)
lpush(name, values)
llen(name)
lrange(name, start, end)
ltrim(name, start, end)
lindex(name, index)
lset(name, index, value)
lrem(name, count, value)
lpop(name, count=None)
rpop(name, count=None)

4. 哈希(hash) 操作：


5. 集合(set) 操作：


6. 有序集合(zset) 操作：

"""
rds2.rpop()