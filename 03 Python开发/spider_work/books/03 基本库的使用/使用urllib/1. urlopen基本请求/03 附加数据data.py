import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'name': 'jack'}), encoding='utf8')

response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

'''
传递了一个参数name=jack。它需要转码成bytes(字节流)类型。其中转字节流使用bytes()方法，
第一个参数需要str(字符串)类型，需要使用urllib.parse模块里的urlencode()方法将参数字典转换为字符串，
第二个参数指定编码格式。

'''