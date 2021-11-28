"""

"""


class Vector:
    def __init__(self, a, b):  # __init__()要求无返回值
        self.a = a
        self.b = b

    def __repr__(self):
        return 'Vector (%d, %d)' % (self.b, self.a)

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
print(v1)  # 优先使用 __str__() 的返回值
