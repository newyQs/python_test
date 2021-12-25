import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
result = re.match('Hello.*?(\d+).*?Demo', content)

# re.search(pattern, string, flags=0)
result2 = re.search('Hello.*?(\d+).*?Demo', content)

print(result)
print(result2)

# re.match()和re.search()的区别：
# match方法是从字符串的开头进行匹配，一旦开头匹配不成功就会返回None
# search方法在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果，找不到返回None
