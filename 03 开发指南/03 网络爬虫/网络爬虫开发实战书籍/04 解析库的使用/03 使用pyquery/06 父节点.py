"""

"""
from pyquery import PyQuery

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

doc = PyQuery(html)
items = doc('.list')

# 我们可以用 parent() 方法来获取某个节点的父节点
container = items.parent()
print(type(container))
print(container)

# 如果想获取某个祖先节点，该怎么办呢？这时可以用 parents() 方法
parents = items.parents()
print(type(parents))
print(parents)

# 如果想要筛选某个祖先节点的话，可以向 parents() 方法传入 CSS 选择器，这样就会返回祖先节点中符合 CSS 选择器的节点：
parent = items.parents('.wrap')
print(parent)
