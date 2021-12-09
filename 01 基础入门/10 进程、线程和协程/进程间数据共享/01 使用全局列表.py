'''
说明：
 全局列表share_data没有起到任何作用。
 这是因为在主进程和子进程中，share_data指向内存中不同的列表
'''
from multiprocessing import Process

share_data = []


def func(name):
    share_data.append(name)
    print(f'我是：{name}，share_data的值是：{share_data}，share_data的地址是：{id(share_data)}')


if __name__ == '__main__':
    p1 = Process(target=func, args=("进程1",))
    p2 = Process(target=func, args=("进程2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("我是：主进程，share_data的值是:", share_data)

