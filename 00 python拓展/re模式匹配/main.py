import re

# match(pattern, string, flags=0): return _compile(pattern, flags).match(string)

ret = re.match('^[0-9]*$', "w14857")
# returning a Match object, or None if no match was found.
print("match:", ret)  # 输出：<re.Match object; span=(0, 3), match='123'> 或者None

if ret:
    print('从开头匹配到数字')
# fullmatch(pattern, string, flags=0):return _compile(pattern, flags).fullmatch(string)
ret = re.fullmatch('^[0-9]*$', "w14857")
print("fullmatch:", ret)

# search(pattern, string, flags=0): return _compile(pattern, flags).search(string)
ret = re.search('^[0-9]*$', "w14857")
# returning a Match object, or None if no match was found.
print("search:", ret)

if ret:
    print('全局匹配到数字')

# sub(pattern, repl, string, count=0, flags=0): return _compile(pattern, flags).sub(repl, string, count)
ret = re.sub('^[0-9]*$', "+", "w14857")
print("sub:", ret)

# subn(pattern, repl, string, count=0, flags=0):return _compile(pattern, flags).subn(repl, string, count)
ret = re.subn('^[0-9]*$', "+", "24857")
print("subn:", ret)

# split(pattern, string, maxsplit=0, flags=0):return _compile(pattern, flags).split(string, maxsplit)
ret = re.split('^[0-9]*$', "w14857")
print("split:", ret)

# findall(pattern, string, flags=0):return _compile(pattern, flags).findall(string)
ret = re.findall('^[0-9]*$', "w14857")
print("findall:", ret)

# finditer(pattern, string, flags=0):return _compile(pattern, flags).finditer(string)
ret = re.finditer('^[0-9]*$', "w14857")
print("finditer:", ret)

# compile(pattern, flags=0):return _compile(pattern, flags)
ret = re.compile('^[0-9]*$')
print("compile:", ret)
