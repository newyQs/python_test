'''
需求：
　　 实现在装饰器函数中，保留 被装饰函数 的元数据
    那什么是函数的元数据？

       在函数对象中保存着一些函数的元数据，如：

              f.__name__           函数名

              f.__doc__              函数文档

              f.__moudle__       函数所属模块名

              f.__dict__              属性字典

              f.__defaults__       默认参数组

              ……
'''

import time
from functools import (wraps, update_wrapper, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)


def count_time(func):
    """
    给目标函数加上计算运行时间统计
    """

    # 这个装上器和update_wrapper一样，默认参数WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        # 定义result接收函数返回值，并且在装饰函数最后返回回去
        resutl = func(*args, **kwargs)
        print('运行时间：', time.time() - start_time)
        return resutl

    # 其中默认参数 WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES
    # update_wrapper(wrapper, func)
    return wrapper


@count_time
def add(num=100):
    """
    计算 0~num 累加值，默认num=100
    """
    time.sleep(1)
    return sum([x for x in range(num + 1)])


if __name__ == '__main__':
    print('函数名：', add.__name__)
    print('属性字典：', add.__dict__)
    print('函数默认参数：', add.__defaults__)
    print('函数所在模块：', add.__module__)
    print('函数文档：', add.__doc__)

    # 打印两个默认参数
    # WRAPPER_ASSIGNMENTS ：__module__', '__name__', '__qualname__', '__doc__', '__annotations__
    # WRAPPER_UPDATES：__dict__
    print(WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)
    result = add()
    print(result)