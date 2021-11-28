from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=67', 'comment']

print(urlunparse(data))
