import matplotlib.pyplot as plt
import seaborn as sbn

sbn.set_style("darkgrid")
x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]

plt.bar(x1, y1)
plt.title('Title')
plt.xlabel('H')
plt.ylabel('V')
plt.show()