text = (input("Text: "))
d = {}
if text.isalpha():
    for x in text:
        d[x] = 0
    for i in text:
        d[i] += 1
    for k in d:
        print(f"{k}:{d[k]}")
else: print("Error")
