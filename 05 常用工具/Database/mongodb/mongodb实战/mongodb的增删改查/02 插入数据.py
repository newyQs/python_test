import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["runoobdb"]  # 数据库
col = db["sites"]  # 集合

# 1. 插入一条数据
mydict = {
    "name": "RUNOOB",
    "alexa": "10000",
    "url": "https://www.runoob.com"
}

x = col.insert_one(mydict)
print(x)
print(x.inserted_id)
# insert_one() 方法返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值


# 2. 插入多条数据
mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]

xs = col.insert_many(mylist)
print(xs)
print(xs.inserted_ids)
# insert_many() 方法返回 InsertManyResult 对象，该对象包含 inserted_ids 属性，该属性保存着所有插入文档的 id 值


# 3. 插入指定 _id 的多条数据
mylist = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google 搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]

xsi = col.insert_many(mylist)
# 输出插入的所有数据对应的 _id 值
print(xsi)
print(xsi.inserted_ids)
