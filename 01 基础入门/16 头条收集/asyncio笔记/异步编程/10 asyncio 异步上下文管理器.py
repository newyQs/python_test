"""
通过定义__aenter__和__aexit__方法来对async with语句中的环境进行控制
"""
import asyncio


class AsyncContextManager:
    def __init__(self, conn):
        self.conn = conn

    async def do_sth(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步连接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库
        await asyncio.sleep(1)


if __name__ == '__main__':
    async def fun():
        async with AsyncContextManager() as f:
            result = await f.do_sth()
            print(result)


    asyncio.run(fun())
