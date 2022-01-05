"""

"""
from pyquery import PyQuery

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = PyQuery(html)
items = doc('.list')
print(type(items))
print(items)

lis = items.find('li')
print(type(lis))
print(lis)

# find() 的查找范围是节点的所有子孙节点，而如果我们只想查找子节点，那么可以用 children() 方法
lis = items.children()
print(type(lis))
print(lis)

# 如果要筛选所有子节点中符合条件的节点，比如想筛选出子节点中 class 为 active 的节点，可以向 children() 方法传入 CSS 选择器.active：
lis = items.children('.active')
print(lis)
