https://blog.csdn.net/weixin_44604541/article/details/117229684

## 1 创建进程（Process）

multiprocessing模块提供了一个Process类可以创建进程对象

创建进程有两种方式：
+ 第一种通过Process类直接创建，参数target指定子进程要执行的程序
+ 第二种通过继承Process类来实现。

我们先用第一种方式创建子进程，子进程会将传递给它的参数扩大一倍，代码如下：
```python
# -*- coding:utf8 -*-
import os
from multiprocessing import Process, current_process


def doubler(number):
    result = number * 2
    # 获取子进程ID
    proc_id = os.getpid()
    # 获取子进程名称
    proc_name = current_process().name
    print('proc_id:{0} proc_name:{1} result:{2}'.format(proc_id, proc_name, result))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    p_list = list()
    # 父进程ID和名称
    print('parent_proc_id:{0} parent_proc_name:{1}'.format(os.getpid(), current_process().name))

    for num in numbers:
        # 创建子进程
        p = Process(target=doubler, args=(num,))
        p_list.append(p)
        # 启动子进程
        p.start()

    # join方法会让父进程等待子进程结束后再执行
    for p in p_list:
        p.join()

    print("Done.")
```

第二种方式通过继承Process类，并重写run方法：
```python
# -*- coding:utf8 -*-
import os
from multiprocessing import Process, current_process


class MyProcess(Process):
    def __init__(self, number):
        # 必须调用父类的init方法
        super(MyProcess, self).__init__()
        self.number = number

    def run(self):
        result = self.number * 2
        # 获取子进程ID
        # self.pid
        proc_id = os.getpid()
        # 获取子进程名称
        # self.name
        proc_name = current_process().name
        print('proc_id:{0} proc_name:{1} result:{2}'.format(proc_id, proc_name, result))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    p_list = []
    # 父进程的ID和名称
    print('parent_proc_id:{0} parent_proc_name:{1}'.format(os.getpid(), current_process().name))

    for num in numbers:
        # 创建子进程
        p = MyProcess(num)
        p_list.append(p)
        # 启动子进程，启动一个新进程实际就是执行本进程对应的run方法
        p.start()

    # join方法会让父进程等待子进程结束后再执行
    for p in p_list:
        p.join()

    print("Done.")
```

## 2 进程锁（Lock）

multiprocessing模块和threading模块一样也支持锁。通过acquire获取锁，执行操作后通过release释放锁。
```python
# -*- coding:utf8 -*-
from multiprocessing import Process, Lock


def printer(item, lock):
    # 获取锁
    lock.acquire()
    try:
        print(item)
    except Exception as e:
        print(e)
    else:
        print('no exception.')
    finally:
        # 释放锁
        lock.release()


if __name__ == '__main__':
    # 实例化全局锁
    lock = Lock()
    items = ['PHP', 'Python', 'Java']
    p_list = list()

    for item in items:
        p = Process(target=printer, args=(item, lock))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    print('Done.')
```

## 3 进程池（Pool）

Pool类表示工作进程的池子，它可以提供指定数量的进程供用户调用，当有请求提交到进程池时，如果进程池有空闲进程或进程数还没到达指定上限，就会分配一个进程响应请求，否则请求只能等待。Pool类主要在执行目标多且需要控制进程数量的情况下使用，如果目标少且不用控制进程数量可以使用Process类。

进程池可以通过map和apply_async方法来调用执行代码，首先我们来看map方法：
```python
# -*- coding:utf8 -*-
import os
from multiprocessing import Pool, current_process


def doubler(number):
    result = number * 2
    proc_id = os.getpid()
    proc_name = current_process().name
    print('proc_id:{0} proc_name:{1} result:{2}'.format(proc_id, proc_name, result))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    pool = Pool(processes=3)
    pool.map(doubler, numbers)

    # 关闭pool使其不再接受新的任务
    pool.close()

    # 关闭pool，结束工作进程，不在处理未完成的任务
    # pool.terminate()

    # 主进程阻塞，结束工作进程，不再处理未完成的任务，join方法要在close或terminate之后使用
    pool.join()

    print('Done')
```

