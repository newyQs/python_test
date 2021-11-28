gcount = 0


def global_test1():
    gcount += 1
    print(gcount)


gcount = 0


def global_test2():
    global gcount  # 声明为全局变量，这样就可以修改了
    gcount += 1
    print(gcount)


def make_counter():
    """
    nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
    """
    count = 0

    def outer():
        def counter():
            nonlocal count
            count += 1
            return count

        return counter

    return outer


if __name__ == '__main__':
    ret = make_counter()
    print(ret()())
