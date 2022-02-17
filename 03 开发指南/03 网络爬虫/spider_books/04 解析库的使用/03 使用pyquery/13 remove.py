"""

"""
from pyquery import PyQuery

html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''

doc = PyQuery(html)
wrap = doc('.wrap')
print(wrap.text())
