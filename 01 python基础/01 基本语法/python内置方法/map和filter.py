"""
（1）filter(function or None, iterable) --> filter object

用 iterable 中函数 function 返回真的那些元素，构建一个新的迭代器。
iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。
如果 function 是 None ，则会假设它是一个身份函数，即 iterable 中所有返回假的元素会被移除。

请注意， filter(function, iterable) 相当于一个生成器表达式，当 function 不是 None 的时候为 (item for item in iterable if function(item))；
function 是 None 的时候为 (item for item in iterable if item)

（2）map(function, iterable, ...) --> map object

返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器。
如果传入了额外的 iterable 参数，function 必须接受相同个数的实参并被应用于从所有可迭代对象中并行获取的项。
当有多个可迭代对象时，最短的可迭代对象耗尽则整个迭代就将结束。

（3）reduce(function, sequence[, initial]) -> value
"""
from functools import reduce

ret = list(map(lambda x: x ** 2, range(1, 10)))
print(ret)

ret = list(filter(lambda x: x > 0, [1, 3, -2, 15, 29, -18]))
print(ret)

ret = reduce(lambda x, y: x * y, range(1, 5))
print(ret)
