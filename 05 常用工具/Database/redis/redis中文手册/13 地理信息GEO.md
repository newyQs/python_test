# Redis 地理信息GEO

Redis GEO 主要用于存储地理位置信息，并对存储的信息进行操作，该功能在 Redis 3.2 版本新增。

Redis GEO 操作方法有：
+ geoadd：添加地理位置的坐标。
+ geopos：获取地理位置的坐标。
+ geodist：计算两个位置之间的距离。
+ georadius：根据用户给定的经纬度坐标来获取指定范围内的地理位置集合。
+ georadiusbymember：根据储存在位置集合里面的某个地点获取指定范围内的地理位置集合。
+ geohash：返回一个或多个位置对象的 geohash 值。

## geoadd
geoadd 用于存储指定的地理空间位置，可以将一个或多个经度(longitude)、纬度(latitude)、位置名称(member)添加到指定的 key 中。

geoadd 语法格式如下：
```text
GEOADD key longitude latitude member [longitude latitude member ...]
```

以下实例中 key 为 Sicily、Catania 为位置名称 ：
```text
redis> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
(integer) 2
redis> GEODIST Sicily Palermo Catania
"166274.1516"
redis> GEORADIUS Sicily 15 37 100 km
1) "Catania"
redis> GEORADIUS Sicily 15 37 200 km
1) "Palermo"
2) "Catania"
redis>
```

geopos
geopos 用于从给定的 key 里返回所有指定名称(member)的位置（经度和纬度），不存在的返回 nil。

## geopos 语法格式如下：
```text
GEOPOS key member [member ...]
```

```text
redis> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
(integer) 2
redis> GEOPOS Sicily Palermo Catania NonExisting
1) 1) "13.36138933897018433"
  2) "38.11555639549629859"
2) 1) "15.08726745843887329"
  2) "37.50266842333162032"
3) (nil)
redis>
```

## geodist
geodist 用于返回两个给定位置之间的距离。

geodist 语法格式如下：
```text
GEODIST key member1 member2 [m|km|ft|mi]
```

member1 member2 为两个地理位置。

最后一个距离单位参数说明：

m ：米，默认单位。

km ：千米。

mi ：英里。

ft ：英尺。

## 计算 Palermo 与 Catania 之间的距离实例

```text
redis> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
(integer) 2
redis> GEODIST Sicily Palermo Catania
"166274.1516"
redis> GEODIST Sicily Palermo Catania km
"166.2742"
redis> GEODIST Sicily Palermo Catania mi
"103.3182"
redis> GEODIST Sicily Foo Bar
(nil)
redis>
```

georadius、georadiusbymember

georadius 以给定的经纬度为中心， 返回键包含的位置元素当中， 与中心的距离不超过给定最大距离的所有位置元素。

georadiusbymember 和 GEORADIUS 命令一样， 都可以找出位于指定范围内的元素， 但是 georadiusbymember 的中心点是由给定的位置元素决定的， 而不是使用经度和纬度来决定中心点。

georadius 与 georadiusbymember 语法格式如下：
```text
GEORADIUS key longitude latitude radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]
GEORADIUSBYMEMBER key member radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]
```

参数说明：
+ m ：米，默认单位。
+ km ：千米。
+ mi ：英里。
+ ft ：英尺。
+ WITHDIST: 在返回位置元素的同时， 将位置元素与中心之间的距离也一并返回。
+ WITHCOORD: 将位置元素的经度和维度也一并返回。
+ WITHHASH: 以 52 位有符号整数的形式， 返回位置元素经过原始 geohash 编码的有序集合分值。 这个选项主要用于底层应用或者调试， 实际中的作用并不大。
+ COUNT 限定返回的记录数。
+ ASC: 查找结果根据距离从近到远排序。
+ DESC: 查找结果根据从远到近排序。

## georadius实例

```text
redis> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
(integer) 2
redis> GEORADIUS Sicily 15 37 200 km WITHDIST
1) 1) "Palermo"
  2) "190.4424"
2) 1) "Catania"
  2) "56.4413"
redis> GEORADIUS Sicily 15 37 200 km WITHCOORD
1) 1) "Palermo"
  2) 1) "13.36138933897018433"
   2) "38.11555639549629859"
2) 1) "Catania"
  2) 1) "15.08726745843887329"
   2) "37.50266842333162032"
redis> GEORADIUS Sicily 15 37 200 km WITHDIST WITHCOORD
1) 1) "Palermo"
  2) "190.4424"
  3) 1) "13.36138933897018433"
   2) "38.11555639549629859"
2) 1) "Catania"
  2) "56.4413"
  3) 1) "15.08726745843887329"
   2) "37.50266842333162032"
redis>
```

## georadiusbymember实例

```text
redis> GEOADD Sicily 13.583333 37.316667 "Agrigento"
(integer) 1
redis> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
(integer) 2
redis> GEORADIUSBYMEMBER Sicily Agrigento 100 km
1) "Agrigento"
2) "Palermo"
redis>
```

geohash
Redis GEO 使用 geohash 来保存地理位置的坐标。

geohash 用于获取一个或多个位置元素的 geohash 值。

geohash 语法格式如下：
```text
GEOHASH key member [member ...]
```

## geohash实例

```text
redis> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
(integer) 2
redis> GEOHASH Sicily Palermo Catania
1) "sqc8b49rny0"
2) "sqdtr74hyu0"
redis>
```