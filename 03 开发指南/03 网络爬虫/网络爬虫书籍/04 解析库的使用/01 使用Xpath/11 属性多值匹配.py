"""

"""
from lxml import etree

# 这里html文本种li节点的class属性有两个值，li 和 li-first
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()') # 获取不到

# 这样获取
result = html.xpath('//li[contains(@class, "li")]/a/text()')

print(result)
