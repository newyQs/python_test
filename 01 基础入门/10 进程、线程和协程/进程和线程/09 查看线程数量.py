import threading
import time


def func():
    print('func 函数当前线程 %s' % threading.current_thread().name)
    time.sleep(2)  # 防止函数过快的退出


def xx():
    print('xx 函数当前线程 %s' % threading.current_thread().name)
    while True:  # 死循环
        pass


if __name__ == '__main__':
    print('文件及目录操作 函数当前线程 %s' % threading.current_thread().name)
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=xx)
    t1.start()
    t2.start()

    threading_names = threading.enumerate()  # 枚举出正在活动的线程，返回列表
    print("目前正在活动的线程:", threading_names)

    time.sleep(3)  # 3 秒后 t1 线程关联的函数 func 退出，t1 线程结束。

    threading_names = threading.enumerate()  # 枚举出正在活动的线程，返回列表
    print("目前正在活动的线程:", threading_names)  # 目前只有主线程和 t2 线程存在

