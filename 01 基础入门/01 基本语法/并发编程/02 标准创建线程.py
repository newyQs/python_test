"""
__init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)

此构造方法中，以上所有参数都是可选参数，即可以使用，也可以忽略。其中各个参数的含义如下：
    group：指定所创建的线程隶属于哪个线程组（此参数尚未实现，无需调用）；
    target：指定所创建的线程要调度的目标方法（最常用）；
    args：以元组的方式，为 target 指定的方法传递参数；
    kwargs：以字典的方式，为 target 指定的方法传递参数；
    daemon：指定所创建的线程是否为后代线程。

start
run
join
"""
import threading


# 定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(*add):
    for arc in add:
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + arc)


# 定义为线程方法传入的参数
my_tuple = ("http://c.biancheng.net/python/",
            "http://c.biancheng.net/shell/",
            "http://c.biancheng.net/java/")

if __name__ == '__main__':
    # 创建线程
    t = threading.Thread(target=action, args=my_tuple)

    t.start()
    t.join()

    for i in range(5):
        print(threading.current_thread().getName())
