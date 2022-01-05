import contextlib


@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    # 【重点】：yield
    yield file_handler

    # __exit__方法
    print('close file:', file_name, 'in __exit__')
    file_handler.close()
    return


with open_func('/Users/MING/mytest.txt') as file_in:
    for line in file_in:
        print(line)

"""
在被装饰函数里，必须是一个生成器（带有yield），而yield之前的代码，就相当于__enter__里的内容。
yield 之后的代码，就相当于__exit__ 里的内容。
上面这段代码只能实现上下文管理器的第一个目的（管理资源），并不能实现第二个目的（处理异常）。
如果要处理异常，可以改成下面这个样子。
"""


@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    try:
        yield file_handler
    except Exception as exc:
        # deal with exception
        print('the exception was thrown')
    finally:
        print('close file:', file_name, 'in __exit__')
        file_handler.close()

        return


with open_func('/Users/MING/mytest.txt') as file_in:
    for line in file_in:
        1 / 0
        print(line)
