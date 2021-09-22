import threading
import time

'''
有一个子线程里面有死循环存在，主线程里面有个 count，我们想让 count 值等于 5 的时候，结束掉该子线程。
在子线程里面补充完成代码
'''


def func():
    while True:
        time.sleep(1)
        print('func 函数当前线程 %s' % threading.current_thread().name)
        pass  # 在此完成代码


if __name__ == '__main__':
    print('main 函数当前线程 %s' % threading.current_thread().name)
    t1 = threading.Thread(target=func)
    t1.start()

    count = 10
    while count:
        count -= 1
        time.sleep(1)
