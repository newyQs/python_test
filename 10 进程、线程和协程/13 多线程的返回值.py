import threading

rst = None
flag = False


def func(data):
    global rst
    global flag
    rst = data * data
    flag = True


if __name__ == '__main__':
    t = threading.Thread(target=func, args=(3,))
    t.start()
    while flag == True:
        print(rst)
        break
