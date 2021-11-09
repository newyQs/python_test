dic = {"name": "lee", "age": 18, "city": "sz"}

print(dic.keys())  # dict_keys(['name', 'age', 'city'])
print(dic.values())  # dict_values(['lee', 18, 'sz'])
print(dic.items())  # dict_items([('name', 'lee'), ('age', 18), ('city', 'sz')])

print(type(dic.keys()))  # <class 'dict_keys'>
print(type(dic.values()))  # <class 'dict_values'>
print(type(dic.items()))  # <class 'dict_items'>

for item in dic:
    print(item)
