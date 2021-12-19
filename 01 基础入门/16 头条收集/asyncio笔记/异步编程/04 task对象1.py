"""
Task对象:在事件循环中添加多个任务的

tasks用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象，
这样可以让协程加入时间循环中等待被调度执行，
除了使用asyncio.create_task()函数意外，还可以使用低层级的loop.create_task()或者ensure_future()函数，不建议手动实例化Task对象，
注意:asyncio.create_task()在python3.7中被加入，在python3.7以前，可以改用低层级的asyncio.ensure_future()函数
"""
import asyncio


async def func():
    print(111)
    await asyncio.sleep(2)
    print(222)


async def main():
    print("main开始")
    # 创建task任务 并将task 任务添加到事件循环
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())

    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)


asyncio.run(main())
