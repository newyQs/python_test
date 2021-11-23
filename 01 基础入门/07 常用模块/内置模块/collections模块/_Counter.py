from collections import Counter

countries = ['Bers', 'Alld', 'Mdkf', 'Ukrain', 'Brkd', 'Alld', 'Mdja', 'Kowjd', 'Bead']
t = Counter(countries)

# 注意：Counter()是dict的子类，可以使用字典的全部方法
print(t)  # Counter({'Bers': 1, 'Alld': 1, 'Mdkf': 1, 'Ukrain': 1, 'Brkd': 1, 'Mdja': 1, 'Kowjd': 1, 'Bead': 1})

for i in t.items():
    print(i)

# most_common()方法
print(t.most_common())
print(t.most_common(1))
print(t.most_common(2))

# elements()方法
print(t.elements())
for i in t.elements():
    print(i)
