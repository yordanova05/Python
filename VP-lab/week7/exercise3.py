def calculator1(num1,num2):
        print(num1+num2)

def calculator2(num1,num2):
        print(num1-num2)

def calculator3(num1,num2):
        print(num1/num2)

def calculator4(num1,num2):
        print(num1*num2)

command = input("command: ")
num1 = float(input())
num2 = float(input())

if command == "+":
    calculator1(num1,num2)
elif command == "-":
    calculator2(num1,num2) 
elif command == "*":
    calculator4(num1,num2) 
elif command == "/":
    calculator3(num1,num2)


