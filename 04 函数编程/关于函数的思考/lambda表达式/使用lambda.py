numbers = []

# 使用lambda表达式
sort_numbers = sorted(numbers, key=lambda num: abs(num))


# 使用函数
def sort_numbers(numbers):
    return sorted(numbers, reverse=True)
