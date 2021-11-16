"""
all(iterable) -- > bool
如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True 。 等价于：
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

any(iterable)
如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False。 等价于:
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
"""
# all(iterable)  -- > bool
print(all([1, 2, 4]))

# any(iterable)  -- > bool
print(any([1, 2, 3]))
