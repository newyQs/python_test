from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '127.0.0.1:9743'

proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
opener = build_opener(proxy_handler)
try:
    resp = opener.open('http://httpbin.org/get')
    print(resp.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

# 结果如下：
"""
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.6"
  }, 
  "origin": "106.185.45.153", 
  "url": "http://httpbin.org/get"
}
"""