import numpy as np

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

print(a[2, 4])  # >>>25

print(a[0, 1:4])  # >>>[12 13 14]
print(a[1:4, 0])  # >>>[16 21 26]
print(a[::2, ::2])  # >>>[[11 13 15]
                    #     [21 23 25]
                    #     [31 33 35]]
print(a[:, 1])  # >>>[12 17 22 27 32]



print(type(a))  # >>><class 'numpy.ndarray'>
print(a.dtype)  # >>>int32
print(a.size)  # >>>25
print(a.shape)  # >>>(5, 5)
print(a.itemsize)  # >>>4
print(a.ndim)  # >>>2
print(a.nbytes)  # >>>100