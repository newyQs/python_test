"""
<html>
<body>
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
</body>
</html>
"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有 li 节点下所有 a 节点的 href 属性
result = html.xpath('//li/a/@href')

print(result)
