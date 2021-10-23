import re

pattern = "^[0-9]*$"  # 空或者只包含数字
test_str = "123"

# sub
ret = re.sub(pattern, "+", test_str)
print(ret)

# subn
ret = re.subn(pattern, "+", test_str)
print(ret)
