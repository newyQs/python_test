"""

"""
import re
from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(text=re.compile('link')))
