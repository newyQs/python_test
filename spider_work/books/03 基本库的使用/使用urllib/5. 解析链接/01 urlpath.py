from urllib.parse import urlparse

'''
urlparse(url, scheme='', allow_fragments=True)
url:
scheme:默认的协议
allow_fragments：是否忽略fragments。默认True,表示不忽略
'''
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result))  # <class 'urllib.parse.ParseResult'>
print(result)

# scheme://netloc/path;params?query#fragment
