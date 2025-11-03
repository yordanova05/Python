n = int(input("n= "))
list=[]
for i in range(n):
    numbers = int(input(f"numebr{i+1}= "))
    list.append(numbers)
print(max(list))