def multiple_generator(number, limit):
    counter = 1
    value = number * counter

    while value <= limit:
        yield value
        counter += 1
        value = number * counter


gen = multiple_generator(500, 1000)
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())

# for num in gen:
#     print(num)

# yield关键字不存结束整个函数，只是暂停函数的操作，直到下一次的调用
