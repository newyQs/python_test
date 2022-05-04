"""
delattr(object, name)
setattr() 相关的函数。实参是一个对象和一个字符串。该字符串必须是对象的某个属性。
如果对象允许，该函数将删除指定的属性。例如 delattr(x, 'foobar') 等价于 del x.foobar 。

getattr(object, name[, default])
返回对象命名属性的值。name 必须是字符串。如果该字符串是对象的属性之一，则返回该属性的值。
例如， getattr(x, 'foobar') 等同于 x.foobar。如果指定的属性不存在，且提供了 default 值，则返回它，否则触发 AttributeError。

hasattr(object, name)
该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。
（此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）

setattr(object, name, value)
本函数与 getattr() 相对应。其参数为一个对象、一个字符串和一个任意值。
字符串可以为某现有属性的名称，或为新属性。只要对象允许，函数会将值赋给属性。如 setattr(x, 'foobar', 123) 等价于 x.foobar = 123。
"""


class A:
    name = "jack"

    @property
    def age(self):
        return 18


a = A()
print(getattr(a, "name"))
print(getattr(a, "age"))

print(hasattr(a, "name"))
print(hasattr(a, "age"))

setattr(a, "sex", "male")
print(getattr(a, "sex"))

delattr(a, "sex")
# print(getattr(a, "sex")) AttributeError: 'A' object has no attribute 'sex'
