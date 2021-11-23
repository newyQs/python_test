import re

#  split(pattern, string, maxsplit=0, flags=0)
# returning a list containing the resulting substrings.
'''
re.split(pattern, string[, maxsplit=0, flags=0])
pattern:匹配的字符串
string:需要切分的字符串
maxsplit:分隔次数，默认为0(即不限次数)
flags:标志位，用于控制正则表达式的匹配方式
'''

print(re.split("[\w]+", "123dsd_+dk~dkkd"))  # ['', '+', '~', '']

print(re.split("[\W]+", "123dsd_+dk~dkkd"))  # ['123dsd_', 'dk', 'dkkd']

# 注：re.split()是以pattern作为分隔符，返回分割后的列表

s = "hdhe  jjjd JJ"

print(s.split(" "))  # ['hdhe', '', 'jjjd', 'JJ']
