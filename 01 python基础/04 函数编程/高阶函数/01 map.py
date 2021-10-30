from collections.abc import Iterable, Iterator, Generator

# 求平方
numbers = [12, 3, 35, 24, 5, 17, 13]

# map(func, *iterables) --> map object
# 函数func依次作用于每个iterables成员
m = map(lambda x: x ** 2, numbers)

print(m)
print(list(m))

print(type(m))
print(isinstance(m, Iterable))  # True
print(isinstance(m, Iterator))  # True
print(isinstance(m, Generator))  # False

# 使用推导式
print([num ** 2 for num in numbers])
