import requests

r = requests.get('http://www.baidu.com')

print(type(r))  # <class 'requests.model.Response'>
print(r.status_code)  # 200
print(type(r.text))  # <class 'str'>
print(r.text)
print(r.cookies)
