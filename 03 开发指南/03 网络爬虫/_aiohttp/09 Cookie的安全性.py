"""
默认ClientSession使用的是严格模式的 aiohttp.CookieJar. RFC 2109，明确的禁止接受url和ip地址产生的cookie，只能接受 DNS 解析IP产生的cookie。

可以通过设置aiohttp.CookieJar 的 unsafe=True 来配置
"""


jar = aiohttp.CookieJar(unsafe=True)
session = aiohttp.ClientSession(cookie_jar=jar)