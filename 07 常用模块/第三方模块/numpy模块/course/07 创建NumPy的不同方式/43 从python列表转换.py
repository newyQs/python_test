import numpy as np

array = np.array([4, 5, 6])
print(array)

mylist = [1, 2, 4]
print(np.array(mylist))

print(type(array), type(mylist))

print(np.array([(1, 2, 3), (4, 5, 6)]))
print(np.array([[1, 2, 3], (4, 5, 6)]))
print(np.array(([1, 2, 3], (4, 5, 6))))
