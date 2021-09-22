import threading


def calculate(num):
    global totalnum

    for i in range(1000000):    # 注意：高级语言的一条语句在CPU执行时可能是若干条语句
        totalnum += num
        totalnum -= num


if __name__ == '__main__':
    totalnum = 0

    t1 = threading.Thread(target=calculate, args=(3,))
    t2 = threading.Thread(target=calculate, args=(7,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(totalnum)

'''
线程之间的任务执行是CPU随机调度的，并且每个线程可能只执行了n条指令之后就被切换到别的线程了。
当多个线程同时操作一个对象，如果没有很好的保护该对象，就会导致结果不符合预期，这种被称为线程不安全。
为了保证线程安全，我们设计了线程锁，即同一时刻只允许一个线程操作该数据。
线程锁用于锁定资源，可以同时使用多个锁。
'''