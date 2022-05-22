import asyncio


async def nested1():
    print("nested1")
    await asyncio.sleep(0.5)
    print("nested1 is finished!")
    return 1


async def nested2():
    print("nested2")
    await asyncio.sleep(0.5)
    print("nested2 is finished!")
    return 2


async def nested3():
    print("nested3")
    await asyncio.sleep(0.5)
    print("nested3 is finished!")
    return 3


async def nested4():
    print("nested4")
    await asyncio.sleep(0.5)
    print("nested4 is finished!")
    return 4


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    print("main")

    task1 = asyncio.create_task(nested1())  # 使用asyncio.create_task将函数打包成一个任务，该协程将自动排入日程等待运行
    task2 = asyncio.create_task(nested2())
    task3 = asyncio.create_task(nested3())
    task4 = asyncio.create_task(nested4())

    await asyncio.sleep(1)  # 在main这个协程中，碰到耗时操作，则挂起任务，执行其他任务，即：task1 or task2 or task3 or task4

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task1)  # 等待 task1 如果task1中存在耗时操作，则挂起
    print(await task2)
    print(await task3)
    print(await task4)


asyncio.run(main())  # 并发运行这个5个协程，运行最高层级的入口点main函数
