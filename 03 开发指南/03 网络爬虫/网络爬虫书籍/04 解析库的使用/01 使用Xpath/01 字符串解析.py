# Xpath常用规则
"""
nodename    选取此节点的所有节点
/           从当前节点，选取直接子节点
//          从当前节点，选取子孙节点
.           选取当前节点
..          选取当前节点的父节点
@           选取属性
https://cuiqingcai.com/5545.html
"""
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''
html = etree.HTML(text)  # <class 'lxml.etree._Element'>
result = etree.tostring(html)  # <class 'bytes'>
print(result.decode('utf-8'))  # <class 'str'>
