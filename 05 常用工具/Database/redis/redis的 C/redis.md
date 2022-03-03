http://c.biancheng.net/redis/
# 1 Redis是什么
Redis 全称 Remote Dictionary Server（即远程字典服务），它是一个基于内存实现的键值型非关系（NoSQL）数据库，由意大利人 Salvatore Sanfilippo 使用 C 语言编写。

与其他内存型数据库相比，Redis 具有以下特点：
+ Redis 不仅可以将数据完全保存在内存中，还可以通过磁盘实现数据的持久存储；
+ Redis 支持丰富的数据类型，包括 string、list、set、zset、hash 等多种数据类型，因此它也被称为“数据结构服务器”；
+ Redis 支持主从同步，即 master-slave 主从复制模式。数据可以从主服务器向任意数量的从服务器上同步，有效地保证数据的安全性；
+ Redis 支持多种编程语言，包括 C、C++、Python、Java、PHP、Ruby、Lua 等语言。

与 SQL 型数据库截然不同，Redis 没有提供新建数据库的操作，因为它自带了 16 （0—15）个数据库（默认使用 0 库）。
在同一个库中，key 是唯一存在的、不允许重复的，它就像一把“密钥”，只能打开一把“锁”。
键值存储的本质就是使用 key 来标识 value，当想要检索 value 时，必须使用与 value 相对应的 key 进行查找。

Redis 数据库没有“表”的概念，它通过不同的数据类型来实现存储数据的需求，不同的数据类型能够适应不同的应用场景，从而满足开发者的需求。

## 1.2 Redis架构
Redis体系架构主要分为两个部分：
+ Redis服务端
+ Redis客户端

客户端和服务端可以位于同一台计算机上，也可以位于不同的计算机上。服务端是整个架构的“大脑”，能够把数据存储到内存中，并且起到管理数据的作用。

## 1.3 Redis优势
下面对 Redis 的优势进行了简单总结：
+ 性能极高：Redis 基于内存实现数据存储，它的读取速度是 110000次/s，写速度是 81000次/s；
+ 多用途工具： Redis 有很多的用途，比如可以用作缓存、消息队列、搭建 Redis 集群等；
+ 命令提示功能：Redis 客户端拥有强大的命令提示功能，使用起来非常的方便，降低了学习门槛；
+ 可移植性：Redis 使用用标准 C语言编写的，能够在大多数操作系统上运行，比如 Linux，Mac，Solaris 等。

## 1.4 Redis应用场景
Redis 用来缓存一些经常被访问的热点数据、或者需要耗费大量资源的内容，通过把这些内容放到 Redis 中，可以让应用程序快速地读取它们。
例如，网站的首页需要经常被访问，并且在创建首页的过程中会消耗的较多的资源，此时就可以使用 Redis 将整个首页缓存起来，从而降低网站的压力，减少页面访问的延迟时间。

我们知道，数据库的存储方式大体可分为两大类，基于磁盘存储和基于内存存储。
磁盘存储的数据库，因为磁头机械运动以及系统调用等因素导致读写效率较低。
Redis 基于内存来实现数据存取，相对于磁盘来说，其读写速度要高出好几个数量级。

Redis 基于内存来实现数据的存储，因此其速度非常快。但是我们知道，计算机的内存是非常珍贵的资源，
所以 Redis 不适合存储较大的文件或者二进制数据，否则会出现错误，Redis 适合存储较小的文本信息。理论上 Redis 的每个 key、value 的大小不超过 512 MB。

# 2 Redis安装


# 3 Redis配置文件
在 Redis 的安装目录中有一个名为 redis.windows.conf 的配置文件，若在 Linux 中则为 redis.conf，本节以 Windows 系统为例对该文件进行讲解。

## 3.1 查看配置项
您可以使用 Redis 的CONFIG命令来查看或者更改 Redis 的配置信息。语法格式如下：

redis 127.0.0.1:6379> CONFIG GET 配置名称

示例如下，获取日志等级的配置项：

redis 127.0.0.1:6379> CONFIG GET loglevel 

输出结果如下：

1) "loglevel"
2) "notice"

通过使用*可以查看所有配置项，命令如下：

redis 127.0.0.1:6379> CONFIG GET *

输出结果：

1) "dbfilename"
2) "dump.rdb"
3) "requirepass"
4) ""
5) "masterauth"
6) ""
7) "cluster-announce-ip"
8) ""
9) "unixsocket"
10) ""
11) "logfile"
12) ""
13) "pidfile"
14) ""
15) "slave-announce-ip"
16) ""
17) "replica-announce-ip"
18) ""
19) "maxmemory"
20) "0"
21) "proto-max-bulk-len"
22) "536870912"
23) "client-query-buffer-limit"
24) "1073741824"
25) "maxmemory-samples"
26) "5"
27) "lfu-log-factor"
28) "10"
29) "lfu-decay-time"
30) "1"
31) "timeout"
32) "0"
33) "active-defrag-threshold-lower"
34) "10"
35) "active-defrag-threshold-upper"
36) "100"
37) "active-defrag-ignore-bytes"
38) "104857600"
.....

## 3.2 更改配置项
如果想要重新设置配置项，需要使用以下命令：

redis 127.0.0.1:6379> CONFIG SET 配置项名称 配置项参数值

示例如下：

127.0.0.1:6379> CONFIG SET loglevel "verbose"

OK

127.0.0.1:6379> CONFIG GET loglevel

1) "loglevel"
2) "verbose"

Redis 的日志级别有以下四种：
1. debug：会打印出很多信息，适用于开发和测试阶段。
2. verbose（冗长的）：包含很多不太有用的信息，但比debug简化一些。
3. notice：适用于生产模式。
4. warning : 警告信息。

Redis 默认设置为 verbose，开发测试阶段可以用 debug，生产模式一般选用 notice。

## 3.3 更改配置文件
Redis 某些配置信息无法直接通过命令修改，此时就需要修改配置文件，比如设置 Redis 允许远程连接的功能。配置文件修改如下：
```
1.注释掉本地IP地址,绑定要访问的外部IP
#bind 127.0.0.1 ::1
bind 192.168.1.1
2.关闭保护模式(把yes改为no)
protected-mode no
3.重启服务器,windows重启
redis-server --service-stop
redis-server --service-start
Linux重启
sudo /etc/init.d/redis-server restart
```

## 3.4 配置项说明

# 4 Redis数据类型
## 4.1 string字符串

## 4.2 hash散列

## 4.3 list列表

## 4.4 set集合

## 4.5 zset有序集合

# 5 Redis命令行模式
