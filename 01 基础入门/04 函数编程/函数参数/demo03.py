"""

"""


def func1(name, *, age=18):
    print(name, age)


func1(1)  # 1 18
func1(1, age=12)  # 1 12


def fun2(name, age=18):
    print(name, age)


fun2(1)  # 1 18
fun2(name=12)
fun2(**{"name": 12})
fun2(1, **{"age": 20})
