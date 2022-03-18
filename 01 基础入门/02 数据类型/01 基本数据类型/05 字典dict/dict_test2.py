dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dic.setdefault((1, 2))

print(dic)
print(ret)

###################################################
dic = {"name": "lee", "age": 18, "city": "sz"}

ret = dict.fromkeys((1, 2, 3))

print(dic)
print(ret)
