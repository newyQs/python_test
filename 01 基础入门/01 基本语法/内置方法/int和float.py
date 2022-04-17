"""
class int([x])
class int(x, BASE=10)

返回一个基于数字或字符串 x 构造的整数对象，或者在未给出参数时返回 0
如果 x 不是数字，或者有 BASE 参数，x 必须是字符串、bytes、表示进制为 BASE 的 整数字面值 的 bytearray 实例

class float([x])

返回从数字或字符串 x 生成的浮点数
"""
print(int())
print(int(2.3))
print(int(2.7))

print(int("33"))
# print(int("23.9")) # ValueError: invalid literal for int() with BASE 10: '23.9'
# print(int("22-10"))

print(float(2))
print(float(2.6))
print(float("22.2"))
print(float("22"))
