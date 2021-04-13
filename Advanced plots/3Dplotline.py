import numpy as npy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [1, 2, 4, 8, 16]
z = [2, 2, 2, 2, 2]

ax.plot(x, y, z)
plt.show()