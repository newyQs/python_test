"""
chr(i)
返回 Unicode 码位为整数 i 的字符的字符串格式。
例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。这是 ord() 的逆函数。

ord(c)
对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。
例如 ord('a') 返回整数 97， ord('€') （欧元符号）返回 8364 。这是 chr() 的逆函数。
"""

# chr <==> ord

print(chr(97))  # "a"
print(ord("a"))  # 97
