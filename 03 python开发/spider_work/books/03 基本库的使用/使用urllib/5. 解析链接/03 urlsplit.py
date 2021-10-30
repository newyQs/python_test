from urllib.parse import urlsplit,urlparse

result1 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result1)

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(result)