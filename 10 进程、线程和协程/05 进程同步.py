from multiprocessing import Process, Array
from multiprocessing import RLock, Lock, Event, Condition, Semaphore
import time
import os


def func(data, share_data, lc):
    lc.acquire()
    share_data[0] += data
    time.sleep(2)
    print(f'进程{os.getpid()}修改share_data里面的数据为：{share_data[0]}')
    lc.release()


if __name__ == '__main__':
    share_data = Array('i', 1)
    lock = RLock()
    share_data[0] = 1
    p1 = Process(target=func, args=(10, share_data, lock))
    p2 = Process(target=func, args=(20, share_data, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
'''
由于多进程是并发执行的，如果多个进程“同时”写某个共享变量，就有可能出现的问题，
我们可以设置进程锁来防止多个进程同时写，也就是说把写操作给锁起来，同时只能有一个进程进入这个写操作。
在 multiprocessing 里也有同名的锁类 RLock，Lock，Event，Condition和 Semaphore，连用法都是一样样的
'''