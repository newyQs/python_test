"""

"""
from pymongo import MongoClient

# 1 连接mongodb
client = MongoClient()

# 2 创建数据库
db = client['weibo']

# 3 创建数据表
collection = db['weibo']


def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')
