"""

"""


def func1(name, *args, age=18):
    print(name, args, age)


func1(1, 2, 11)  # 1 (2, 11) 18
func1(1, 2, age=11)  # 1 (2,) 11

func1(1, 2, 3, age=11)  # 1 (2, 3) 11
