def palindrom(number:str):
    palindrom_number = number[::-1]
    if palindrom_number == number:
        print(1)
    else:
        print(0)
num = input()
palindrom(num)