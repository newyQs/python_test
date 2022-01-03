"""
/ 和 // 的区别，其中 / 用于获取直接子节点，// 用于获取子孙节点
"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')  # 选择 li 节点的所有直接 a 子节点

print(result)
