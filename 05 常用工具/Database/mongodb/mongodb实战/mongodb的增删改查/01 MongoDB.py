import pymongo

# 1.创建数据库
# 创建数据库需要使用 MongoClient 对象，并且指定连接的 URL 地址和要创建的数据库名。
# 如下实例中，我们创建的数据库 runoobdb :
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
# 注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。

# 2. 判断数据库是否已存在
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "runoobdb" in dblist:
    print("数据库已存在！")
# 注意：database_names 在最新版本的 Python 中已废弃，Python3.7+ 之后的版本改为了 list_database_names()。

# 3. 创建一个集合
# MongoDB 使用数据库对象来创建集合，实例如下：
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]

mycol = mydb["sites"]
# 注意: 在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。

# 4. 判断集合是否已存在
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['runoobdb']

collist = mydb.list_collection_names()
# collist = mydb.collection_names()
if "sites" in collist:  # 判断 sites 集合是否存在
    print("集合已存在！")
# 注意：collection_names 在最新版本的 Python 中已废弃，Python3.7+ 之后的版本改为了 list_collection_names()。
