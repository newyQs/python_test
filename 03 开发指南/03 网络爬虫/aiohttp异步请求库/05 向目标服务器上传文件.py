"""

"""
import asyncio
import aiohttp


async def main():
    """传递文件"""
    files = {'file': open('report.xls', 'rb')}
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=files) as resp:
            print(resp.status)
            print(await resp.text())


async def main2():
    """实例化FormData可以指定filename和content_type"""
    data = aiohttp.FormData()
    data.add_field('file',
                   open('report.xls', 'rb'),
                   filename='report.xls',
                   content_type='application/vnd.ms-excel')
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=data) as resp:
            print(resp.status)
            print(await resp.text())


async def main3():
    """流式上传文件"""
    async with aiohttp.ClientSession() as session:
        with open('report.xls', 'rb') as f:
            async with session.post('http://httpbin.org/post', data=f) as resp:
                print(resp.status)
                print(await resp.text())


async def main4():
    """因为content属性是 StreamReader（提供异步迭代器协议），所以您可以将get和post请求链接在一起。python3.6及以上才能使用"""
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as resp:
            async with session.post('http://httpbin.org/post', data=resp.content) as r:
                print(r.status)
                print(await r.text())


if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(main2())
    asyncio.run(main3())
    asyncio.run(main4())
