from multiprocessing import Process, Manager
import os


def func(key, share_data):
    share_data[key] = '我是进程' + str(os.getpid())
    print(share_data)


if __name__ == '__main__':
    share_data = Manager().dict()

    p1 = Process(target=func, args=("lucy", share_data))
    p1.start()

    p2 = Process(target=func, args=("jack", share_data))
    p2.start()

    p1.join()
    p2.join()

    share_data["贾跃亭"] = "我是进程" + str(os.getpid())
    print(share_data)

'''
通过 Manager 类也可以实现进程间数据的共享:
Manager() 返回的 manager 对象提供一个服务进程，使得其他进程可以通过代理的方式操作 Python 对象。
manager 对象支持 list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value ,Array等多种格式
'''
