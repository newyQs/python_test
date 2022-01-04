"""

"""
import http.cookiejar
import urllib.request

filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)    # 保存格式1
cookie = http.cookiejar.LWPCookieJar(filename)  # 保存格式2
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)
