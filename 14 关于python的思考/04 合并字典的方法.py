# Python3.5+中实现字典合并的方法
salary_first = {'lisa': 239000, 'Ganesh': 876500, 'john': 345000}
salary_second = {'Albert': 378299, 'Ary': 382791}

tt = {**salary_first, **salary_second}
print(tt)

# 3.5之前的方法
salary = salary_first.copy()
salary.update(salary_second)

print(salary)
