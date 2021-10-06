from collections import namedtuple


# 不变的类
class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point(3, 4, 5)
print(p.x, p.y, p.z)

# 使用namedtuple
Point = namedtuple('Point', ['x', 'y', 'z'])
point = Point(x=5, y=6, z=9)
print(point.x, point.y, point.z)
