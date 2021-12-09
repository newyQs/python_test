"""

"""
import threading


# 创建子线程类，继承自 Thread 类
class MyThread(threading.Thread):
    def __init__(self, add):
        # threading.Thread.__init__(self)
        # super(my_Thread, self).__init__()
        super().__init__()
        self.add = add

    # 重写run()方法
    def run(self):
        for arc in self.add:
            # 调用 getName() 方法获取当前执行该程序的线程名
            print(threading.current_thread().getName() + " " + arc)


# 定义为 run() 方法传入的参数
my_tuple = (
    "http://c.biancheng.net/python/",
    "http://c.biancheng.net/shell/",
    "http://c.biancheng.net/java/"
)

if __name__ == '__main__':
    # 创建子线程
    my_thread = MyThread(my_tuple)
    # 启动子线程
    my_thread.start()
    # 主线程执行此循环
    for i in range(5):
        print(threading.current_thread().getName())
