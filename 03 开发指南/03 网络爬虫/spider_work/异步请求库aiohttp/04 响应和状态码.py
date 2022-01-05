"""
resp.history 查看重定向历史
resp.headers 获取响应头
resp.cookies 获取响应cookie
resp.status 获取响应状态码
resp.text(encoding='utf-8) 获取响应文本
resp.json() 获取json响应数据
resp.read() 获取二进制响应数据
resp.content.read(100) 获取流响应，每次获取100个字节

"""
import asyncio
import aiohttp


async def main():
    params = {'key1': 'value1', 'key2': 'value2'}
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get', params=params) as resp:
            print(resp.status)  # 状态码
            print(await resp.text(encoding='utf-8'))  # 文本响应，可以设置响应编码，默认是utf-8
            print(await resp.json())  # json响应
            print(await resp.read())  # 二进制响应，适用于下载图片等


async def main2():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/events') as resp:
            print(resp.status)  # 状态码
            print(await resp.content.read(100))  # 流响应，适用于大文件，分次读取

            # await生成一个迭代器，通过不断循环拿到每一次100个字节码
            while True:
                chunk = await resp.content.read(100)
                print(chunk)
                if not chunk:
                    break


if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(main2())
