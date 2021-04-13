import matplotlib.pyplot as plt
import numpy as npy
import seaborn as sns
sns.set_style("darkgrid")

N = 150
x1 = npy.random.rand(N)
y1 = npy.random.rand(N)
s1 = npy.random.rand(N) * 30
x2 = npy.random.rand(N)
y2 = npy.random.rand(N)
s2 = npy.random.rand(N) * 30

plt.scatter(x1, y1, s=s1)
plt.scatter(x2, y2, s=s2)
plt.title('Title')
plt.xlabel('H title')
plt.ylabel('V title')
plt.show()