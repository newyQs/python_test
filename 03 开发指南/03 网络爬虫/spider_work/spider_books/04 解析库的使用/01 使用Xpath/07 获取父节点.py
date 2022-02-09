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

# 首先选中 href 属性为 link4.html 的 a 节点，然后再获取其父节点，然后再获取其 class 属性
result = html.xpath('//a[@href="link4.html"]/../@class')
# 也可以通过 parent:: 来获取父节点
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')

print(result)
