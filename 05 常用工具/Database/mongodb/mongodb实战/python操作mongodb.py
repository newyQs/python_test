"""
https://www.runoob.com/python3/python-mongodb.html
"""
import pymongo

# 连接mongodb
# client = pymongo.MongoClient(host="localhost", port=27017)
# 或者
client = pymongo.MongoClient("mongodb://localhost:27017")

db = client.test
# print(db.name)
# # print(db.my_collection)

# print(db.my_collection.insert_one({"x": 10}).inserted_id)
# print(db.my_collection.insert_one({"x": 8}).inserted_id)
# print(db.my_collection.insert_one({"x": 11}).inserted_id)

# print(db.my_collection.find_one())

print(db.my_collection.find())
for item in db.my_collection.find():
    print(item["x"])

print(db.my_collection.create_index("x"))
for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
    print(item["x"])

print([item["x"] for item in db.my_collection.find().limit(2).skip(1)])
