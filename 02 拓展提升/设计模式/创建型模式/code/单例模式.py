"""
python实现单例模式
"""
import threading


# 函数装饰器方式
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class A(object):
    def __init__(self, a=0):
        self.a = a


a1 = A(1)
a2 = A(2)
print(id(a1), id(a2))


# 类装饰器方式
class Singleton(object):

    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class B(object):
    def __init__(self):
        pass


b1 = B()
b2 = B()
print(id(b1), id(b2))


#
class Singleton(object):

    def __init__(self, *args, **kwargs):
        import time
        time.sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)

        return Singleton._instance


def task():
    obj = Singleton.get_instance()
    print(obj)


# for i in range(10):
#     t = threading.Thread(target=task)
#     t.start()


# 使用__new__函数实现
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(id(obj1))
print(id(obj2))
