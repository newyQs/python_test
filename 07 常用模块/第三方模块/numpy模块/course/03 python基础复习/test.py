import numpy as np

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
print(np.array([1, 2, 3]))
print('-----')
print(np.array([[1, 2], [3, 4]]))
print('-----')
print(np.array([1, 2, 3, 4, 5], ndmin=2))
print('-----')
print(np.array([1, 2, 3], dtype=complex))
print('-----')

print(np.dtype(np.int32))
