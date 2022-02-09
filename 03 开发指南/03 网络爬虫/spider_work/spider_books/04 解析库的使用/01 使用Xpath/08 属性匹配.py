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

# 选取 class 为 item-1 的 li 节点
result = html.xpath('//li[@class="item-0"]')

print(result)
