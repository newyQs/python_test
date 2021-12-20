"""

"""
import asyncio


class Reader(object):
    """自定义异步迭代器（同是也是异步可迭代对象）"""

    def __init__(self):
        self.count = 0

    async def readline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__self(self):
        return self


async def __anext__(self):
    val = await self.readline()
    if val is None:
        raise StopAsyncIteration
    return val


async def func():
    obj = Reader()
    # async for 循环只能在异步函数中使用
    async for item in obj:
        print(item)


asyncio.run(func())
