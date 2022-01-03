# 一行解决
def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]
