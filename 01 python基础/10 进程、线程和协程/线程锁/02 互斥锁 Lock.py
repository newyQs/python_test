import threading


def calculate(num):
    global totalnum
    for i in range(1000000):
        lock.acquire()
        totalnum += num
        totalnum -= num
        lock.release()


if __name__ == '__main__':
    lock = threading.Lock()  # 通过threading.Lock()创建一个锁
    totalnum = 0

    t1 = threading.Thread(target=calculate, args=(3,))
    t2 = threading.Thread(target=calculate, args=(7,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(totalnum)
'''
上锁。锁只有一个，无论有多少个线程，同一时刻只能有一个线程持有该锁，所以不会造成冲突。
Python 在 threading 模块中定义了几种线程锁类，分别是：
Lock 互斥锁
RLock 可重入锁
Semaphore 信号
Event 事件
Condition 条件
Barrier “阻碍”
'''
