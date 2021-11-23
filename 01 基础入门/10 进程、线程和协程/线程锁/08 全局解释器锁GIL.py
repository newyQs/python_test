print()
'''
在大多数环境中，本质上在某一时刻单核CPU只能有一个线程被执行，多核CPU则可以支持多个线程同时执行。
但是在python中，无论CPU有多少核，同时只能执行一个线程，只就是由于GIL导致的。
python中的某个线程想要执行，必须先拿到GIL，并且在同一个进程中，GIL只有一个。
GIL只有在CPython解释器中才有，因为CPython调用的是c语言的原生线程，不能直接操作cpu，只能利用GIL保证同一时间只能
有一个线程拿到数据。在PyPy和JPython中没有GIL。

针对不同类型的任务，多线程执行效率是不同的：
    CPU密集型?(各种循环处理、计算等等)，由于计算工作多，ticks 计数很快就会达到阈值，
    然后触发 GIL 的释放与再竞争（多个线程来回切换是需要消耗资源的），所以 Python 下的多线程对 CPU 密集型任务并不友好，
    对于计算密集型的业务，我们可以使用多进程来充分利用多核 CPU。

    IO密集型？(文件处理、网络通信等涉及数据读写的操作)，多线程能够有效提升效率(单线程下有 IO 操作会进行 IO 等待，
    造成不必要的时间浪费，而开启多线程能在线程A等待时，自动切换到线程 B，可以不浪费 CPU 的资源，从而能提升程序执行效率)。
    所以 Python 的多线程对 IO 密集型任务比较友好。
    
为什么不去掉GIL？
    很难
    
使用建议：
    python想要充分利用多核CPU，就用多进程，因为每个进程有各自独立的GIL，互不干扰。
    在python中，多进程的执行效率优于多线程（仅针对多核CPU而言）。
    建议在IO密集型使用多线程，计算密集型使用多进程。
'''
import time


def counter():
    count = 1
    data = 1
    while count < 500000:
        count += 1
        data += data


if __name__ == '__main__':
    bgtime = time.time()
    counter()
    counter()
    endtime = time.time()

    print(f'单线程用时:{endtime - bgtime}')
