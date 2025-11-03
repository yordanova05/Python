def figura(name):
    if name == "triugulnik":
        a = float(input("a = "))
        b = float(input("b = "))
        h = float(input("h = "))
        print("S = ",(a+b)*h/2)
    elif name == "kvadrat":
        a = float(input("a = "))
        print("S = ",a*a)
    elif name == "pravougulnik":
        a = float(input("a = "))
        b = float(input("b = "))
        print("S = ",a*b)
f = input("figura : ")
figura(f)