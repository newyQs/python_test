import pymongo

"""
先创建测试数据
{'_id': ObjectId('5b23696ac315325f269f28d1'), 'name': 'RUNOOB', 'alexa': '1', 'url': 'https://www.runoob.com'}
{'_id': ObjectId('5b23696ac315325f269f28d1'), 'name': 'Gooogle', 'alexa': '2', 'url': 'https://www.google.com'}
{'_id': ObjectId('5b23696ac315325f269f28d1'), 'name': 'Taobao', 'alexa': '3', 'url': 'https://www.tao.com'}
{'_id': ObjectId('5b23696ac315325f269f28d1'), 'name': 'Tencent', 'alexa': '4', 'url': 'https://www.tencent.com'}
{'_id': ObjectId('5b23696ac315325f269f28d1'), 'name': 'Alibaba', 'alexa': '5', 'url': 'https://www.alibaba.com'}
{'_id': ObjectId('5b23696ac315325f269f28d1'), 'name': 'Facebook', 'alexa': '6', 'url': 'https://www.facebook.com'}
{'_id': ObjectId('5b23696ac315325f269f28d1'), 'name': 'Github', 'alexa': '7', 'url': 'https://www.github.com'}
"""

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

# 先创建测试数据
mycol.insert_many(
    [
        {'_id': '5b23696ac', 'name': 'RUNOOB', 'alexa': '1', 'url': 'https://www.runoob.com'},
        {'_id': '5b23696ac', 'name': 'Gooogle', 'alexa': '2', 'url': 'https://www.google.com'},
        {'_id': '5b23696ac', 'name': 'Taobao', 'alexa': '3', 'url': 'https://www.tao.com'},
        {'_id': '5b23696ac', 'name': 'Tencent', 'alexa': '4', 'url': 'https://www.tencent.com'},
        {'_id': '5b23696ac', 'name': 'Alibaba', 'alexa': '5', 'url': 'https://www.alibaba.com'},
        {'_id': '5b23696ac', 'name': 'Facebook', 'alexa': '6', 'url': 'https://www.facebook.com'},
        {'_id': '5b23696ac', 'name': 'Github', 'alexa': '7', 'url': 'https://www.github.com'}
    ]
)

# 1. 查询一条数据
# 我们可以使用 find_one() 方法来查询集合中的一条数据。
# 查询 sites 文档中的第一条数据：
x = mycol.find_one()
print(x)

# 2. 查询集合中所有数据
# find() 方法可以查询集合中的所有数据，类似 SQL 中的 SELECT * 操作。
# 以下实例查找 sites 集合中的所有数据：
for x in mycol.find():
    print(x)

# 3. 查询指定字段的数据
# 我们可以使用 find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。
for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)

# 除了 _id，你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
# 以下实例除了 alexa 字段外，其他都返回：
for x in mycol.find({}, {"alexa": 0}):
    print(x)

# 以下代码同时指定了 0 和 1 则会报错：
# for x in mycol.find({},{ "name": 1, "alexa": 0 }):
#   print(x)

# 4. 根据指定条件查询
# 我们可以在 find() 中设置参数来过滤数据。
# 以下实例查找 name 字段为 "RUNOOB" 的数据：
myquery = {"name": "RUNOOB"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# 5. 高级查询
# 查询的条件语句中，我们还可以使用修饰符。
# 以下实例用于读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"} :
myquery = {"name": {"$gt": "H"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# 6. 使用正则表达式查询
# 我们还可以使用正则表达式作为修饰符。
# 正则表达式修饰符只用于搜索字符串的字段。
# 以下实例用于读取 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 {"$regex": "^R"} :
myquery = {"name": {"$regex": "^R"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# 6. 返回指定条数记录
# 如果我们要对查询结果设置指定条数的记录可以使用 limit() 方法，该方法只接受一个数字参数。
# 以下实例返回 3 条文档记录：
myresult = mycol.find().limit(3)

# 输出结果
for x in myresult:
    print(x)
