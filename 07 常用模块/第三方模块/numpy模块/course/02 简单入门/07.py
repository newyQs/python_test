import numpy as np

# Fancy indexing
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]
print(a)  # >>>[ 0 10 20 30 40 50 60 70 80 90]
print(b)  # >>>[10 50 90]
