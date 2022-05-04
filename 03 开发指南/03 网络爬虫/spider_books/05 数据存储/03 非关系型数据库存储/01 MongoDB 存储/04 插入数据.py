"""

"""
import pymongo

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# 1. 连接mongodb
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# 2. 创建数据库
db = client.test

# 3. 创建数据表
collection = db.students
# collection = db['students']

# 4.1 插入单条数据
result = collection.insert(student1)
print(result)

# 4.2 也可以同时插入多条数据，只需要以列表形式传递即可
result = collection.insert([student1, student2])
print(result)
