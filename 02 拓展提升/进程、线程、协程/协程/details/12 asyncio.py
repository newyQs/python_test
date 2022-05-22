import asyncio, time


async def work(x):
    for _ in range(3):
        print("Work {} is running ..".format(x))
        await asyncio.sleep(1)  # 当执行某个协程时，在任务阻塞的时候用await挂起
    return "Work {} is finished!".format(x)


async def main_work():
    coroutine_1 = work(1)
    coroutine_2 = work(2)
    coroutine_3 = work(3)

    tasks = [
        asyncio.ensure_future(coroutine_1),
        asyncio.ensure_future(coroutine_2),
        asyncio.ensure_future(coroutine_3),
    ]

    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print("The task's result is : {}".format(task.result()))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_work())
