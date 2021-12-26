import requests

resp = requests.get('http://www.janshu.com')

print(type(resp.status_code), resp.status_code)
print(type(resp.headers), resp.headers)
print(type(resp.cookies), resp.cookies)
