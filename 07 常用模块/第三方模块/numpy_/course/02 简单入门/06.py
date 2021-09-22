import numpy as np

# dot, sum, min, max, cumsum
a = np.arange(10)

print(a.sum())  # >>>45
print(a.min())  # >>>0
print(a.max())  # >>>9
print(a.cumsum())  # >>>[ 0  1  3  6 10 15 21 28 36 45]
