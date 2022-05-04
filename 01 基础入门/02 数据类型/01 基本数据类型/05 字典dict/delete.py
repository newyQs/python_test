"""
字典删除键值对：

pop(key)：
删除指定的键值对

popitem()：
删除最后一个键值对
"""
dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.pop("name")

print(ret)  # D.pop(k[,d]) -> v 返回被删除键的值
print(dic)

print(dic.pop("sex", None))  # pop(key) 中 key不存在将会报错，除非给个默认值，如None

################################################
dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.popitem()

print(ret)  # 返回被删除的键值对
print(dic)
