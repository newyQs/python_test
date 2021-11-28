import requests

data = {
    'name': 'jack',
    'age': 18
}
r = requests.get('http://httpbin.org/get', params=data)  # 附加参数
print(r.text)
print(type(r.text))  # <class 'str'>

print(r.json())
print(type(r.json()))  # <class 'dict'>

print(r.json)
