# Redis 键(Keys)

以 Redis DEL 命令为例。如果键被删除，它将给出输出 1，否则它将为 0。
```text
redis 127.0.0.1:6379> SET javatpoint redis   
OK   
redis 127.0.0.1:6379> DEL javatpoint  
(integer) 1 
```


下表列出了 Redis 键相关的命令:

命令	    描述
DEL	        用于删除 key
DUMP	    序列化给定 key ，并返回被序列化的值
EXISTS	    检查给定 key 是否存在
EXPIRE	    为给定 key 设置过期时间
EXPIREAT	用于为 key 设置过期时间，接受的时间参数是 UNIX 时间戳
PEXPIRE	    设置 key 的过期时间，以毫秒计
PEXPIREAT	设置 key 过期时间的时间戳(unix timestamp)，以毫秒计
KEYS	    查找所有符合给定模式的 key
MOVE	    将当前数据库的 key 移动到给定的数据库中
PERSIST	    移除 key 的过期时间，key 将持久保持
PTTL	    以毫秒为单位返回 key 的剩余的过期时间
TTL	        以秒为单位，返回给定 key 的剩余生存时间(
RANDOMKEY	从当前数据库中随机返回一个 key
RENAME	    修改 key 的名称
RENAMENX	仅当 newkey 不存在时，将 key 改名为 newkey
TYPE	    返回 key 所储存的值的类型