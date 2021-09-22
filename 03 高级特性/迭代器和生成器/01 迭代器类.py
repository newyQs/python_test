class MutiplyByTwo:
    def __init__(self, number):
        self.number = number
        self.count = 0

    def __next__(self):
        self.count += 1
        return self.number * self.count

# mul = MutiplyByTwo(500)
# print(next(mul))
# print(next(mul))
# print(next(mul))

# 2.一个迭代器，但不是可迭代对象
# 并不支持被for循环遍历
# for i in MutiplyByTwo(500):  # TypeError: 'MutiplyByTwo' object is not iterable
#     print(i)

# 3.一个可迭代对象有一个名为__iter__的方法，该方法返回迭代器
# 因此python中字符串，列表，文件和字典都是可迭代对象
