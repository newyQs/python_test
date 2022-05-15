"""

"""
# 01 字典排序:按照值
d = {'a': 23, 'g': 43, 'f': 29, 'e': 10}
print(d.items())
s = sorted(d.items(), key=lambda x: x[1], reverse=False)


# 02 将字符串“k:1|k1:2|k2:3|k3:4”处理成字典：{k:1, k1:2, k2:3, k3:4}
def str2dict(string):
    dic = dict()
    for items in string.split('|'):
        key, value = items.split(':')
        dic[key] = value

    return dic


st = 'k:1|k1:2|k2:3|k3:4'
print(str2dict(st))

# 03 将alist中的元素的age按照从大到小排序？
alist = [{'name': 'jack', 'age': 20}, {'name': 'lucy', 'age': 19}, {'name': 'rouse', 'age': 32}]
ret = sorted(alist, key=lambda x: x['age'], reverse=True)
print(ret)

# 04 字典和json的区别？
'''
字典是一种数据结构，json是一种数据的表现形式，字典的key必须是可hash的，而json的key必须是字符串
'''
