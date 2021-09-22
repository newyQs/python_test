import numpy as np

'''
A x = b
其中
A=[[ 2  1 -2]
 [ 3  0  1]
 [ 1  1 -1]]
 
b=[[-3]
 [ 5]
 [-2]]

'''
A = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
print(A)

b = np.transpose(np.array([[-3, 5, -2]]))
print(b)

x = np.linalg.solve(A, b)
print(x)
