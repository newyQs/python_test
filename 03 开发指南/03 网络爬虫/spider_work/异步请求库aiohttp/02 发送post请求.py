"""
put: session.put('http://httpbin.org/put', data=b'data')
delete: session.delete('http://httpbin.org/delete')
head: session.head('http://httpbin.org/get')
options: session.options('http://httpbin.org/get')
patch: session.patch('http://httpbin.org/patch', data=b'data')

"""
import asyncio
import aiohttp


async def main():
    data = b'\x00Binary-data\x00'  # 未经编码的数据通过bytes数据上传
    data = 'text'  # 传递文本数据
    data = {'key': 'value'}  # 传递form表单

    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=data) as resp:
            print(resp.status)
            print(await resp.text())


# 复杂的post请求
async def main2():
    pyload = {'key': 'value'}  # 传递pyload
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', json=pyload) as resp:
            print(resp.status)
            print(await resp.text())


if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(main2())
