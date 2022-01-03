import requests

data = {
    'name': 'jack',
    'age': 18
}
resp = requests.get('http://httpbin.org/get', params=data)  # 附加参数
# print(resp.text)
# print(type(resp.text))  # <class 'str'>
#
# print(resp.json())
# print(type(resp.json()))  # <class 'dict'>
#
# print(resp.json)
import pdb
pdb.set_trace()