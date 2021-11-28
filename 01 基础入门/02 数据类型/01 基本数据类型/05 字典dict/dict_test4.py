dic = {"name": "lee", "age": 18, "city": "sz"}

d = dic.copy()  # D.copy() -> a shallow copy of D "
print(d)

d["name"] = "jack"
print(d)
print(dic)

###############################################
dic = {"data": [1, 2, 3]}

d = dic.copy()
print(d)

d["data"] = [1, 2]
print(d)
print(dic)

###############################################
dic = {"name": "lee", "age": 18, "city": "sz"}

print(dic.get("name"))
print(dic.get("job"))
print(dic.get("job", {}))

###############################################
dic = {"a": 1, "b": 2}
dc = d.clear()  # D.clear() -> None

print(d)
print(dc)
