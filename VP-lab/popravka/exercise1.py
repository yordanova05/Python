while True:
    try:
        num = int(input())
        if 60 > num > 40:
            break
        else:
            raise ArithmeticError ("Invalid input")
    except ValueError:
        print("Invalid input!")
        
list1 = []
list2= []
for x in range(num):
    
    while True:
        n = int(input())
        
        if 5900 > n > -6000:
            
            if abs(n) > 9:
                desetici = abs(n // 10) % 10
                if desetici % 4 == 0 :
                    list1.append(n)
                    break
                
            if abs(n) > 99:
                stotici = abs(n // 100) % 10
                if stotici == 6:
                    list1.append(n)
                    break
                    
            if n % 3 == 0 and n % 2 == 1:
                list2.append(n)
                break
        
        break
        
print(list1)
print(list2)

#purvi spisuk!
sum1 = 0
count = 0

for x in list1:
    if abs(x) > 99 and x % 2 == 1:
        sum1 += x
        count += 1

print(sum1/count)
    
max_negative = max([x for x in list1 if x < 0 and x % 2 == 0])
min_positive = min([x for x in list1 if x > 0 and x % 2 == 0])

print("Index max_negative: ", list1.index(max_negative))
print("Index min_positive: ", list1.index(min_positive))

for i in range(len(list1)-1, -1, -1):
    if list1[i] > 999 and list[i] % 2 == 0:
        list1.remove(list1[i])

print(list1)

#vtori spisuk!
count2 = 0
for x in list2:
    if 9 < x < 100:
        count += 1
        print(x)
        
print(count2)
        
proizvedenie = 1

for i in range(len(list2)):
    if i % 2 == 1 and list2[i] < 0:
        proizvedenie *= list2[i]
        
print(proizvedenie)

if len(list1) > len(list2):
    list1.reverse()
    
    for i in range(len(list1) -1, -1, -1):
        if len(list1) == len(list2):
            break
        
        list1.remove(list1[i])
    
    list1.reverse()
        
elif len(list1) < len(list2):
    list2.reverse()
    
    for i in range(len(list2) -1, -1, -1):
        if len(list1) == len(list2):
            break
        
        list2.remove(list2[i])
    
    list2.reverse()
    
print(list1)
print(list2)