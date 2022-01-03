import re

content = '54aK54yr5oiR54ix5L2g'
# re.sub(pattern, repl, string, count=0, flags=0)
content_sub = re.sub('\d+', '', content)

print(content_sub)

# 修改文本
# 将一串字符串中的所有数字去掉
# 如果使用字符串的replace()方法就太麻烦了
# 使用re.sub('pattern','',s)就很方便
