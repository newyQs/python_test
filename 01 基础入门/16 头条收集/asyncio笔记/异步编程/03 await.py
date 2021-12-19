"""
await+可等待对象（协程对象，Future,Task对象-》IO等待）

await 就是等待对象的值得到结果之后再继续向下走
"""
import asyncio


async def func():
    print("xxx")
    response = await asyncio.sleep(2)
    print("结束", response)


asyncio.run(func())
