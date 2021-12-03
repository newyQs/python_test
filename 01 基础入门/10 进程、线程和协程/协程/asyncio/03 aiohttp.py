"""
如果需要并发http请求怎么办呢，通常是用requests，但requests是同步的库，如果想异步的话需要引入aiohttp。
这里引入一个类，from aiohttp import ClientSession，首先要建立一个session对象，然后用session对象去打开网页。
session可以进行多项操作，比如post, get, put, head等。
"""
import asyncio
from aiohttp import ClientSession

tasks = []
url = "https://www.baidu.com/{}"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))
