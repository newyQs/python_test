'''
signal.alarm()
注意两点：一是signal信号机制要在linux上才能运行； 二是signal信号在主线程中才会起作用
'''
import time
import signal


class TimeoutError(Exception):
    """自定义超时异常类"""

    def __init__(self, msg):
        super(TimeoutError, self).__init__()
        self.msg = msg


def time_out(interval, callback):
    """超时处理"""
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError("run func timeout")

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)  # interval秒后向进程发送SIGALRM信号
                result = func(*args, **kwargs)
                signal.alarm(0)  # 函数在规定时间执行完后关闭alarm闹钟
                return result
            except TimeoutError as e:
                callback(e)

        return wrapper

    return decorator


def timeout_callback(e):
    '''超时异常后的操作'''
    print(e.msg)


@time_out(2, timeout_callback)
def task1():
    print("task1 start")
    time.sleep(3)
    print("task1 end")


@time_out(2, timeout_callback)
def task2():
    print("task2 start")
    time.sleep(1)
    print("task2 end")


if __name__ == "__main__":
    task1()
    task2()
