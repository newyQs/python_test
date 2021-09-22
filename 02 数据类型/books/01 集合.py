# 了解什么时候使用哪种数据结构，会对内存，易用性和代码性能方面有比较大的差异
# 集合的主要优势就是速度快？

'''
1.集合内部的元素不重复
2.不支持索引访问集合内部的元素
3.集合使用散列表之后，可以在o（1）时间访问元素
4.集合不支持切片，可以查询
5.集合可以在插入元素时，对其排序
'''
data = {'first', 'second', 'third', 'fourth', 'fifth'}
print(data)
print(sorted(data))
print(data)

# 集合是使用散列表实现的，因此每当一个新项添加到集合中时，该项在内存中的位置由散列的对象确定。
# 这就是为什么散列在访问数据时性能更好，速度非常快，而不是使用列表。
users = {'1267': {'first': 'Larry', 'last': 'Page'}, '2343': {'first': 'John', 'last': 'Freedom'}}
ids = set(users.keys())
full_names = []
for user in users.values():
    full_names.append(user['first'] + ' ' + user['last'])

print(ids)
print(full_names)
