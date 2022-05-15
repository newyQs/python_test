"""
https://www.jb51.net/article/214860.htm
"""


# 方式1，元类实现：
class MetaClass(type):
    def __call__(self, *args, **kwargs):
        """
        self : class Singleton
        """
        if not hasattr(self, "ins"):
            insObject = super(__class__, self).__call__(*args, **kwargs)
            setattr(self, "ins", insObject)
        return getattr(self, "ins")


class Singleton(object, metaclass=MetaClass):
    pass


if __name__ == "__main__":
    ins = Singleton()
    print(id(ins))
    ins = Singleton()
    print(id(ins))


# 方式2，继承实现：
class ParentClass:
    def __new__(cls, *args, **kwargs) -> object:
        """
        cls : class Singeton
        """
        if not hasattr(cls, "ins"):
            insObject = super(__class__, cls).__new__(cls, *args, **kwargs)
            setattr(cls, "ins", insObject)
        return getattr(cls, "ins")


class Singleton(ParentClass):
    pass


if __name__ == "__main__":
    ins = Singleton()
    print(id(ins))
    ins = Singleton()
    print(id(ins))


# 方式3，装饰器实现：
def warpper(clsObject):
    def inner(*args, **kwargs):
        if not hasattr(clsObject, "ins"):
            insObject = clsObject(*args, **kwargs)
            setattr(clsObject, "ins", insObject)
        return getattr(clsObject, "ins")

    return inner


@warpper
class Singleton:
    pass


if __name__ == "__main__":
    ins = Singleton()
    print(id(ins))
    ins = Singleton()
    print(id(ins))


# 方式4，@classmethod实现单例模式：
class Singleton:

    @classmethod
    def getSingletonInstanceObject(cls, *args, **kwargs):
        if not hasattr(cls, "ins"):
            insObject = cls(*args, **kwargs)
            setattr(cls, "ins", insObject)
        return getattr(cls, "ins")


if __name__ == "__main__":
    ins = Singleton.getSingletonInstanceObject()
    print(id(ins))
    ins = Singleton.getSingletonInstanceObject()
    print(id(ins))
