"""

"""
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p class="story">
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
"""

soup = BeautifulSoup(html, 'lxml')

print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))
