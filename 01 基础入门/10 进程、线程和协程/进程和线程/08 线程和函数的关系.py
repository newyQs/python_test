import threading


def func():
    print('func 函数当前线程 %s' % threading.current_thread().name)


def xx():
    print('xx 函数当前线程 %s' % threading.current_thread().name)
    func()


if __name__ == '__main__':
    print('main 函数当前线程 %s' % threading.current_thread().name)
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=xx)
    t1.start()
    t2.start()
    func()
    t1.join()
    t2.join()

'''
线程是操作系统给进程分配和管理的，而线程一般是依托于某个函数去执行;
所以哪个线程调用哪个函数，这个函数内的代码就属于哪个线程的;
当线程依托的函数结束，该线程也就结束了;
'''
