list_10 = []
while True:
    x = int(input("Число:"))
    if x > 0:
        list_10.append(x)
    if len(list_10) == 10:
        break
print(list_10)   

count = 0
for x in list_10:
    if x % 2 == 0:
        count+=1
print(count)

proizvedenie = 1
for x in list_10:
    proizvedenie*=x
print(proizvedenie)

list_10.sort()
list_3 = []
for i in range(len(list_10)):
    if list_10[i] % 2 != 0 and len(list_3) < 3:
        list_3.append(list_10[i])
print(list_3)

list_3.sort()
list_3.append(100)
list.append(200)
    