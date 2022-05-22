
from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool() as p:
        for i in range(1, 11):
            res = p.apply(f, (i,))
            print(res, end=",")
