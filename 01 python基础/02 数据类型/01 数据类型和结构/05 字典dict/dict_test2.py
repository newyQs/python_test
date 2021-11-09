dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.update({"sex": "male"})
print(ret)  # D.update(E=None, **F) -> None.

# 如果更新的键不存在。则添加
print(dic)  # {'name': 'lee', 'age': 18, 'city': 'sz', 'sex': 'male'}

# 如果更新的键存在。则修改
dic.update({"sex": "female"})
print(dic)

# args ==> dict  or iterable???

