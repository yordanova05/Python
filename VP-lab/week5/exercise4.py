n = int(input("n = "))
my_list = []
my_dict = {}
value = []
for x in range(1,n+1):
    my_list.append(x)

for x in range(len(my_list),0,-1):
    value.append(x)

for i in range(len(my_list)):
    my_dict[my_list[i]] = value[i]

print(my_list)
print(value)
print(my_dict)
