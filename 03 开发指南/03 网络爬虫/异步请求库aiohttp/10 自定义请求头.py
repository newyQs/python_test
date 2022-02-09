"""

"""
import aiohttp

async with aiohttp.ClientSession(headers={'User-Agent': 'your agent'}) as session:
    async with session.get('http://httpbin.org/headers') as resp:
        print(resp.status)
        print(await resp.text())
