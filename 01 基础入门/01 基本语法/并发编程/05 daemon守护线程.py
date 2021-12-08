"""
当程序中拥有多个线程时，主线程执行结束并不会影响子线程继续执行。换句话说，只有程序中所有线程全部执行完毕后，程序才算真正结束。

除此之外，Python 还支持创建另一种线程，称为守护线程（或后台线程）。
此类线程的特点是，当程序中主线程及所有非守护线程执行结束时，未执行完毕的守护线程也会随之消亡（进行死亡状态），程序将结束运行。

Python 解释器的垃圾回收机制就是守护线程的典型代表，当程序中所有主线程及非守护线程执行完毕后，垃圾回收机制也就没有再继续执行的必要了。

护线程本质也是线程，因此其创建方式和普通线程一样，唯一不同之处在于，将普通线程设为守护线程，需通过线程对象调用其 damon 属性，将该属性的值该为 True。

并且需要注意的一点是，线程对象调用 daemon 属性必须在调用 start() 方法之前，否则 Python 解释器将报 RuntimeError 错误。
"""
import threading


# 定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(length):
    for arc in range(length):
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + str(arc))


# 创建线程
thread = threading.Thread(target=action, args=(20,))
# 将thread设置为守护线程
thread.daemon = True
# 启动线程
thread.start()
# 主线程执行如下语句
for i in range(5):
    print(threading.current_thread().getName())

"""
程序中第 26 行代码处，通过调用 thread 线程的 daemon 属性并赋值为 True，则该 thread 线程就变成了守护线程。
由于该程序中除了 thread 守护线程就只有主线程 MainThread，因此只要主线程执行结束，则守护线程将随之消亡。
"""