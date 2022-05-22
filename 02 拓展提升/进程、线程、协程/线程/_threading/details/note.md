https://fishpond.blog.csdn.net/article/details/117251428

## 1、线程的使用

（1）普通创建方式
```python
import threading
import time

def run(n):
    print("task", n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=("t1",))
    t2 = threading.Thread(target=run, args=("t2",))
    t1.start()
    t2.start()
```

（2）自定义线程

继承threading.Thread来自定义线程类，其本质是重构Thread类中的run方法
```python
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()  # 重构run函数必须要写
        self.n = n

    def run(self):
        print("task", self.n)
        time.sleep(1)
        print('2s')
        time.sleep(1)
        print('1s')
        time.sleep(1)
        print('0s')
        time.sleep(1)

if __name__ == "__main__":
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    t1.start()
    t2.start()
```

（3）守护线程

我们看下面这个例子，这里使用setDaemon(True)把所有的子线程都变成了主线程的守护线程，因此当主进程结束后，子线程也会随之结束。所以当主线程结束后，整个程序就退出了。
```python
import threading
import time

def run(n):
    print("task", n)
    time.sleep(1)       #此时子线程停1s
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')

if __name__ == '__main__':
    t = threading.Thread(target=run, args=("t1",))
    t.setDaemon(True)   #把子进程设置为守护线程，必须在start()之前设置
    t.start()
    print("end")

```
我们可以发现，设置守护线程之后，当主线程结束时，子线程也将立即结束，不再执行。

（4）主线程等待子线程结束

为了让守护线程执行结束之后，主线程再结束，我们可以使用join方法，让主线程等待子线程执行。
```python
import threading
import time

def run(n):
    print("task", n)
    time.sleep(1)       #此时子线程停1s
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')

if __name__ == '__main__':
    t = threading.Thread(target=run, args=("t1",))
    t.setDaemon(True)   #把子进程设置为守护线程，必须在start()之前设置
    t.start()
    t.join() # 设置主线程等待子线程结束
    print("end")
```

（5）多线程共享全局变量

线程是进程的执行单元，进程是系统分配资源的最小单位，所以在同一个进程中的多线程是共享资源的。
```python
import threading
import time

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num += 1
    print("in work1 g_num is : %d" % g_num)

def work2():
    global g_num
    print("in work2 g_num is : %d" % g_num)

if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t1.start()
    time.sleep(1)
    t2 = threading.Thread(target=work2)
    t2.start()
```

# 2、线程池

面向对象开发中，大家知道创建和销毁对象是很费时间的，因为创建一个对象要获取内存资源或者其它更多资源。无节制的创建和销毁线程是一种极大的浪费。那我们可不可以把执行完任务的线程不销毁而重复利用呢？仿佛就是把这些线程放进一个池子，一方面我们可以控制同时工作的线程数量，一方面也避免了创建和销毁产生的开销。

线程池在标准库中其实是有体现的，只是在官方文章中基本没有被提及：
```text
In : from multiprocessing.pool import ThreadPool
In : pool = ThreadPool(5)
In : pool.map(lambda x: x**2, range(5))
Out: [0, 1, 4, 9, 16]

```

当然我们也可以自己实现一个：
```python
# -*-coding=utf-8-*-
import time
import threading
from random import random
from Queue import Queue


def double(n):
    return n * 2


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()

    def run(self):
        while 1:
            f, args, kwargs = self._q.get()
            try:
                print('USE: {}'.format(self.name))  # 线程名字
                print(f(*args, **kwargs))
            except Exception as e:
                print(e)
            self._q.task_done()


class ThreadPool(object):
    def __init__(self, num_t=5):
        self._q = Queue(num_t)
        # Create Worker Thread
        for _ in range(num_t):
            Worker(self._q)

    def add_task(self, f, *args, **kwargs):
        self._q.put((f, args, kwargs))

    def wait_complete(self):
        self._q.join()


pool = ThreadPool()
for _ in range(8):
    wt = random()
    pool.add_task(double, wt)
    time.sleep(wt)
pool.wait_complete()
```

