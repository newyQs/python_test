# Boolean masking
import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2 * np.pi, 50)
print(a)
b = np.sin(a)
print(b)
plt.plot(a, b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()
