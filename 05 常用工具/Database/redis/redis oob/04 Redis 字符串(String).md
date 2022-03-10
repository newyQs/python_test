# Redis 字符串(String)
Redis 字符串数据类型的相关命令用于管理 redis 字符串值，基本语法如下：
```
redis 127.0.0.1:6379> COMMAND KEY_NAME
```

示例：
```
redis 127.0.0.1:6379> SET runoobkey redis
OK
redis 127.0.0.1:6379> GET runoobkey
"redis"
```
在以上实例中我们使用了 SET 和 GET 命令，键为 runoobkey。

## redis字符串命令
```
set key value 

get key

getrange key start end

getbit key offset

mget key1(key2...)

setbit key offset value

setex key seconds value
```