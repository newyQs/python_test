"""
https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto

sorted(iterable, *, key=None, reverse=False)

根据 iterable 中的项返回一个新的已排序列表。
具有两个可选参数，它们都必须指定为关键字参数。
key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。 默认值为 None (直接比较元素)。
reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。
内置的 sorted() 确保是稳定的。 如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的 --- 这有利于进行多重排序（例如先按部门、再按薪级排序）。
"""
from operator import itemgetter, attrgetter, methodcaller

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda student: student[2]))
print(sorted(student_objects, key=lambda student: student.age))  # sort by age


print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age')))
# Operator 模块功能允许多级排序。 例如，按 grade 排序，然后按 age 排序：
sorted(student_tuples, key=itemgetter(1, 2))
sorted(student_objects, key=attrgetter('grade', 'age'))
