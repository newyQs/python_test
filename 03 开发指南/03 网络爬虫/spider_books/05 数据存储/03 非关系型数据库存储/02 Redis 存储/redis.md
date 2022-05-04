# Redis 数据类型

五种类型与类比java的模型
+ string --> String
+ hash --> Hashmap
+ list --> LinkList
+ set --> HashSet
+ sorted_set --> TreeSet

redis 数据存储格式
+ redis自身是一个Map类型的存储方式，其中所有的数据都是采用key:value的形式存储
+ 我们讨论的数据类型指的是存储的数据的类型，也就是value部分的类型，key部分永远都是字符串

