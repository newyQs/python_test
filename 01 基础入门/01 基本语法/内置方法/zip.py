"""
zip(*iterables, strict=False)
在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组。

考虑几个问题：
元素个数不一致？
zip(*iterables) --> A zip object yielding tuples until an input is exhausted.

list(zip('abcdefg', range(3), range(4)))
       [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

"""
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)

for item in zip([1, 2, 3]):
    print(item)

print(zip([1, 2, 3], ['sugar', 'spice', 'everything nice']))
