# programa v koqto potrebitelq vuvejda text, na negova baza se suzdava rechnik, za kluchove na rechnika slujat simvolite ot teksta
# a stoinostta na elementite se opredelq ot broq na suotvetnite simvoli v teksta
# primer : "SWTABAASW" ===== A: 3 S: 2 T: 1 B:1

text = input("Text: ")
d = {}
for key in text:
    d[key] = 0
for value in text:
    d[value] +=1
for k in d:
    print(f"{k} : {d[k]}", end = " ")
