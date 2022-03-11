import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

# sort() 方法可以指定升序或降序排序。
# sort() 方法第一个参数为要排序的字段，第二个字段指定排序规则，1 为升序，-1 为降序，默认为升序。

# 升序
mydoc = mycol.find().sort("alexa")
# 降序
# mydoc = mycol.find().sort("alexa", -1)
for x in mydoc:
    print(x)
