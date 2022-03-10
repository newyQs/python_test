# Redis 键(key)
redis key的基本用法：
```
redis 127.0.0.1:6379> COMMAND KEY_NAME
```

示例：
```
redis 127.0.0.1:6379> SET runoobkey redis
OK
redis 127.0.0.1:6379> DEL runoobkey
(integer) 1
```
在以上实例中 DEL 是一个命令， runoobkey 是一个键。 如果键被删除成功，命令执行后输出 (integer) 1，否则将输出 (integer) 0

## Redis keys 命令
```
del key
dump key
exists key

```