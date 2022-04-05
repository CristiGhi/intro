# ex 1 - O variabilă este un nume pentru un loc din memoria computerului în care stocam unele date
# ex 2
s ='tema1'
i = 32
b = False
f = 3.14

# ex 3
print(type(s))
print(type(i))
print(type(b))
print(type(f))

# ex 4    rotunjim un float
f=round(f)
print(round(f))

# ex 5
print('Am facut ' + s)
print(f'{i} este nr meu preferat')
print(f'Daca b nu e True atunci e {b}')
print(f'pi are valoarea {f}')

# ex 6    afiseaza 'Numele complet are x caractere'
numele = 'Ghiurco'
prenumele = 'Cristi'
print(f'Numele complet are ' + str(len(numele + prenumele)) + ' caractere')

# ex 7  aria dreptunghiului
L = 15
l = 30
x = L * l
print(f'Aria dreptunghiului este {x} ')

# ex 8   afiseaza stringul fara ultimele x caractere
d = 'Coral is either the stupidest animal or the smartest rock'
x1 = 10
print(d[:-(x1)])

# ex 9   declaram primele 5 si ultimele 5 caractere
d1 = (d[:5] + d[-5:])
print(d1)

# ex 10    afisati de cate ori apare cuvantul 'the'
print(d.count('the'))

# ex 11    inlocuieste the cu THE peste tot
print(d.replace('the' , 'THE'))

# ex 12    salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
print(len(d))
k = d.find('rock') +1
print(k)
print(d[:53])     # afiseaza tot stringul pana la acest cuvant

# ex 13   declarati o alta variabila de tip string in care sa le adaugati folosind tehnica de formatare a unui string
n = (f'{s}  {i}  {b}  {f}')
print(n)

# ex 14 afisati doar numerele pare ; afisati doar numerele impare
v = '0123456789'
print(v[::2])
print(v[1::2])

# ex 15     Aveti un dreptunghi, declarati 2 variabile pe nume “lungime” si “latime”, ele trebuie sa primeasca ca si input de la tastatura dimensiunile.
          # Printati aria calculata a dreptunghilui
lungime = int(input('introdu lungimea ' ))
latime = int(input('introdu latimea '))
aria = lungime * latime
print (aria)

# ex 16    citeste de la tastatura un string de dimensiune impara
         # afiseaza caracterul din mijloc
w = input('Scrie string : ')
print(w[(len(w)-1)//2:(len(w)+2)//2])


# ex 17   folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare



