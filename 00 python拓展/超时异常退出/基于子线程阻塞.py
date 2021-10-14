import time
import threading


def callback_func():
    print('超时回调')


def time_out(interval, callback=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            t.setDaemon(True)  # 设置主线程结束，则子线程立刻结束
            t.start()
            t.join(interval)  # 主线程阻塞等待interval秒
            if t.is_alive() and callback:
                return threading.Timer(0, callback).start()  # 立即执行回调函数
            else:
                return

        return wrapper

    return decorator


@time_out(2, callback_func)
def task3(hh):
    print('**********task3****************')
    for i in range(3):
        time.sleep(1)
        print(i)
        print(hh)


@time_out(2, callback_func)
def task4(hh):
    print('**********task4****************')
    for i in range(3):
        # time.sleep(1)
        print(i)
        print(hh)


if __name__ == '__main__':
    task3('参数')
    task4('参数')
