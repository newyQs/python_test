'''
https://www.cnblogs.com/wongbingming/p/10519553.html
https://www.jianshu.com/p/7bae11eaf84d
http://www.hechaku.com/arcitle/20186243.html

with 语句：上下文管理器
上下文管理器，让我们在需要的时候，可以准确的分配和释放资源
上下文管理器，用于锁定（locking）,解锁（unlocking）或关闭开启的文件

1. 上下文表达式：with open('testAPI.txt') as f:
2. 上下文管理器：open('testAPI.txt')
3. f 不是上下文管理器，应该是资源对象。

是在一个类里，实现了__enter__和__exit__的方法，这个类的实例就是一个上下文管理器
'''
# with语句可以确保我们的文件对象最终被关闭掉
with open('testAPI.txt', 'r') as f:
    print(f.read())

# 等价于：
try:
    f = open('testAPI.txt', 'r')
    print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

'''
with语句的底层原理：
遇到with语句时：
1。__enter__方法先被执行，并返回一个变量,返回的变量即赋值给 as 后的变量
2。执行语句块 
3。执行__exit__方法

在编写代码时，可以将资源的连接或者获取放在__enter__中，而将资源的关闭写在__exit__ 中。
'''


class File:
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        print('来了')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        print('走了')
        self.file.close()
        return True


with File('testAPI.txt') as f:
    print('hello')

'''
在__exit__中处理异常
其3个参数：exc_type, exc_val, exc_tb
exc_type:异常对象所属的类（异常类型）
exc_val:异常对象本身（异常值）
exc_tb:一个异常处理器到异常被抛出的点的栈追踪器（异常的错误栈信息）
当主逻辑代码没有报异常时，这三个参数将都为None
如果我们想忽视异常，则加上一个 return True
'''

'''
使用生成器语法实现一个上下文管理器
'''
from contextlib import contextmanager


@contextmanager
def file(filename):
    ff = open(filename)
    try:
        yield ff
    finally:
        ff.close()


with file('testAPI.txt') as ff:
    print('hello')
