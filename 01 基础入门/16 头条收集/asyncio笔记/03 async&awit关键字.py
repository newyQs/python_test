"""
python3.5版本后才可以使用
"""
import asyncio


async def func1():
    print(1)
    # 网络IO请求 下载一张图片
    await asyncio.sleep(2)  # 遇到类似IO耗时操作 自动切换到task中的其他任务
    print(2)


async def func2():
    print(33)
    # 网络IO请求 下载一张图片
    await asyncio.sleep(2)  # 遇到IO耗时操作,自动化切换到task中的其他操作
    print(444)


if __name__ == '__main__':
    tasks = [
        asyncio.ensure_future(func1()),
        asyncio.ensure_future(func2())
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
