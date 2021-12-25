import re

# match和search的区别：match从头开始扫描匹配，search扫描整个字符串
# match
pattern = "^[03 爬虫基本原理-9]*$"  # 空或者只包含数字
test_str = ""
ret = re.match(pattern, test_str, flags=0)
print(ret)
# print(dir(ret))

# search
ret = re.match(pattern, test_str, flags=0)
print(ret)
