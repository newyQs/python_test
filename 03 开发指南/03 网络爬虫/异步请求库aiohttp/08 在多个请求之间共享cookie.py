"""

"""
import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        await session.get('http://httpbin.org/cookies/set?my_cookie=my_value')
        filtered = session.cookie_jar.filter_cookies('http://httpbin.org')
        print(filtered)
        assert filtered['my_cookie'].value == 'my_value'
        async with session.get('http://httpbin.org/cookies') as r:
            json_body = await r.json()
            print(json_body)
            assert json_body['cookies']['my_cookie'] == 'my_value'


if __name__ == "__main__":
    asyncio.run(main())
