"""
update()
    更新或创建
"""
dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.update({"sex": "male"})
print(ret)  # D.update(E=None, **F) -> None.

# update 如果键不存在，则添加
print(dic)  # {'name': 'lee', 'age': 18, 'city': 'sz', 'sex': 'male'}

# update 如果键存在，则修改
dic.update({"sex": "female"})
print(dic)

# args ==> dict  or iterable???
