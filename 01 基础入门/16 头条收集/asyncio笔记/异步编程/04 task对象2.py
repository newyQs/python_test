"""

"""
import asyncio


async def func():
    print(111)
    await asyncio.sleep(2)
    print(222)


async def main():
    print("main开始")
    # 创建task任务 并将task 任务添加到事件循环
    task1 = asyncio.create_task(func(), name="task1")
    task2 = asyncio.create_task(func(), name="task2")
    task_list = [task1, task2]
    # 返回值都放在done集合中，pending 执行过程中部分返回值放在pending中
    done, pending = await asyncio.wait(task_list)
    print(done)


asyncio.run(main())
