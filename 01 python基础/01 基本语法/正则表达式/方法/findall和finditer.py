import re

# findall(pattern, string, flags=0)
# return a list of all non-overlapping matches in the string.
# re.findall(pattern, string, flags=0)

# finditer(pattern, string, flags=0)
# Return an iterator over all non-overlapping matches in the string.
# re.finditer(pattern, string, flags=0)

# 用法
pattern = "[\w]+"

print(re.findall(pattern, "dj%l~12"))
if re.findall(pattern, "djll12"):  # --> List
    print("findall：测试通过")

print(re.finditer(pattern, "sdkk24"))
if re.finditer(pattern, "sdkk24"):  # --> Iterator
    print("finditer：测试通过")