map只能向处理函数传递一个参数。

下面来看一下apply/apply_async函数，apply函数是阻塞的，apply_async函数是非阻塞的，这里我们以apply_async函数为例：
```python
# -*- coding:utf8 -*-
import os
import time
from multiprocessing import Pool, current_process


def doubler(number, parent_proc_id, parent_proc_name):
    result = number * 2
    proc_id = os.getpid()
    proc_name = current_process().name
    # 设置等待时间，可以验证apply和apply_async的阻塞和非阻塞
    time.sleep(2)
    print('parent_proc_id:{0} parent_proc_name:{1} proc_id:{2} proc_name:{3} number:{4} result:{5}'.format(
        parent_proc_id, parent_proc_name, proc_id, proc_name, number, result))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    parent_proc_id = os.getpid()
    parent_proc_name = current_process().name
    pool = Pool(processes=3)
    for num in numbers:
        # 非阻塞
        pool.apply_async(doubler, (num, parent_proc_id, parent_proc_name))
        # 阻塞其它进程
        # pool.apply_async(doubler, (num, parent_proc_id, parent_proc_name))

    # 关闭pool使其不再接受新的任务
    pool.close()

    # 关闭pool，结束工作进程，不在处理未完成的任务
    # pool.terminate()

    # 主进程阻塞，结束工作进程，不再处理未完成的任务，join方法要在close或terminate之后使用
    pool.join()

    print('Done')
```

## 4 进程间通信（Pipe、Queue)

进程间通信的方式一般有管道（Pipe）、信号（Signal）、消息队列（Message）、信号量（Semaphore）、共享内存（Shared Memory）、套接字（Socket）等。这里我们着重讲一下在Python多进程编程中常用的进程方式multiprocessing.Pipe函数和multiprocessing.Queue类。

### 1、Pipe

multiprocessing.Pipe()即管道模式，调用Pipe()方法返回管道的两端的Connection。Pipe方法返回(conn1, conn2)代表一个管道的两个端。Pipe方法有duplex参数，如果duplex参数为True(默认值)，那么这个管道是全双工模式，也就是说conn1和conn2均可收发；duplex为False，conn1只负责接受消息，conn2只负责发送消息。send()和recv()方法分别是发送和接受消息的方法。一个进程从Pipe某一端输入对象，然后被Pipe另一端的进程接收，单向管道只允许管道一端的进程输入另一端的进程接收，不可以反向通信；而双向管道则允许从两端输入和从两端接收。
```python
# -*- coding:utf8 -*-
import os, time
from multiprocessing import Process, Pipe, current_process


def proc1(pipe, data):
    for msg in range(1, 6):
        print('{0} 发送 {1}'.format(current_process().name, msg))
        pipe.send(msg)
        time.sleep(1)
    pipe.close()


def proc2(pipe, length):
    count = 0
    while True:
        count += 1
        if count == length:
            pipe.close()
        try:
            # 如果没有接收到数据recv会一直阻塞，如果管道被关闭，recv方法会抛出EOFError
            msg = pipe.recv()
            print('{0} 接收到 {1}'.format(current_process().name, msg))
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    conn1, conn2 = Pipe(True)
    data = range(0, 6)
    length = len(data)
    proc1 = Process(target=proc1, args=(conn1, data))
    proc2 = Process(target=proc2, args=(conn2, length))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    print('Done.')
```

### 2、Queue

Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。Queue的使用主要是一边put()，一边get()，但是Queue可以是多个Process进行put()操作，也可以是多个Process进行get()操作。 put方法用来插入数据到队列中，put方法还有两个可选参数：block和timeout。如果block为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果block为False，但该Queue已满，会立即抛出Queue.Full异常。 get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：block和timeout。如果block为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果block为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值；否则，如果队列为空，则立即抛出Queue.Empty异常。

