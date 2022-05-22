import multiprocessing
import time


def process(num):
    print("Process:%d" % num)


if __name__ == '__main__':
    for i in range(8):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()
    print('CPU核心数量:' + str(multiprocessing.cpu_count()))  # 查看当前机器CPU核心数量
    # 目前所有的运行的进程
    for p in multiprocessing.active_children():
        print('子进程名称: ' + p.name + ' id: ' + str(p.pid))
    print('进程结束')
