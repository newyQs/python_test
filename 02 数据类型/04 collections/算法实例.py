import time


# 若a+b+c=1000,a^2+b^2=c^2，求a,b,c

# 算法1
def calc1():
    start_time = time.time()
    for i in range(1001):
        for j in range(1001):
            for k in range(1001):
                if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                    print(i, j, k)

    end_time = time.time()
    print(f'消耗时间：{end_time - start_time}')


# 算法2
def calc2():
    start_time = time.time()
    for i in range(1001):
        for j in range(1001):
            k = 1000 - i - j
            if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                print(i, j, k)

    finish_time = time.time()
    print(f'算法2消耗时间：{finish_time - start_time}')


calc2()
