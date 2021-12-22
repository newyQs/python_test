# python异步编程之asyncio（百万并发）
前言：python由于GIL（全局锁）的存在，不能发挥多核的优势，其性能一直饱受诟病。
然而在IO密集型的网络编程里，异步处理比同步处理能提升成百上千倍的效率，弥补了python性能方面的短板，
如最新的微服务框架japronto，resquests per second可达百万级。

python还有一个优势是库（第三方库）极为丰富，运用十分方便。
asyncio是python3.4版本引入到标准库，python2x没有加这个库，毕竟python3x才是未来啊，哈哈！python3.5又加入了async/await特性。

 
在学习asyncio之前，我们先来理清楚同步/异步的概念：
+ 同步是指完成事务的逻辑，先执行第一个事务，如果阻塞了，会一直等待，直到这个事务完成，再执行第二个事务，顺序执行。。。
+ 异步是和同步相对的，异步是指在处理调用这个事务的之后，不会等待这个事务的处理结果，直接处理第二个事务去了，通过状态、通知、回调来通知调用者处理结果。
## 1. asyncio
使用sleep(1)模拟耗时1秒的io操作

同步代码：
```
import time

def hello():
    time.sleep(1)

def run():
    for i in range(5):
        hello()
        print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！
if __name__ == '__main__':
    run()
```
异步代码：
```
import time
import asyncio

# 定义异步函数
async def hello():
    await asyncio.sleep(1)
    print('Hello World:%s' % time.time())

if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    tasks = [hello() for i in range(5)]
    loop.run_until_complete(asyncio.wait(tasks))
```
async def 用来定义异步函数，await 表示当前协程任务等待睡眠时间，允许其他任务运行。
然后获得一个事件循环，主线程调用asyncio.get_event_loop()时会创建事件循环，
你需要把异步的任务丢给这个循环的run_until_complete()方法，事件循环会安排协同程序的执行。

## 2. aiohttp
如果需要并发http请求怎么办呢，通常是用requests，但requests是同步的库，如果想异步的话需要引入aiohttp。
这里引入一个类，from aiohttp import ClientSession，首先要建立一个session对象，然后用session对象去打开网页。
session可以进行多项操作，比如post, get, put, head等。

基本用法：
```
async with ClientSession() as session:
    async with session.get(url) as response:
```

aiohttp异步实现的例子：
```
import asyncio
from aiohttp import ClientSession


tasks = []
url = "https://www.baidu.com/{}"
async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))
```
首先async def 关键字定义了这是个异步函数，await 关键字加在需要等待的操作前面，
response.read()等待request响应，是个耗IO操作。然后使用ClientSession类发起http请求。

### 多链接异步访问
如果我们需要请求多个URL该怎么办呢，同步的做法访问多个URL只需要加个for循环就可以了。
但异步的实现方式并没那么容易，在之前的基础上需要将hello()包装在asyncio的Future对象中，然后将Future对象列表作为任务传递给事件循环。
```
import time
import asyncio
from aiohttp import ClientSession

tasks = []
url = "https://www.baidu.com/{}"
async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
#            print(response)
            print('Hello World:%s' % time.time())

def run():
    for i in range(5):
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))
```
### 收集http响应
好了，上面介绍了访问不同链接的异步实现方式，但是我们只是发出了请求，如果要把响应一一收集到一个列表中，
最后保存到本地或者打印出来要怎么实现呢，可通过asyncio.gather(*tasks)将响应全部收集起来，具体通过下面实例来演示。
```
import time
import asyncio
from aiohttp import ClientSession

tasks = []
url = "https://www.baidu.com/{}"
async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            print('Hello World:%s' % time.time())
            return await response.read()

def run():
    for i in range(5):
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))
    print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
```

### 异常解决
假如你的并发达到2000个，程序会报错：ValueError: too many file descriptors in select()。
报错的原因字面上看是 Python 调取的 select 对打开的文件有最大数量的限制，这个其实是操作系统的限制，
linux打开文件的最大数默认是1024，windows默认是509，超过了这个值，程序就开始报错。这里我们有三种方法解决这个问题：
1. 限制并发数量。（一次不要塞那么多任务，或者限制最大并发数量）
2. 使用回调的方式。
3. 修改操作系统打开文件数的最大限制，在系统里有个配置文件可以修改默认值，具体步骤不再说明了。
不修改系统默认配置的话，个人推荐限制并发数的方法，设置并发数为500，处理速度更快。
```
import time,asyncio,aiohttp


url = 'https://www.baidu.com/'
async def hello(url,semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.read()


async def run():
    semaphore = asyncio.Semaphore(500) # 限制并发量为500
    to_get = [hello(url.format(),semaphore) for _ in range(1000)] #总共1000任务
    await asyncio.wait(to_get)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
```