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

如果要想获取子孙节点内部的所有文本，可以直接用 // 加 text() 的方式，这样可以保证获取到最全面的文本信息，但是可能会夹杂一些换行符等特殊字符。
如果想获取某些特定子孙节点下的所有文本，可以先选取到特定的子孙节点，然后再调用 text() 方法获取其内部文本，这样可以保证获取的结果是整洁的。
"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')  # 这种不行
# result = html.xpath('//li[@class="item-0"]/a/text()')
result = html.xpath('//li[@class="item-0"]//text()')

print(result)
