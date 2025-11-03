n = int(input("n= "))
sum = 0
for i in range(n):
    num = int(input("numbers: "))
    sum +=num
print(sum)
#nachin 2
data=[]
for i in range(n):
    num = int(input("numbers: "))
    data.append(num)
print(sum(data))
