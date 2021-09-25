import urllib.request
import socket
import urllib.error

# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read().decode('utf-8'))

'''
这里设置超时时间为0.1s，如果程序运行0.1s过后，服务器依然没有响应，就会抛出URLError异常。
该异常属于urllib.error模块，错误原因是超时。

因此可以通过设置这个超时时间也控制一个网页在长时间未响应时，就跳过它的抓取。
'''

# 这样实现：
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
