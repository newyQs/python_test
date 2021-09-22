from collections.abc import Iterator, Iterable, Generator

# range()
print(range(10))
print(type(range(10)))  # <class 'range'>

# enumerate()
print(enumerate('hello'))
for index, value in enumerate('hello'):
    print(index, value)