在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
```python
# -*- coding:utf8 -*-
import os, time, random
from multiprocessing import Process, Queue


def write(q):
    print('Process to write: %s' % os.getpid())
    for val in range(0, 6):
        print('Put %s to queue...' % val)
        q.put(val)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        try:
            val = q.get(block=True, timeout=5)
            print('Get %s from queue.' % val)
        except Exception as e:
            if q.empty():
                print('队列消费完毕.')
                break


if __name__ == '__main__':
    q = Queue()

    proc1 = Process(target=write, args=(q,))
    proc2 = Process(target=read, args=(q,))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    # 如果proc2不break的话会一直阻塞，不调用join调用terminate方法可以终止进程
    # proc2.terminate()

    print('Done.')
```

Pipe的读写效率要高于Queue。那么我们如何的选择它们呢？
+ 如果你的环境是多生产者和消费者，那么你只能是选择queue队列
+ 如果两个进程间处理的逻辑简单，但是就是要求绝对的速度，那么pipe是个好选择

## 5 共享内存（Value、Array）

共享内存

主要通过 Value 或者 Array 来实现。常见的共享的有以下几种：
```text
In : from multiprocessing.sharedctypes import typecode_to_type

In : typecode_to_type
Out:
{'B': ctypes.c_ubyte,
 'H': ctypes.c_ushort,
 'I': ctypes.c_uint,
 'L': ctypes.c_ulong,
 'b': ctypes.c_byte,
 'c': ctypes.c_char,
 'd': ctypes.c_double,
 'f': ctypes.c_float,
 'h': ctypes.c_short,
 'i': ctypes.c_int,
 'l': ctypes.c_long,
 'u': ctypes.c_wchar}
```

而且共享的时候还可以给 Value 或者 Array 传递 lock 参数来决定是否带锁，如果不指定默认为 RLock。

我们看一个例子：
```python
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_bool, c_double

lock = Lock()


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def modify(n, b, s, arr, A):
    n.value **= 2
    b.value = True
    s.value = s.value.upper()
    arr[0] = 10
    for a in A:
        a.x **= 2
        a.y **= 2


n = Value('i', 7)
b = Value(c_bool, False, lock=False)
s = Array('c', 'hello world', lock=lock)
arr = Array('i', range(5), lock=True)
A = Array(Point, [(1.875, -6.25), (-5.75, 2.0)], lock=lock)

p = Process(target=modify, args=(n, b, s, arr, A))
p.start()
p.join()

print(n.value)
print(b.value)
print(s.value)
print(arr[:])
print([(a.x, a.y) for a in A])
```

有 2 点需要注意：
+ 并不是只支持 typecode_to_type 中指定那些类型，只要在 ctypes 里面的类型就可以。
+ arr 是一个 int 的数组，但是和 array 模块生成的数组以及 list 是不一样的，它是一个 SynchronizedArray 对象，支持的方法很有限，比如 append/extend 等方法是没有的。

输出结果如下：
```python
❯ python shared_memory.py
49
True
HELLO WORLD
[10, 1, 2, 3, 4]
[(3.515625, 39.0625), (33.0625, 4.0)]
```

## 6 服务器进程（Manager）

一个 multiprocessing.Manager 对象会控制一个服务器进程，其他进程可以通过代理的方式来访问这个服务器进程。 常见的共享方式有以下几种：

Namespace。创建一个可分享的命名空间。
Value/Array。和上面共享 ctypes 对象的方式一样。
dict/list。创建一个可分享的 dict/list，支持对应数据结构的方法。
Condition/Event/Lock/Queue/Semaphore。创建一个可分享的对应同步原语的对象。

看一个例子：
```python
from multiprocessing import Manager, Process


def modify(ns, lproxy, dproxy):
    ns.a **= 2
    lproxy.extend(['b', 'c'])
    dproxy['b'] = 0


manager = Manager()
ns = manager.Namespace()
ns.a = 1
lproxy = manager.list()
lproxy.append('a')
dproxy = manager.dict()
dproxy['b'] = 2

p = Process(target=modify, args=(ns, lproxy, dproxy))
p.start()
print('PID:', p.pid)
p.join()

print(ns.a)
print(lproxy)
print(dproxy)
```

