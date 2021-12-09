"""

"""
import threading


# 定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(*add):
    for arc in add:
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + arc)


if __name__ == '__main__':
    # 定义为线程方法传入的参数
    my_tuple = (
        "http://c.biancheng.net/python/",
        "http://c.biancheng.net/shell/",
        "http://c.biancheng.net/java/"
    )
    # 创建线程
    thread = threading.Thread(target=action, args=my_tuple)
    # 启动线程
    thread.start()
    # 指定 thread 线程优先执行完毕
    # thread 线程调用了 join() 方法，并且没有指定具体的 timeout 参数值。这意味着如果程序想继续往下执行，必须先执行完 thread 线程。
    thread.join()
    # 主线程执行如下语句
    for i in range(5):
        print(threading.current_thread().getName())
