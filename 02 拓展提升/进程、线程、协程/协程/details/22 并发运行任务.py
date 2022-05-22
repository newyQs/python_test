# 使用事件循环和asyncio.wait、asyncio.gather实现并发运行任务
import asyncio, time


async def work_1(x):
    print(f"Starting {x}")
    time.sleep(1)
    print(f"Starting {x}")
    for _ in range(3):
        print(f"Work {x} is running ..")
        await asyncio.sleep(2)  # 耗时操作，此时挂起该协程，执行其他协程
    return f"Work {x} is finished"


async def work_2(x):
    print(f"Starting {x}")
    for _ in range(3):
        await asyncio.sleep(1)  # 耗时操作，此时挂起该协程，执行其他协程
        print(f"Work {x} is running ..")
    return f"Work {x} is finished"


coroutine_1 = work_1(1)
coroutine_2 = work_2(2)

loop = asyncio.get_event_loop()  # 创建一个事件循环

# 方式一，asyncio.wait(tasks)接受一个task列表  执行的顺序与列表里的任务顺序有关
tasks = [
    asyncio.ensure_future(coroutine_1),
    asyncio.ensure_future(coroutine_2),
]
# 注册到事件循环中，并执行
dones, pendings = loop.run_until_complete(
    asyncio.wait(tasks))  # loop.run_until_complete(asyncio.wait(tasks))的作用相当于：await asyncio.wait(tasks)
for task in dones:
    print(task.result())

# 方式二，使用asyncio.gather(*tasks)，接受一堆tasks，tasks也可以是一个列表，使用*解包
# task_1 = asyncio.ensure_future(coroutine_1)
# task_2 = asyncio.ensure_future(coroutine_2)
# task_result_list = loop.run_until_complete(asyncio.gather(task_1, task_2))  # 返回一个列表，里面包含所有task的result()的结果
# print(task_result_list)
