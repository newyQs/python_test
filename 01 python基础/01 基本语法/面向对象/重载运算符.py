"""
反向运算符重载：
__radd__: 加运算
__rsub__: 减运算
__rmul__: 乘运算
__rdiv__: 除运算
__rmod__: 求余运算
__rpow__: 乘方

复合重载运算符：
__iadd__: 加运算
__isub__: 减运算
__imul__: 乘运算
__idiv__: 除运算
__imod__: 求余运算
__ipow__: 乘方
"""


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __repr__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        if other.__class__ is Vector:
            return Vector(self.a + other.a, self.b + other.b)
        elif other.__class__ is int:
            return Vector(self.a + other, self.b)

    def __radd__(self, other):
        """反向算术运算符的重载
        __add__运算符重载可以保证V+int的情况下不会报错，但是反过来int+V就会报错，通过反向运算符重载可以解决此问题
        """

        if other.__class__ is int or other.__class__ is float:
            return Vector(self.a + other, self.b)
        else:
            raise ValueError("值错误")

    def __iadd__(self, other):
        """复合赋值算数运算符的重载
        主要用于列表，例如L1+=L2,默认情况下调用__add__，会生成一个新的列表，
        当数据过大的时候会影响效率，而此函数可以重载+=，使L2直接增加到L1后面
        """

        if other.__class__ is Vector:
            return Vector(self.a + other.a, self.b + other.b)
        elif other.__class__ is int:
            return Vector(self.a + other, self.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
print(v1 + 5)
print(6 + v2)
