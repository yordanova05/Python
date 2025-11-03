import random
try:
    while True:
        n = int(input())
        if n > 20 and n < 80:
            break
except ValueError:
    print("Inavalid input")
except ArithmeticError as e:
    print("Invalid input" + e)
    
list1 = []
for i in range(n):
    list1.append(random.randint(-800,1000))
print(list1)
    
count = 0
for num in list1:
    if (num >= -800 and num <= -100) or (num >=100 and num <= 999):
        last = (abs(num) // 100)
        if last % 3 == 0:
            count+=1

print(count)
list_negative = [x for x in list1 if x < 0]
list_positive = [x for x in list1 if x > 0]
index_max_minus = list1.index(max(list_negative))
index_min_plus = list1.index(min(list_positive))

print(index_max_minus)
print(index_min_plus)

list2 = [x for x in list1 if x % 7 == 0 and x % 2 != 0]
print(list2)

average = 0
countt = 0

for i in range(len(list2)):
    if i % 2 == 0 and i != 0:
        average += list2[i]
        countt +=1
if average != 0:
    print(average/countt)

for num in list2:
    if num > -100 and num < -9:
        print(num)
        
list2.remove(min(list2))
print(list2)





