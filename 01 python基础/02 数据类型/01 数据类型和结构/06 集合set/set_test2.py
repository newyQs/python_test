s2 = {'1', '2', '3'}
s3 = {'1', '2', '5'}

# 交集
a = s2.intersection(s3)  # 取交集, s2.intersection(s3) 与 s3.intersection(s2) 一样
print(a)  # {'2', '1'}
b = s2.intersection(s3)
print(b)  # {'2', '1'}
print(s2 & s3)  # 取交集 {'2', '1'}

# 并集
print(s2.union(s3))  # 取并集 {'2', '5', '3', '1'}
print(s2 | s3)  # 取并集 {'2', '5', '3', '1'}

# 差集
print(s2.difference(s3))  # 取s2中存在，s3 不存在的，#取差集 {'3'}
print(s2 - s3)  # 取差集 {'3'}
print(s3 - s2)  # {'5'}

# 对称差集，取s2, s3 中不同时存在的元素
print(s2 ^ s3)  # {'3', '5'}print(s2.symmetric_difference(s3))#对称差集，就是把两个集合中相同的去掉
