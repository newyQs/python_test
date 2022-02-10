"""
位于 time 模块中的 sleep(secs) 函数，可以实现令当前执行的线程暂停 secs 秒后再继续执行。
所谓暂停，即令当前线程进入阻塞状态，当达到 sleep() 函数规定的时间后，再由阻塞状态转为就绪状态，等待 CPU 调度。
"""
import threading
import time


# 定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(*add):
    for arc in add:
        # 暂停 0.1 秒后，再执行
        time.sleep(0.1)
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + arc)


# 定义为线程方法传入的参数
my_tuple = ("http://c.biancheng.net/python/",
            "http://c.biancheng.net/Shell/",
            "http://c.biancheng.net/java/")
# 创建线程
thread = threading.Thread(target=action, args=my_tuple)
# 启动线程
thread.start()
# 主线程执行如下语句
for i in range(5):
    print(threading.current_thread().getName())

"""
可以看到，和未使用 sleep() 函数的输出结果相比，显然主线程 MainThread 在前期获得 CPU 资源的次数更多，
因为 Thread-1 线程中调用了 sleep() 函数，在一定程序上会阻碍该线程获得 CPU 调度。
"""