import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^(Hello)\s(\d+)\s(World)', content)

print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))
print(result.span())

# 使用()将想要提取的子字符串括起来。()实际上标记了一个子表达式的开始和结束位置，被标记的每个子表达式会一次对应每一个分组
# 调用group()方法传入分组的索引即可获取提取的结果
