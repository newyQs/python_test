"""
字典删除键值对：

pop(key)：
删除指定的键值对

popitem()：
删除最后一个键值对
"""
dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.pop("name")

print(ret)  # D.pop(k[,d]) -> v
print(dic)

################################################
dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.popitem()

print(ret)
print(dic)
