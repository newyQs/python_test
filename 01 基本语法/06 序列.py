from collections.abc import Iterable, Iterator, Generator

# range()
r = range(10)
print(r)
print(type(r))  # <class 'range'>
print(isinstance(r, Iterable))  # True
print(isinstance(r, Iterator))  # False
print(isinstance(r, Generator))  # False

print('---------分割线')
# enumerate()
e = enumerate('hello')
print(e)
print(type(e))
print(isinstance(e, Iterable))  # True
print(isinstance(e, Iterator))  # True
print(isinstance(e, Generator))  # False

for index, value in e:
    print(index, value)
