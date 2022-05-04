"""https://cuiqingcai.com/5587.html


redis://[:password]@host:port/db
rediss://[:password]@host:port/db
unix://[:password]@/path/to/socket.sock?db=db

"""
from redis import StrictRedis, Redis, ConnectionPool

# 连接redis：

# 1. 使用Redis
# redis = Redis(host='localhost', port=6379, db=0, password='foobared')

# 2. 使用StrictRedis
# redis = StrictRedis(host='localhost', port=6379, db=0, password='foobared')

# 3. 使用ConnectionPool
pool = ConnectionPool(host='localhost', port=6379, db=0, password='foobared')
redis = StrictRedis(connection_pool=pool)

# 4. 或者构造url连接
# url = 'redis://:foobared@localhost:6379/0'
# pool = ConnectionPool.from_url(url)
# redis = StrictRedis(connection_pool=pool)

# 5.
# redis = Redis.from_url(url=url)


redis.set('name', 'Bob')
print(redis.get('name'))
