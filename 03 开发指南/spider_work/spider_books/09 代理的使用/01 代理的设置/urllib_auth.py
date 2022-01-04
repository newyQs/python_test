from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 如果遇到需要认证的代理，可以这样设置：其中 username 就是用户名，password 为密码
proxy = 'username:password@127.0.0.1:9743'

proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
