"""

"""
import requests
from pyquery import PyQuery

doc = PyQuery(url='http://cuiqingcai.com')
print(doc('title'))

# 类似于下面
doc = PyQuery(requests.get('http://cuiqingcai.com').text)
print(doc('title'))
