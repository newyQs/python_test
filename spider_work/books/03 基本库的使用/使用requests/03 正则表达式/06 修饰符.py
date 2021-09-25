import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''

result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))
# .匹配的是除换行符之外的任意字符，当遇到换行符时，.*?就不能匹配了，所以导致匹配失败。
# 这里添加一个修饰符re.S就可以修正这个错误。
# 这个修饰符的作用是使.匹配包括换行符在内的所有字符。
# 其他的一些修饰符如下：
'''
re.I        使匹配对大小写不敏感
re.L        做本地化识别（local-aware）匹配
re.M        多行匹配，影响^和$
re.S        使.匹配包括换行符在内的所有字符
re.U        根据Unicode字符集解析字符。这个标志影响\w,\W,\b和\B
re.X        该标志通过给与你更灵活的格式以便你将正则表达式写得更易于理解
'''
# 网页匹配中，常用的就是re.S和re.I


