"""

"""
import aiohttp
import asyncio

cookies = {'cookies_are': 'working'}


async def main():
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.get('http://httpbin.org/cookies') as resp:
            print(resp.status)
            print(await resp.text())
            assert await resp.json() == {"cookies": {"cookies_are": "working"}}


if __name__ == "__main__":
    asyncio.run(main())
