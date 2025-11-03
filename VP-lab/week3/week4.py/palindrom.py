word = input("Word: ").lower()

if len(word)<=1:
    print("Dumata e tvurde kratka!")
elif (word == word[::-1]):
    print("Palindrom!")
