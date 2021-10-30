def sum(f1, f2):
    if isinstance(f1, int) and isinstance(f2, int):
        return f1 + f2
    else:
        raise ValueError('provide only int values')


def find_first_odd_number(numbers):
    odd_numbers = []
    if isinstance(numbers, list):
        raise ValueError('only accept list, wrong data type')

    for item in numbers:
        if item % 2 == 0:
            odd_numbers.append(item)

    return odd_numbers
