from collections.abc import Iterable, Iterator, Generator

# 求平方
numbers = [12, 3, 35, 24, 5, 17, 13]

# map(func, *iterables) --> map object
m = map(lambda x: x ** 2, numbers)
print(m)
print(list(m))

print(type(m))
print(isinstance(m, Iterable))
print(isinstance(m, Iterator))
print(isinstance(m, Generator))


# 使用推导式
print([num ** 2 for num in numbers])
