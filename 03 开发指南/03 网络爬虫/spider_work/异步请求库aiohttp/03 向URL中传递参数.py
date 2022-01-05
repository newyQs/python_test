"""

"""
import asyncio
import aiohttp


async def main():
    """以下三种方式均可以"""
    params = {'key1': 'value1', 'key2': 'value2'}
    params = [('key', 'value1'), ('key', 'value2')]
    params = 'key=value+1'

    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get', params=params) as resp:
            print(resp.status)
            print(await resp.text())


if __name__ == '__main__':
    asyncio.run(main())
