import matplotlib.pyplot as plt
import numpy as npy

x = npy.arange(0, 10)
y = 0.05 * x * x

plt.ylim(0, 10)
plt.plot(x, y, color='turquoise')
plt.fill_between(x, y, color='turquoise', alpha=0.5)
plt.show()
