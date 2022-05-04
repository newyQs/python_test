"""
zadd(name, *args, **kwargs)
向键为 name 的 zset 中添加元素 member，score 用于排序。如果该元素存在，则更新其顺序
name： 键名；args：可变参数
redis.zadd('grade', 100, 'Bob', 98, 'Mike')
向键为 grade 的 zset 中添加 Bob（其 score 为 100），并添加 Mike（其 score 为 98）
2，即添加的元素个数

zrem(name, *values)
删除键为 name 的 zset 中的元素
name：键名；values：元素
redis.zrem('grade', 'Mike')
从键为 grade 的 zset 中删除 Mike
1，即删除的元素个数

zincrby(name, value, amount=1)
如果在键为 name 的 zset 中已经存在元素 value，则将该元素的 score 增加 amount；否则向该集合中添加该元素，其 score 的值为 amount
name：key 名；value：元素；amount：增长的 score 值
redis.zincrby('grade', 'Bob', -2)
键为 grade 的 zset 中 Bob 的 score 减 2
98.0，即修改后的值

zrank(name, value)
返回键为 name 的 zset 中元素的排名，按 score 从小到大排序，即名次
name：键名；value：元素值
redis.zrank('grade', 'Amy')
得到键为 grade 的 zset 中 Amy 的排名
1

zrevrank(name, value)
返回键为 name 的 zset 中元素的倒数排名（按 score 从大到小排序），即名次
name：键名；value：元素值
redis.zrevrank('grade', 'Amy')
得到键为 grade 的 zset 中 Amy 的倒数排名
2

zrevrange(name, start, end, withscores=False)
返回键为 name 的 zset（按 score 从大到小排序）中 index 从 start 到 end 的所有元素
name：键值；start：开始索引；end：结束索引；withscores：是否带 score
redis.zrevrange('grade', 0, 3)
返回键为 grade 的 zset 中前四名元素
[b'Bob', b'Mike', b'Amy', b'James']

zrangebyscore(name, min, max, start=None, num=None, withscores=False)
返回键为 name 的 zset 中 score 在给定区间的元素
name：键名；min：最低 score；max：最高 score； start：起始索引；num：个数；withscores：是否带 score
redis.zrangebyscore('grade', 80, 95)
返回键为 grade 的 zset 中 score 在 80 和 95 之间的元素
[b'Bob', b'Mike', b'Amy', b'James']

zcount(name, min, max)
返回键为 name 的 zset 中 score 在给定区间的数量
name：键名；min：最低 score；max：最高 score
redis.zcount('grade', 80, 95)
返回键为 grade 的 zset 中 score 在 80 到 95 的元素个数
2

zcard(name)
返回键为 name 的 zset 的元素个数
name：键名
redis.zcard('grade')
获取键为 grade 的 zset 中元素的个数
3

zremrangebyrank(name, min, max)
删除键为 name 的 zset 中排名在给定区间的元素
name：键名；min：最低位次；max：最高位次
redis.zremrangebyrank('grade', 0, 0)
删除键为 grade 的 zset 中排名第一的元素
1，即删除的元素个数

zremrangebyscore(name, min, max)
删除键为 name 的 zset 中 score 在给定区间的元素
name：键名；min：最低 score；max：最高 score
redis.zremrangebyscore('grade', 80, 90)
删除 score 在 80 到 90 之间的元素
1，即删除的元素个数
"""
from redis import Redis

redis = Redis(host='localhost', port=6379, db=0, password='foobared')

redis.zadd()

redis.zrem()

redis.zincrby()

redis.zrank()

redis.zrevrange()

redis.zrangebyscore()

redis.zcount()

redis.zcard()

redis.zremrangebyrank()

redis.zremrangebyscore()