在 id 为 8341 的进程中就可以修改共享状态了：
```python
❯ python manager.py
PID: 8341
1
['a', 'b', 'c']
{'b': 0}
```

## 7 查看当前状况（cpu_count、active_children）

另外还可以通过 cpu_count() 方法还有 active_children() 方法获取当前机器的 CPU 核心数量以及得到目前所有的运行的进程。
```python
import multiprocessing


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
```

## 8、例子

（1）process、lock与value
```python
import multiprocessing as mp
import time

def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1) 
        v.value += num # 获取共享内存
        print(v.value)
    l.release() # 释放


def multicore():
    l = mp.Lock() # 定义一个进程锁
    #l = 1
    v = mp.Value('i', 0) # 定义共享内存
    p1 = mp.Process(target=job, args=(v,1,l)) # 需要将lock传入
    p2 = mp.Process(target=job, args=(v,3,l)) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__=='__main__':
    multicore()

```
上述代码即对共享内存叠加5次，p1进程每次叠加1，p2进程每次叠加3，为了避免p1与p2在运行时抢夺共享数据v，在进程执行时锁住了该进程，从而保证了执行的顺序。我测试了三个案例：

直接运行上述代码输出[1, 2, 3, 4, 5, 8, 11, 14, 17, 20]，运行时间为1.037s
在1的基础上注释掉锁（上述注释了三行），在没有锁的情况下，输出[1, 4, 5, 8, 9, 12, 13, 15, 14, 16],运行时间为0.53s
在2的基础上将p1.join()调到p2.start()前面，输出为[1, 2, 3, 4, 5, 8, 11, 14, 17, 20]，运行时间为1.042s.
可以发现，没锁的情况下调整join可以取得与加锁类似的结果，这是因为join即是阻塞主进程，直至当前进程结束才回到主进程，若将p1.join（）放到p1.start()后面，则会马上阻塞主进程，使得p2要稍后才开始，这与锁的效果一样。

如果如上述代码所示，p1.join（）在p2.start()后面，虽然是p1先join()，但这时只是阻塞了主进程，而p2是兄弟进程，它已经开始了，p1就不能阻止它了，所以这时如果没锁的话p1与p2就是并行了，运行时间就是一半，但因为它们争抢共享变量，所以输出就变得不确定了。

（2）pool
```python
import multiprocessing as mp
#import pdb

def job(i):
    return i*i

def multicore():
    pool = mp.Pool()
    #pdb.set_trace()
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    # 用get获得结果
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])

multicore()

```

pool其实非常好用，特别是map与apply_async。通过pool这个接口，我们只有指定可以并行的函数与函数参数列表，它就可以自动帮我们创建多进程池进行并行计算，真的不要太方便。

pool特别适用于数据并行模型，假如是消息传递模型那还是建议自己通过process来创立进程吧

3、其他
（1）注意事项
尽量避免共享数据
所有对象都尽量是可以pickle的
避免使用terminate强行终止进程，以造成不可预料的后果
有队列的进程在终止前队列中的数据需要清空，join操作应放到queue清空后
明确给子进程传递资源、参数
windows平台另需注意：

注意跨模块全局变量的使用，可能被各个进程修改造成结果不统一
主模块需要加上if name == 'main':来提高它的安全性，如果有交互界面，需要加上freeze_support()


（2）dummy
一些开源项目代码，好多人在用 multiprocessing.dummy 这个子模块，「dummy」这个词有「模仿」的意思，它虽然在多进程模块的代码中，但是接口和多线程的接口基本一样。官方文档中这样说：

multiprocessing.dummy replicates the API of multiprocess ing but is no more than a wrapper around the threading module.

恍然大悟！！！如果分不清任务是 CPU 密集型还是 IO 密集型，就用如下 2 个方法分别试：

from multiprocessing import Pool
from multiprocessing.dummy import Pool
1
2
哪个速度快就用哪个，尽量在写兼容的方式，这样在多线程 / 多进程之间切换非常方便

还有一点：现在，如果一个任务拿不准是 CPU 密集还是 I/O 密集型，且没有其它不能选择多进程方式的因素，都统一直接上多进程模式
