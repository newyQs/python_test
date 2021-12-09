"""

"""
import multiprocessing


def process_fun(queue, name):
    print(multiprocessing.current_process().pid, "进程放数据：", name)
    # 将 name 放入队列
    queue.put(name)


if __name__ == '__main__':
    # 创建进程通信的Queue
    queue = multiprocessing.Queue()
    # 创建子进程
    process = multiprocessing.Process(target=process_fun, args=(queue, "http://c.biancheng.net/python/"))
    # 启动子进程
    process.start()
    # 该子进程必须先执行完毕
    process.join()
    print(multiprocessing.current_process().pid, "取数据：")
    print(queue.get())
