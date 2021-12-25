"""
Request(url, data=None, headers={},origin_req_host=None, unverifiable=False,method=None)
url:
data:附加数据。必须是byte(字节)类型
header:是一个字典，就是请求头。
origin_req_host:指的是请求方的host名称或者IP地址
unverifiable:
method:请求方法。如GET,POST,PUT等
"""
from urllib import request

req = request.Request('http://python.org')
resp = request.urlopen(request)
print(resp.read().decode('utf-8'))

print(type(request))  # <class 'urllib.request.Request'>
