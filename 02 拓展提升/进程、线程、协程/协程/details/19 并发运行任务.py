# 并发运行任务的案例
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")  # python3.7新语法，了解一波
        await asyncio.sleep(1)  # await后面是 可等待对象
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

    return f"Task {name}: Finished!"


async def main():
    # Schedule three calls *concurrently*:
    results = await asyncio.gather(  # results包含所有任务的返回结果，是一个列表，按执行顺序返回结果
        factorial("A", 2),  # 协程，会自动调度为任务
        factorial("B", 3),
        factorial("C", 4),
    )
    print(results)


asyncio.run(main())  # 协程的嵌套，后面有详解
