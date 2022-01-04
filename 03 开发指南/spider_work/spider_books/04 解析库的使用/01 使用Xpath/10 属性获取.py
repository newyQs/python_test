"""

"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有 li 节点下所有 a 节点的 href 属性
result = html.xpath('//li/a/@href')

print(result)
