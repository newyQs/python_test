"""

"""
from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dic = {
    'name': 'jack'
}

data = bytes(parse.urlencode(dic), encoding='utf8')

req = request.Request(url=url, data=data, headers=headers, method='POST')
resp = request.urlopen(req)
# headers也可通过add_header()方法来添加:req.add_header()

print(resp.read().decode('utf-8'))
