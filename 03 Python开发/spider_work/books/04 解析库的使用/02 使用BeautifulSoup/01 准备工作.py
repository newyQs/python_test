"""
1. 节点选择器
2. 方法选择器
3. CSS选择器
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')

print(soup.p.string)
