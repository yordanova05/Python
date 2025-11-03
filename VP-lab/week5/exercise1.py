
n = int(input("n = "))
while True:
    if n < 0:
        n = int(input("n = "))
    elif n==0:
        n = int(input("n = "))
    elif n > 0:
        break
    
one = []
two = []

for x in range(0,n+1):
    one.append(x)
for x in range(n,-1,-1):
    two.append(x)
print(tuple(one))
print(tuple(two))
print(sorted(one,reverse=True))