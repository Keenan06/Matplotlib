import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]

colors = ['green', 'red', 'blue', 'white', 'lightblue']

plt.bar(x1, y1, edgecolor='black', color=colors, linewidth=2.5)
plt.title('Title')
plt.xlabel('H')
plt.ylabel('V')
plt.show()