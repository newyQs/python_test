import asyncio


async def func(i):
    print('test1', i)
    await asyncio.sleep(1)
    print('test2', i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [func(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

"""
async def 用来定义异步函数，await 表示当前协程任务等待睡眠时间，允许其他任务运行。
然后获得一个事件循环，主线程调用asyncio.get_event_loop()时会创建事件循环，
你需要把异步的任务丢给这个循环的run_until_complete()方法，事件循环会安排协同程序的执行。
"""
