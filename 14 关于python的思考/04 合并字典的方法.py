# 不同版本合并字典的方法：

# 3.5之后：使用解刨的形式
salary_first = {'lisa': 239000, 'Ganesh': 876500, 'john': 345000}
salary_second = {'Albert': 378299, 'Ary': 382791}

tt = {**salary_first, **salary_second}
print(tt)


# 3.5之前：使用的是update
salary = salary_first.copy()
salary.update(salary_second)

print(salary)
