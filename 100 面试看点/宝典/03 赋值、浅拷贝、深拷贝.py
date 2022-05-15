"""

"""
# 1.赋值：相互影响
a = ['abc', 1, True, ['jkl', 'djj'], {'name': 'lee', 'age': 18}]
b = a

print(a)
print(b)

a[0] = '==>jkl'

print(a)
print(b)

# 2.浅拷贝
"""
浅拷贝会创建新对象，其内容非原对象本身的引用，而是原对象内第一层对象的引用。
浅拷贝有三种形式:切片操作、工厂函数、copy 模块中的 copy 函数。


"""

# 3.深拷贝

"""
深拷贝只有一种形式，copy 模块中的 deepcopy()函数。
"""
