"""
enumerate(iterable, start=0)
返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。
enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。

等价于：
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
"""

# start默认是从0开始

for i, v in enumerate("hello"):
    print(i, v)
print()

for i, v in enumerate("hello", start=1):
    print(i, v)

print(enumerate("hello"))  # <enumerate object at 0x000001E095C1FC40>
print(list(enumerate("hello")))  # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
