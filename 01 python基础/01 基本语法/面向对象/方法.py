"""
静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用。

普通方法: 默认有个self参数，且只能被对象调用。

类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器。

逻辑上类方法应当只被类调用，实例方法实例调用，静态方法两者都能调用。
主要区别在于参数传递上的区别，实例方法悄悄传递的是self引用作为参数，而类方法悄悄传递的是 cls 引用作为参数。
"""


class Test(object):
    def InstanceFun(self):
        print("InstanceFun")
        print(self)

    @classmethod
    def ClassFun(cls):
        print("ClassFun")
        print(cls)

    @staticmethod
    def StaticFun():
        print("StaticFun")


t = Test()

t.InstanceFun()  # 输出InstanceFun，打印对象内存地址“<__main__.Test object at 0x0293DCF0>”
t.StaticFun()  # 输出StaticFun
t.ClassFun()  # 输出ClassFun，打印类位置 <class '__main__.Test'>
t.ClassFun(Test)  # 错误   classFun() takes exactly 1 argument (2 given)

Test.ClassFun()  # 输出ClassFun，打印类位置 <class '__main__.Test'>
Test.StaticFun()  # 输出StaticFun
Test.InstanceFun()  # 错误，TypeError: unbound method instanceFun() must be called with Test instance as first argument
Test.InstanceFun(t)  # 输出InstanceFun，打印对象内存地址“<__main__.Test object at 0x0293DCF0>”


