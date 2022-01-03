import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))

# re.match(pattern, string, flags=0)
# 从字符串的起始位置匹配正则表达式，如果匹配就返回匹配成功的字符串，否则返回None
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
print(result)  # <re.Match object; span=(0, 25), match='Hello 123 4567 World_This'>
print(result.group())  # Hello 123 4567 World_This
print(result.span())  # (0, 25)
