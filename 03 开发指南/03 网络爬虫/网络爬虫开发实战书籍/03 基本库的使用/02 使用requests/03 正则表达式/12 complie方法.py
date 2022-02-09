import re

# 将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
# compile(pattern, flags=0)
content1='2021-06-08 12:00'
content2='2021-06-12 14:00'
content3='2021-06-18 15:00'

pattern=re.compile('\d{2}:\d{2}')

result1=re.sub(pattern,'',content1)
result2=re.sub(pattern,'',content2)
result3=re.sub(pattern,'',content3)

print(result1,result2,result3)