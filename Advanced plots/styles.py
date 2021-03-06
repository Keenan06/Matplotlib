import matplotlib.pyplot as plt

plt.style.use('bmh')
print(plt.style.available)

x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]

plt.bar(x1, y1)
plt.title('Title')
plt.xlabel('H title')
plt.ylabel('V title')
plt.show()