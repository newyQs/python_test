import urllib.request

'''
urlopen(url,data,timeout,cafile,capath,cadefault,context)
urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            *, cafile=None, capath=None, cadefault=False, context=None)
            
url:
data:附加数据
timeout：超时时间
cafile和capath分别指定CA证书和它的路径
context必须是ssl.SSLContext类型，用来指定SSL设置。
caswfault现在已经弃用了，默认值为False
'''

response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))  # <class 'http.client.HTTPResponse'>
'''
返回一个HTTPResponse类型的对象，主要包含read(),readinto(),getheader(name),getheaders(),fileno()等方法
以及msg,version,status,reason,debuglevel,closed等属性。
'''

