# Redis HyperLogLog

Redis HyperLogLog 是用来做基数统计的算法，HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定 的、并且是很小的。

在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 264 个不同元素的基 数。这和计算基数时，元素越多耗费内存就越多的集合形成鲜明对比。

但是，因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。

```text
redis 127.0.0.1:6379> PFADD rediscomcn "redis"
1) (integer) 1
redis 127.0.0.1:6379> PFADD rediscomcn "mongodb"
1) (integer) 1
redis 127.0.0.1:6379> PFADD rediscomcn "mysql"
1) (integer) 1
redis 127.0.0.1:6379> PFCOUNT rediscomcn
(integer) 3
```

## 命令大全

命令	描述
PFADD	添加指定元素到 HyperLogLog 中。
PFCOUNT	返回给定 HyperLogLog 的基数估算值。
PFMERGE	将多个 HyperLogLog 合并为一个 HyperLogLog

