#dalmatienii
for i in range(1,102):
    print(f'Dalmatianul cu nr {i}' )

# dalmatienii din 2 in 2
for i in range(1,102, 2):    #al 3-lea - pasul (din 2 in 2)
    print(f'Dalmatianul cu nr {i}' )


numere=[3, 7, 10, 20, 30]
#parcurgere liste cu for prin intermediul indexului
for i in range(0, len(numere)):
    print(f'indexul curent este {i}')
    print(f'numarul curent este {numere[i]}')

# for each
s=0

for numar in numere:
    print(f'Numarul curent este {numar}')
    s=s+numar
print (f'suma este {s}')

# de cate ori apare 3 in [3, 2, 3, 5, 3, 3]