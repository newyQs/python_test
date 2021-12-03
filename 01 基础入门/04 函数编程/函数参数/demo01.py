"""
func(index, name=jack, age=18)
func(index,*args)
func(index,name=12)
"""


def func1(name, *args, **kwargs):
    print(name, args, kwargs)


func1(1)  # 1 () {}
func1(1, ())  # 1 ((),) {}            # 这个
func1(1, 2)  # 1 (2,) {}
func1(1, 2, 3)  # 1 (2, 3) {}
func1(1, (2, 3))  # 1 ((2, 3),) {}
func1(1, *(2, 3))  # 1 (2, 3) {}

func1(1, x=2)  # 1 () {'x': 2}
func1(1, x=2, y=3)  # 1 () {'x': 2, 'y': 3}
func1(1, (), {})  # 1 ((), {}) {}            # 这个
func1(1, {"x": 1})  # 1 ({'x': 1},) {}

func1(1, *{"x": 1, "y": 2})  # 1 ('x', 'y') {}
func1(1, **{"x": 1, "y": 2})  # 1 () {'x': 1, 'y': 2}
