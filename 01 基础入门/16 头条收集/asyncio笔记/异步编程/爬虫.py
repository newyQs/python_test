"""

"""
import aiohttp
import asyncio


async def fetch(session, url):
    print("发送请求:", url)
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text()
        print("得到结果:", url, len(text))
        return text


async def main():
    async with aiohttp.clientsession() as session:
        url_list = [
            "http://python.orgh",
            "https://www.baidu.com",
            "https://www/pythonav.com"
        ]
    tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]

    done.pending = await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
