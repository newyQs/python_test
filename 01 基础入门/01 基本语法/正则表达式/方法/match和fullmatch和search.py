import re

# match(pattern, string, flags=0)
# returning a Match object, or None if no match was found.
# re.match()

# fullmatch(pattern, string, flags=0)
# returning a Match object, or None if no match was found.
# re.fullmatch(pattern, string, flags=0)

# search(pattern, string, flags=0)
# returning a Match object, or None if no match was found.
# re.search(pattern, string, flags=0)

# 用法：
pattern = "[\w]+"

if re.match(pattern, "~123"):  # 字符串开头匹配 --> obj or None
    print("match：测试通过")

if re.search(pattern, "wjj123"):  # 字符串只要匹配 --> obj or None
    print("search：测试通过")

if re.fullmatch(pattern, "wdss"):  # 字符串完整匹配 --> obj or None
    print("fullmatch：测试通过")
