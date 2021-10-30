from collections import ChainMap

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}

c = ChainMap(a, b)

# 现在假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）。
# 一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类
# print(c['x'])
# print(c['y'])

print(c)
print(len(c))
print(list(c.keys()))
print(list(c.values()))
print(list(c.items()))
