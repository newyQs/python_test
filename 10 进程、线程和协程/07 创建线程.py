import threading


def func(args):
    print(f'我是第{args}个线程，我的线程号是：{threading.current_thread().name}')


if __name__ == '__main__':
    for i in range(1, 100):
        t = threading.Thread(target=func, args=(i,))
        t.start()
'''
进程是由若干线程组成的，一个进程至少有一个线程。
线程是操作系统直接执行的执行单元。
僵尸线程：子线程还没结束，主线程就已经结束了。建议加上t.join()方法
强制结束子线程：setDaemon(True)，该函数会把所有的子线程都变成主线程的守护线程，当主线程结束后，守护子线程也会随之结束，整个进程也跟着退出
'''