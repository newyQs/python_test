from multiprocessing import Process

sharedata = []


def func(name):
    sharedata.append(name)
    print(f'我是：{name}，sharedata的值是：{sharedata}，shareddata的地址是：{id(sharedata)}')


if __name__ == '__main__':
    p1 = Process(target=func, args=("进程1",))
    p2 = Process(target=func, args=("进程2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("我是：主进程，sharedata的值是:", sharedata)

# 全局列表sharedata没有起到任何作用，在主进程和子进程中，sharedata指向内存中不同的列表
