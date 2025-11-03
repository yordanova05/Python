possitive = []
negative = []
zero = []
even=[]
odd=[]
numbers=[]
upper_ten=0
while True:
    number = int(input("Number: "))
    numbers.append(number)
    if len(numbers)==10 or number == -1:
        break
    elif number == 0:
        zero.append(number)
    elif number<0:
        if number%2==0:
            even.append(number)
        else: 
            odd.append(number)
        negative.append(number)
    elif number>0:
        if number>10:
            upper_ten=upper_ten+1
        if number%2==0:
            even.append(number)
        else: 
            odd.append(number)
        possitive.append(number)

print("possitive len:",len(possitive) )
print("negative len:",len(negative) )
print("zeros len:",len(zero) )
print("sredna stoinost na possitive:",sum(possitive)/len(possitive))
print("sredna stoinost na negative:",sum(negative)/len(negative))
print("sredna stoinost na zeros:",sum(zero)/len(zero))
print("odd: ",odd)
print("even: ",even)
print("Above 10 numbers counter: ",upper_ten)
