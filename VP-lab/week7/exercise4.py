def f(l,num):
    for n in range(len(l)):
        if l[n] > num:
            l[n] = 0
    print(l)


data = []
number = int(input("num:"))
for n in range(10):
    num = int(input(f"num{n+1}: "))
    data.append(num)

f(data,number)

