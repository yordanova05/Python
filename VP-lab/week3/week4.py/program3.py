# n = int(input("n = "))
# for i in range(n):
#     print("*"*(i+1))

n = int(input("n= "))
for i in range(n):
    print(" "*(n-i-1),end='')
    print('*'*(2*i+1))

