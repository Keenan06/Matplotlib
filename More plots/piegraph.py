import matplotlib.pyplot as plt

values = [16, 18, 4, 8]
pielabels = ['Python', 'c#', 'C++', 'Java']
piecolors = ['blue', 'yellow', 'pink', 'orange']
pieexplode = [0, 0.1, 0, 0]

plt.pie(values, labels=pielabels, explode=pieexplode, colors=piecolors, startangle=180, shadow=True)
plt.title('Pie Chart')
plt.xlabel('H')
plt.ylabel('V')
plt.legend(loc='best')
plt.show()