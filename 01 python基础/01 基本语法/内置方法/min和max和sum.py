"""
（1）sum(iterable, /, start=0)
从 start 开始自左向右对 iterable 的项求和并返回总计值。 iterable 的项通常为数字，而 start 值则不允许为字符串。
对某些用例来说，存在 sum() 的更好替代。 拼接字符串序列的更好更快方式是调用 ''.join(sequence)。

（2）min(iterable, *[, default=obj, key=func]) -> value
min(arg1, arg2, *args, *[, key=func]) -> value
返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的。
如果只提供了一个位置参数，它必须是 iterable，返回可迭代对象中最小的元素；如果提供了两个及以上的位置参数，则返回最小的位置参数。
有两个可选只能用关键字的实参。key 实参指定排序函数用的参数，如传给 list.sort() 的。default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。
如果有多个最小元素，则此函数将返回第一个找到的。这和其他稳定排序工具如 sorted(iterable, key=keyfunc)[0] 和 heapq.nsmallest(1, iterable, key=keyfunc) 保持一致。

（3）max(iterable, *[, default=obj, key=func]) -> value
max(arg1, arg2, *args, *[, key=func]) -> value
返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的。
如果只提供了一个位置参数，它必须是非空 iterable，返回可迭代对象中最大的元素；如果提供了两个及以上的位置参数，则返回最大的位置参数。
有两个可选只能用关键字的实参。key 实参指定排序函数用的参数，如传给 list.sort() 的。default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。
如果有多个最大元素，则此函数将返回第一个找到的。这和其他稳定排序工具如 sorted(iterable, key=keyfunc, reverse=True)[0] 和 heapq.nlargest(1, iterable, key=keyfunc) 保持一致。
"""
min()
max()
sum()
