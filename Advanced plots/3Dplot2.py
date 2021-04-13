import numpy as npy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = npy.random.rand(10)
y1 = npy.random.rand(10)
z1 = npy.random.rand(10)

x2 = npy.random.rand(10)
y2 = npy.random.rand(10)
z2 = npy.random.rand(10)

ax.scatter(x1, y2, z1, s=20, color='red', marker='^')
ax.scatter(x2, y2, z2, s=20, color='blue', marker='o')

plt.show()