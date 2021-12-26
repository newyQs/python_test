import requests

resp = requests.get('https://www.baidu.com')
print(resp.cookies)

for key, value in resp.cookies.items():
    print(key + '=' + value)
