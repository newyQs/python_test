"""

"""
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())

# 选取 class 为 item-1 的 li 节点
result = html.xpath('//li[@class="item-0"]')

print(result)
