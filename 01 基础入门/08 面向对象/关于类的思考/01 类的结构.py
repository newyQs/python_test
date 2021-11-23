'''
倾向于按照以下顺序组织类的结构：
1）类变量
2）__init__
3）Python的内置方法(__call__、__repr__等)
4）类方法
5）静态方法
6）属性
7）实例方法
8）私有方法
'''
import datetime


class Employee(person):
    POSITIONS = ('Superwiser', 'Manager', 'CEO', 'Founder')

    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        self.age = None
        self._age_last_calculated = None
        self._recalculated_age()

    def __str__(self):
        return 'Name:' + self.name + '\nDepartment:' + self.department

    @classmethod
    def no_position_allowed(cls, position):
        return [t for t in cls.POSITIONS if t != position]

    @staticmethod
    def c_position(position):
        return [t for t in TITLES if t in position]

    @property
    def id_with_name(self):
        return self.id, self.name

    def age(self):
        if datetime.date.today() > self._age_last_calculated:
            self._recalculated_age()
        return self.age

    def _recalculated_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        if today < datetime.date(today.year, self.birthday.month, self.birthday.year):
            age -= 1

        self.age = age
        self._age_last_calculated = today
