"""

"""
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert(student1)
print(result)

# 也可以同时插入多条数据，只需要以列表形式传递即可
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result = collection.insert([student1, student2])
print(result)
