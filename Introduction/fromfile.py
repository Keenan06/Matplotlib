x = []
y = []

with open('values.txt','r') as myfile:
    for line in myfile:
        y.append(int(line))

x = list(range(0, len(y)+1))
print(x)
print(y)