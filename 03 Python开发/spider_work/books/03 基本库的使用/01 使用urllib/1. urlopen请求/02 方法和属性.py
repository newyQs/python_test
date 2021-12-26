"""
urlopen(
    url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, *, cafile=None, capath=None, cadefault=False, context=None
)
"""
from urllib import request

resp = request.urlopen('https://www.python.org')

print(type(resp))  # <class 'http.client.HTTPResponse'>

# print(resp.status)
# print(resp.getheaders())
# print(resp.getheader('Server'))

print(dir(resp))