执行一下:
```text
USE: Thread-1
1.58762376489
USE: Thread-2
0.0652918738849
USE: Thread-3
0.997407997138
USE: Thread-4
1.69333900685
USE: Thread-5
0.726900613676
USE: Thread-1
1.69110052253
USE: Thread-2
1.89039743989
USE: Thread-3
0.96281118122
```

线程池会保证同时提供 5 个线程工作，但是我们有 8 个待完成的任务，可以看到线程按顺序被循环利用了

# 3、同步机制

（1）Semaphore（信号量）
在多线程编程中，为了防止不同的线程同时对一个公用的资源（比如全部变量）进行修改，需要进行同时访问的数量（通常是 1）。信号量同步基于内部计数器，每调用一次 acquire ()，计数器减 1；每调用一次 release ()，计数器加 1. 当计数器为 0 时，acquire () 调用被阻塞。

```python
import time
from random import random
from threading import Thread, Semaphore

sema = Semaphore(3)


def foo(tid):
    with sema:
        print('{} acquire sema'.format(tid))
        wt = random() * 2
        time.sleep(wt)
    print('{} release sema'.format(tid))


threads = []

for i in range(5):
    t = Thread(target=foo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

这个例子中，我们限制了同时能访问资源的数量为 3。看一下执行的效果：
```text
❯ python semaphore.py
0 acquire sema
1 acquire sema
2 acquire sema
2 release sema
3 acquire sema
1 release sema
4 acquire sema
0 release sema
3 release sema
4 release sema
```

（2）Lock（互斥锁）

Lock 也可以叫做互斥锁，其实相当于信号量为 1

我们先看一个不加锁的例子：
```python
import time
from threading import Thread

value = 0


def getlock():
    global value
    new = value + 1
    time.sleep(0.001)  # 使用sleep让线程有机会切换
    value = new


threads = []

for i in range(100):
    t = Thread(target=getlock)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(value)
```

执行一下：
```text
❯ python nolock.py
16
```

大写的黑人问号，不加锁的情况下，结果会远远的小于 100

加上互斥锁看看：
```python
import time
from threading import Thread, Lock

value = 0
lock = Lock()


def getlock():
    global value
    with lock:
        new = value + 1
        time.sleep(0.001)
        value = new

threads = []

for i in range(100):
    t = Thread(target=getlock)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(value)
```

写法还可以是用acquire()和release()
```python
from threading import Thread,Lock
import os,time
def work():
    global n
    lock.acquire()
    temp=n
    time.sleep(0.1)
    n=temp-1
    lock.release()
if __name__ == '__main__':
    lock=Lock()
    n=100
    l=[]
    for i in range(100):
        p=Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()
```

（3）RLock（递归锁）

RLcok类的用法和Lock类一模一样，但它支持嵌套，在多个锁没有释放的时候一般会使用RLcok类。

acquire () 能够不被阻塞的被同一个线程调用多次。但是要注意的是 release () 需要调用与 acquire () 相同的次数才能释放锁。

（4）Condition（条件）

一个线程等待特定条件，而另一个线程发出特定条件满足的信号。最好说明的例子就是「生产者 / 消费者」模型：
```python
import time
import threading


def consumer(cond):
    t = threading.currentThread()
    with cond:
        cond.wait()  # wait()方法创建了一个名为waiter的锁，并且设置锁的状态为locked。这个waiter锁用于线程间的通讯
        print('{}: Resource is available to consumer'.format(t.name))


def producer(cond):
    t = threading.currentThread()
    with cond:
        print('{}: Making resource available'.format(t.name))
        cond.notifyAll()  # 释放waiter锁，唤醒消费者


condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()
```

执行一下：
```text
❯ python condition.py
p: Making resource available
c2: Resource is available to consumer
c1: Resource is available to consumer

```
可以看到生产者发送通知之后，消费者都收到了。

（5）Event（事件）

一个线程发送 / 传递事件，另外的线程等待事件的触发。主要提供以下几个方法：
+ clear 将flag设置为“False”
+ set 将flag设置为“True”
+ is_set 判断是否设置了flag
+ wait 会一直监听flag，如果没有检测到flag就一直处于阻塞状态
+ 事件处理的机制：全局定义了一个“Flag”，当flag值为“False”，那么event.wait()就会阻塞，当flag值为“True”，那么event.wait()便不再阻塞。

我们同样的用「生产者 / 消费者」模型的例子:
```python
import time
import threading
from random import randint

