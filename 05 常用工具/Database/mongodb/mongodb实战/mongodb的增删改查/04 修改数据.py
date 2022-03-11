import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

# 我们可以在 MongoDB 中使用 update_one() 方法修改文档中的记录。该方法第一个参数为查询的条件，第二个参数为要修改的字段。
# 如果查找到的匹配数据多于一条，则只会修改第一条。
myquery = {"alexa": "3"}
newvalues = {"$set": {"alexa": "12"}}
mycol.update_one(myquery, newvalues)

# 输出修改后的  "sites"  集合
for x in mycol.find():
    print(x)

# update_one() 方法只能修匹配到的第一条记录，如果要修改所有匹配到的记录，可以使用 update_many()。
# 以下实例将查找所有以 F 开头的 name 字段，并将匹配到所有记录的 alexa 字段修改为 123：
myquery = {"name": {"$regex": "^F"}}
newvalues = {"$set": {"alexa": "123"}}
x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "文档已修改")
