"""
isinstance(object, classinfo)
如果 object 参数是 classinfo 参数的实例，或其（直接、间接或 virtual ）子类的实例，则返回 True。
如果 object 不是给定类型的对象，则总是返回 False。如果 classinfo 是类型对象的元组（或由该类元组递归生成）或多个类型的 union 类型，
那么当 object 是其中任一类型的实例时就会返回 True。如果 classinfo 不是某个类型或类型元组，将会触发 TypeError 异常。

class type(object)
class type(name, bases, dict, **kwds)
传入一个参数时，返回 object 的类型。 返回值是一个 type 对象，通常与 object.__class__ 所返回的对象相同。
推荐使用 isinstance() 内置函数来检测对象的类型，因为它会考虑子类的情况。

传入三个参数时，返回一个新的 type 对象。
这在本质上是 class 语句的一种动态形式，name 字符串即类名并会成为 __name__ 属性；
bases 元组包含基类并会成为 __bases__ 属性；如果为空则会添加所有类的终极基类 object。
dict 字典包含类主体的属性和方法定义；它在成为 __dict__ 属性之前可能会被拷贝或包装。

"""
print(isinstance())

print(type())
