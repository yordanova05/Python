number_2 = [2,5,12,4,56]
number_2.remove(min(x for x in number_2 if x % 2 == 0))
print(number_2)