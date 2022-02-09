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


/ 和 // 的区别，其中 / 用于获取直接子节点，// 用于获取子孙节点
"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//ul//a')  # 获取 ul 节点下的所有子孙 a 节点
# result = html.xpath('//ul/a') # 获取不到ul下没有直接子节点a

print(result)
