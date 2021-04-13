import matplotlib.pyplot as plt
import numpy as npy

x = npy.arange(0, 10)
y1 = 0.05 * x * x
y2 = 0.03 * x * x

plt.ylim(0, 5)
plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='green')
plt.fill_between(x, y1, y2, color='red', alpha=0.5)
plt.show()
