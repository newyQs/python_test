import threading
import time


def terminate():
    global flag_running
    flag_running = False


def func():
    while flag_running:
        print("i'm running......")
        time.sleep(1)


if __name__ == '__main__':
    flag_running = True
    t = threading.Thread(target=func)
    t.start()

    count = 10
    while count:
        count -= 1
        if count == 5:
            terminate()
        time.sleep(1)

'''
threading模块的start函数可以启动线程，但是 threading 并没有提供暂停, 恢复和停止线程的方法, 
一旦线程对象调用 start 启动后，线程将由操作系统来全权管理，此时，对我们的应用程序来说该线程就属于失控状态，
只能等到对应的方法函数运行完毕，线程才会退出。

之所以想终止线程，是因为线程被卡在了一个地方，可能是 while True 循环，也可能是需要运算时间很长的语句，
总之，让线程退出是我们常见的需求，下面我们介绍几种方案：
第一种方案，调用 setDaemon(True) 方法，我们可以让子线程成为主线程的守护线程，这些线程会在主线程终止时自动销毁，
但是，这种方案局限性很大，比如，我们无法在主线程存活的情况下，主动结束子线程。
第二种方案，子线程带一个退出请求标志，在线程中不停的去轮询这个标志值，看是不是该自己离开了，
当你想让该线程退出的时候，你可以在其它线程中设置这个退出标志。
如果线程执行一些像 I/O 这样的阻塞操作，那么通过轮询来终止线程将使得线程之间的协调变得非常棘手。
比如，如果一个线程一直阻塞在一个 I/O 操作上，它就永远无法返回，也就无法检查自己是否已经被结束了。
我们可以利用超时循环来退出阻塞，让程序可以继续轮询退出标志
'''