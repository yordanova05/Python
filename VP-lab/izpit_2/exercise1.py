import random
try:  
    while True:  
        n = int(input())
        if n > 20 and n < 30:
            break
except ValueError:
    raise "Invalid input!"
except ArithmeticError as e:
    raise e

numbers = []

for i in range(n):
    numbers.append(random.randint(-100,100))
    
sum = 0

for i in range(1,n,2):
    sum += numbers[i]
    
print(sum)

count = 0
proizvedenie = 1

for num in numbers:
    num1 = num%10
    if (num1) % 2 == 0:
        count+=1
    if num < 0 and num % 2 == 0:
        proizvedenie *= num
        
print(count)
print(proizvedenie)    

list2 = [x for x in numbers if x > n]
print(list2)
result = max(list2) - abs(min(list2))
print(result)

count_2 = 0

for y in list2:
    if y % 2 != 0:
        print(y, end = " ")
        count_2+=1
print("\n",count_2)

list2.remove(min(list2))
print(list2)