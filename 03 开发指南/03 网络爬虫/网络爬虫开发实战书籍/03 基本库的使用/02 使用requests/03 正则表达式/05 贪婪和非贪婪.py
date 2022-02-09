import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)

print(result)
print(result.group(1))
# 贪婪匹配是尽可能匹配多的字符，非贪婪匹配是尽可能匹配少的字符
# .*代表贪婪匹配，.*?代表非贪婪匹配
# 建议在做匹配时，字符串中间尽量使用非贪婪匹配，就是使用.*?来代替.*
# 避免出现匹配结果缺失的情况

content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)

print(result1.group(1))
print(result2.group(1))
# 特别注意：如果匹配的结果在字符串结尾，.*?就有可能匹配不到任何内容，因为它会尽可能匹配可能少的字符。
