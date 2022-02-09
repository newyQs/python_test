"""
https://zhuanlan.zhihu.com/p/130983521

官方推荐使用一个客户端会话来发起所有请求，会话中记录了请求的cookie，但你还可以使用aiohttp.request来发送请求。

当我们使用 async def 就是定义了一个异步函数，异步逻辑由asyncio提供支持。

async with aiohttp.ClientSession() as session 为异步上下文管理器，在请求结束时或者发生异常请求时支持自动关闭实例化的客户端会话。
"""
import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())

aiohttp.request()

if __name__ == '__main__':
    # python3.7才支持这种写法，作为一个入口函数，以debug模式运行事件循环
    asyncio.run(main(), debug=True)

    # python3.6及以下版本写法
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(main()))
    loop.close()
