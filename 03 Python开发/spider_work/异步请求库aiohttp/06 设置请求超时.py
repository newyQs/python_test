"""
ClientTimeout类有四个类属性:

total:整个操作时间包括连接建立，请求发送和响应读取。
connect:该时间包括建立新连接或在超过池连接限制时等待池中的空闲连接的连接。
sock_connect:连接到对等点以进行新连接的超时，不是从池中给出的。
sock_read:从对等体读取新数据部分之间的时间段内允许的最大超时。
"""
import aiohttp
import asyncio

timeout = aiohttp.ClientTimeout(total=60)


async def main():
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())


if __name__ == "__main__":
    asyncio.run(main())
