# 示例1：两个整数相加，不是int类型就返回None
def sum(f1, f2):
    if isinstance(f1, int) and isinstance(f2, int):
        return f1 + f2
    else:
        return None


sum(12, 5)
sum(12, 'str')


# 示例2：如果找不到奇数就返回None，如果Number的类型不是列表也返回None
def find_odd_number(numbers):
    odd_numbers = []
    if not isinstance(numbers, list):
        return None

    for item in numbers:
        if item % 2 == 0:
            odd_numbers.append(item)
    return odd_numbers


