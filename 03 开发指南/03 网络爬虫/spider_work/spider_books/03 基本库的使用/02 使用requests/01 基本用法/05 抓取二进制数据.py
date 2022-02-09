import requests

resp = requests.get('https://github.com/favicon.ico')
# print(resp.text)
# print(resp.content)

# 将返回的响应的content保存下来即可
with open('favicon.ico', 'wb') as f:
    f.write(resp.content)

# text和content的区别？
