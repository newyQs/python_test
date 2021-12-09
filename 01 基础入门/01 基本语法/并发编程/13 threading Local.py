"""

"""
import threading

# 创建全局ThreadLocal对象:
local = threading.local()


def process():
    # 3.获取当前线程关联的resource:
    res = local.resource
    print(res + "http://c.biancheng.net/python/")


def process_thread(res):
    # 1.为当前线程绑定ThreadLocal的resource:
    local.resource = res
    # 2.线程的调用函数不需要传递res了，可以通过全局变量local访问
    process()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('t1线程',))
    t2 = threading.Thread(target=process_thread, args=('t2线程',))
    t1.start()
    t2.start()
