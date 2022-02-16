"""
'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history',
'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok',
'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url'
"""
import requests

r = requests.get('http://www.baidu.com')

print(r.raise_for_status())

# print(type(r))  # <class 'requests.model.Response'>
# print(r.status_code)  # 200
# print(type(r.text))  # <class 'str'>
# print(r.text)
# print(r.cookies)

# print(dir(r))
"""
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', 
'__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 
'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links',
'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
"""

# print("apparent_encoding:", r.apparent_encoding)
# print("close:", r.close)
# print("connection:", r.connection)
# print("content:", r.content)
# print("cookies:", r.cookies)
# print("elapsed:", r.elapsed)
# print("encoding:", r.encoding)
# print("headers:", r.headers)
# print("history:", r.history)
# print("is_permanent_redirect:", r.is_permanent_redirect)
# print("is_redirect:", r.is_redirect)
# print("iter_content:", r.iter_content)
# print("iter_lines:", r.iter_lines)
# print("json:", r.json)
# print("links:", r.links)
# print("next:", r.next)
# print("ok:", r.ok)
# print("raise_for_status:", r.raise_for_status)
# print("raw:", r.raw)
# print("reason:", r.reason)
# print("request:", r.request)
# print("status_code:", r.status_code)
# print("text:", r.text)
# print("url:", r.url)
