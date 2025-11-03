import random
data = []
data1 = []
for x in range(10):
    data.append(random.randint(0,10))

for i in range(len(data)):
    data1.append(data[i])
    if i < len(data) - 1:
        sum_value = data[i] + data[i + 1]
        data1.append(sum_value)

print(data)
print(data1)