list_10 = []
for x in range(10):
    while True:
        num = int(input("Цяло положително число:"))
        if num >=0 :
            list_10.append(num)
            break
print(list_10)

for num in list_10:
    if num % 2 != 0:
        print(num)
        
average = sum(list_10)/len(list_10)
print(average)

list_10.sort(reverse=True)
list_5 =[]
for x in list_10:
    if x % 2 == 0 and len(list_5) < 5:
        list_5.append(x)

print(list_5)
list_5.sort(reverse=True)

for i in range(len(list_5)-1, -1, -1):
    if i % 2 == 0 and i != 0:
        list_5.remove(list_5[i])
         
print(list_5)
    
    
    