"""

"""
import pymongo

# 1. 连接mongodb
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# 2. 创建数据库
db = client.test

# 3. 创建数据表
collection = db.students
# collection = db['students']
