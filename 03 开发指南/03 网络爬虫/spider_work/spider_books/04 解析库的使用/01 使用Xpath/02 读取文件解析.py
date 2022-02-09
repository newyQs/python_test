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

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
<html>
<body>
<div>&#13;
    <ul>&#13;
        <li class="item-0"><a href="link1.html">first item</a></li>&#13;
        <li class="item-1"><a href="link2.html">second item</a></li>&#13;
        <li class="item-inactive"><a href="link3.html">third item</a></li>&#13;
        <li class="item-1"><a href="link4.html">fourth item</a></li>&#13;
        <li class="item-0"><a href="link5.html">fifth item</a>&#13;
        </li>
    </ul>&#13;
</div>
</body>
</html>
"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
