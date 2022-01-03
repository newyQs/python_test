import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)

print(result)
print(result.group())
print(result.span())

# 注：.可以匹配任意字符（除换行符）,*可以匹配前面的字符无限次
# 因此组合在一起就是：.*  可以匹配任意数量的的字符了
