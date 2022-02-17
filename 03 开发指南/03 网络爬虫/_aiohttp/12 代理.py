"""

"""
import aiohttp

# 使用无授权代理

async with aiohttp.ClientSession() as session:
    async with session.get("http://python.org", proxy="http://proxy.com") as resp:
        print(resp.status)

# 代理授权的两种方式
# 第一种
async with aiohttp.ClientSession() as session:
    proxy_auth = aiohttp.BasicAuth('user', 'pass')
    async with session.get("http://python.org", proxy="http://proxy.com", proxy_auth=proxy_auth) as resp:
        print(resp.status)

# 第二种
session.get("http://python.org", proxy="http://user:pass@some.proxy.com")
