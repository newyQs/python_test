dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.pop("name")

print(ret)  # D.pop(k[,d]) -> v
print(dic)

################################################
dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.popitem()

print(ret)
print(dic)
