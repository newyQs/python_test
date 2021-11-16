"""
dir([object])
如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。
"""

print(dir())


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']


s = Shape()
print(dir(s))
