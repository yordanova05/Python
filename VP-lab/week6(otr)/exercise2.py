# programa v koqto potrebitelq vuvejda cqlo chislo, suzdava se spisuk,
# sustoi se ot chisla ot edno do tova chislo vuz osnova na spisuka se suzdava rechnik
# ot tozi rehcnik elementite na spisuka slujat za kluchove
# a stoinosti na elementite sa elementite na spisuka v obraten red

n = int(input("n = "))
my_list = []
my_reversed_list = []
d = {}

for i in range(1,n+1):
    my_list.append(i)

my_reversed_list = sorted(my_list,reverse=True)

for x in range(len(my_list)):
    d[my_list[x]]=my_reversed_list[x]

print(d)

