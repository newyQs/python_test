'''
案例：

       为分析程序内哪些函数执行时间开销较大，我们需定义一个带timeout参数的装饰器

       需求：

　　　　统计被装饰函数的运行时间

　　　　时间大于timeout时，将此次函数调用记录到log日志中

　　　　运行时可以修改timeout的值
'''

import time
import logging
from random import randint


def run_time(timeout):
    """
    定义检查函数运行时间，并打印对应函数运行时间超出设定时间日志，并支持更改timeout
    """

    # python2
    # timeout = [timeout]

    # 真正包裹函数
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            used_time = time.time() - start_time

            # 对于超出timeout的函数进行日志打印
            if used_time > timeout:
                msg = '%s: %s > %s' % (func.__name__, used_time, timeout)
                logging.warn(msg)

                # python2
                # if used_time > timeout[0]:
                #     msg = '%s: %s > %s' % (func.__name__, used_time, timeout[0])
                #     logging.warn(msg)
                # return result
            return result

        # 设置timeout参数值
        def set_timeout(value):
            # 声明嵌套域变量，可以更改，python2通过把列表形式进行更改
            nonlocal timeout
            timeout = value

        # 定义接口
        wrapper.set_timeout = set_timeout

        # python2
        # def set_timeout(value):
        #     timeout[0] = value
        # wrapper.set_timeout = set_timeout

        return wrapper

    return out_wrapper


@run_time(1.5)
def func():
    # 随机有50%的几率程序沉睡1秒
    while randint(0, 1):
        time.sleep(1)
    print('func_run')


if __name__ == "__main__":
    for _ in range(10):
        func()

    print('_' * 50)

    # 更改run_time装饰器中timeout参数
    func.set_timeout(2)
    for _ in range(10):
        func()