TIMEOUT = 2


def consumer(event, l):
    t = threading.currentThread()
    while 1:
        event_is_set = event.wait(TIMEOUT)
        if event_is_set:
            try:
                integer = l.pop()
                print('{} popped from list by {}'.format(integer, t.name))
                event.clear()  # 重置事件状态
            except IndexError:  # 为了让刚启动时容错
                pass


def producer(event, l):
    t = threading.currentThread()
    while 1:
        integer = randint(10, 100)
        l.append(integer)
        print('{} appended to list by {}'.format(integer, t.name))
        event.set()  # 设置事件
        time.sleep(1)


event = threading.Event()
l = []

threads = []

for name in ('consumer1', 'consumer2'):
    t = threading.Thread(name=name, target=consumer, args=(event, l))
    t.start()
    threads.append(t)

p = threading.Thread(name='producer1', target=producer, args=(event, l))
p.start()
threads.append(p)

for t in threads:
    t.join()
```
执行的效果是这样的：
```text
77 appended to list by producer1
77 popped from list by consumer1
46 appended to list by producer1
46 popped from list by consumer2
43 appended to list by producer1
43 popped from list by consumer2
37 appended to list by producer1
37 popped from list by consumer2
33 appended to list by producer1
33 popped from list by consumer2
57 appended to list by producer1
57 popped from list by consumer1
```

可以看到事件被 2 个消费者比较平均的接收并处理了。如果使用了 wait 方法，线程就会等待我们设置事件，这也有助于保证任务的完成。

（6）Queue

队列在并发开发中最常用的。我们借助「生产者 / 消费者」模式来理解：生产者把生产的「消息」放入队列，消费者从这个队列中对去对应的消息执行。

如下 4 个方法：
+ put: 向队列中添加一个项。
+ get: 从队列中删除并返回一个项。
+ task_done: 当某一项任务完成时调用。
+ join: 阻塞直到所有的项目都被处理完。

```python
import time
import threading
from random import random
from Queue import Queue

q = Queue()


def double(n):
    return n * 2


def producer():
    while 1:
        wt = random()
        time.sleep(wt)
        q.put((double, wt))


def consumer():
    while 1:
        task, arg = q.get()
        print(arg, task(arg))
        q.task_done()


for target in (producer, consumer):
    t = threading.Thread(target=target)
    t.start()
```
这就是最简化的队列架构。

Queue 模块还自带了 PriorityQueue（带有优先级）和 LifoQueue（后进先出）2 种特殊队列。我们这里展示下线程安全的优先级队列的用法， PriorityQueue 要求我们 put 的数据的格式是(priority_number, data)，我们看看下面的例子：
```python
import time
import threading
from random import randint
from Queue import PriorityQueue

q = PriorityQueue()


def double(n):
    return n * 2


def producer():
    count = 0
    while 1:
        if count > 5:
            break
        pri = randint(0, 100)
        print('put :{}'.format(pri))
        q.put((pri, double, pri))  # (priority, func, args)
        count += 1


def consumer():
    while 1:
        if q.empty():
            break
        pri, task, arg = q.get()
        print('[PRI:{}] {} * 2 = {}'.format(pri, arg, task(arg)))
        q.task_done()
        time.sleep(0.1)


t = threading.Thread(target=producer)
t.start()
time.sleep(1)
t = threading.Thread(target=consumer)
t.start()
```

其中消费者是故意让它执行的比生产者慢很多，为了节省篇幅，只随机产生 5 次随机结果。我们看下执行的效果：
```text
❯ python priority_queue.py
put :84
put :86
put :16
put :93
put :14
put :93
[PRI:14] 14 * 2 = 28

[PRI:16] 16 * 2 = 32
[PRI:84] 84 * 2 = 168
[PRI:86] 86 * 2 = 172
[PRI:93] 93 * 2 = 186
[PRI:93] 93 * 2 = 186

```
可以看到 put 时的数字是随机的，但是 get 的时候先从优先级更高（数字小表示优先级高）开始获取的。