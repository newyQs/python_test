# Redis 字符串 ( Strings )

语法：
```text
redis 127.0.0.1:6379> COMMAND KEY_NAME
```

```text
redis 127.0.0.1:6379> SET javatpoint redis   
OK   
redis 127.0.0.1:6379> GET javatpoint   
"redis"  
```

## 命令大全

命令	    描述
SET	        设置指定 key 的值
GET	        获取指定 key 的值
GETRANGE	返回 key 中字符串值的子字符
GETSET	    将给定 key 的值设为 value ，并返回 key 的旧值 ( old value )
GETBIT	    对 key 所储存的字符串值，获取指定偏移量上的位 ( bit )
MGET	    获取所有(一个或多个)给定 key 的值
SETBIT	    对 key 所储存的字符串值，设置或清除指定偏移量上的位(bit)
SETEX	    设置 key 的值为 value 同时将过期时间设为 seconds
SETNX	    只有在 key 不存在时设置 key 的值
SETRANGE	从偏移量 offset 开始用 value 覆写给定 key 所储存的字符串值
STRLEN	    返回 key 所储存的字符串值的长度
MSET	    同时设置一个或多个 key-value 对
MSETNX	    同时设置一个或多个 key-value 对
PSETEX	    以毫秒为单位设置 key 的生存时间
INCR	    将 key 中储存的数字值增一
INCRBY	    将 key 所储存的值加上给定的增量值 ( increment )
INCRBYFLOAT	将 key 所储存的值加上给定的浮点增量值 ( increment )
DECR	    将 key 中储存的数字值减一
DECRBY	    将 key 所储存的值减去给定的减量值 ( decrement )
APPEND	    将 value 追加到 key 原来的值的末尾