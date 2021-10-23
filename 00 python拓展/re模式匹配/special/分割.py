import re

pattern = "^[0-9]*$"  # 空或者只包含数字
test_str = ""
ret = re.split(pattern, test_str)
print(ret)
