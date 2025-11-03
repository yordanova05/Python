# d = dict(<kluch> = <stoinost>)
# d = dict()
# d[<kluch>] = <stoinost>
# d1 = dict([(kluch,stoinost),(kluch,stoinost)])
# d2 = {kluch : stoinost , kluch : stoinost}

d = dict(name = "Ivan", last_name = " Ivanov", age = 18)
print(d)
print(d["last_name"])

d1 = dict([("name","Gosho"), ("last_name","Petrov"),("age",19)])
d2={"name" : "Grisho", "last_name": "Strashilov", "age" : 20}

print(d1)

"name" in d2 #True
len(d2)

d2["sex"]="male"
d2["name"]="Racho"  # prisvoqva nova stoinost pri veche prisustvasht kluch

del d2["sex"]
d2.pop("sex")

#metodite = keys() values() items
# keys() vrushta vsichki kluchove v spisuka
# values() vrushta vsichki stoinosti v spisuka
# items() kombinaciq na vsichki kluchove i stoinosti

for key in d1.items():
    print(key)

keys = list(d1.keys())
keys.sort()
for key in keys:
    print(key,d1[key])




days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Staurday","Sunday"]
d3 = {x+1 : days[x] for x in range(len(days))}

# mnojestvo - sudurja unikalni stoinosti
# elementite ne sa podredeni
s1 = set("hello")
print(s1)

s2 = set([1,2,4,True,False,0])
# TRUE nqma da vleze tui kato 1 == True kakto i False == 0
# shte vlqzat: (1,2,4,False)

s3 = {1,2,3,48,5,8,1,4}
s = set() #prazno mnojestvo
s = {} #prazen rechnik

s3.add(33)
s3.remove(1)
s3.pop(48)
s3.pop() # maha sluchaen element
s3.discard(1) # ako nqma kakvo da premahne nqma da izkara greshka

ss1 = {3,5,1,8}
ss2 = {2,8,5,4,6}
# | obedinenie ili method union()
ss3 = ss1|ss2 # {3,5,1,8,4,6}
ss3 = ss1.union(ss2)
# - razlika ili difference()
ss4 = ss1 - ss2 # {3,1} 
ss4 = ss2 - ss1 # {2,4,6}
ss4 = ss1.difference(ss2) # {3,1}
# & presichane intersection()
ss6 = ss1&ss2 # {8,5}
# ^ metrichna razlika symnetic.difference
ss7 = ss1^ss2 # {3,1,2,4,6}

3 in s1 #True
len(ss1) #4

for x in ss1 :
    print(x)

niz = "hello my friend"
niz[4] 

# [nachalo : krai: stupka]
niz[1:8:2] #"el y"
niz.title() # Hello My Friend
niz.split(".") #razbiva niza na podnizove
niz1 = " ".join(days)  #konkatinira spisuk sus zadaden parametur " "
#niz = "... Hello world...!"
niz.strip(". !") #izchistva nachaloto i kraq na zadadenite simvoli
niz.replace("a","A",2) #zamenq zdadeniq argument s tekushtiq (zamenq a, s A, broi na zameni)
niz.find("my") #vrushta indexa na nachaloto na niza, vrustha 6 AKO GO NQMA SHTE VURNE -1
niz.index("my") #vrushta indexa na nachaloto na niza, vrustha 6 AKO GO NQMA SHTE VURNE GRESHKA

