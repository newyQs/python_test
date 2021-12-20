"""
函数名前面有async 关键字的函数

协程对象 执行协程函数得到的对象

# 协程函数
async def func():
    print(111)


# 协程对象
result = func()

协程对象的内部代码不会执行

如果要执行 需要交给事件循环来处理
"""
import asyncio


async def func():
    print(111)


result = func()

# loop = asyncio,get_event_loop()
# loop.run_until_complete(result)

# python3.7以后
asyncio.run(result)
