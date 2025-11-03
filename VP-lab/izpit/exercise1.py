while True:
    n = int(input())
    if n >15 and n<35:
        break

numbers = []
number_4 = []
numbers_2_3 = []
average = 0

for i in range(n):
    while True:
        num = int(input())
        if num > 30 and num < 300:
            numbers.append(num)
            break
        else: 
            print("number between 30 and 300!")

for num in numbers:
    num_des = num%10
    if num_des == 3 or num_des ==  6 or num_des == 9:
        print(num, end = " ")

for number in numbers:
    if number % 6 == 4:
        number_4.append(number)
print("\nIndex ostatuk 4: ",numbers.index(min(number_4)))

for number in numbers:
    if number < 100:
        if number % 2 == 0 or number % 3 == 0:
            numbers_2_3.append(number)

print("Numbers kratni na 2 ili 3: ", numbers_2_3)

len_necheten_index =0
for i in range(1,len(numbers_2_3)+1,2):
    average += numbers_2_3[i]
    len_necheten_index+=1
print("Average: ", average/len_necheten_index)

min = min(numbers_2_3)
numbers_2_3.remove(min)
print("Nem list: ",numbers_2_3)