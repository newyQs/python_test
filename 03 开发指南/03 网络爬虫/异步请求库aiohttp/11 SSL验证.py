"""
默认情况下，aiohttp对HTTPS协议使用严格检查，如果你不想上传SSL证书，可将ssl设置为False。
"""
import aiohttp

r = await session.get('https://example.com', ssl=False)
