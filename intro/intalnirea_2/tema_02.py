# ex-01 Instructiunea if se foloseste pentru a executa o instructiune sau o secventa de instructiuni numai cand valoare logica a unei expresii este adevarata
# ex-02 Verifica si afiseaza daca x este numar pozitiv sau nu
# ex-03 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
try:
    x = int(input('Type number : '))
except:
    print('is not a number ')
else:
    if x > 0:
        print('numar pozitiv')
    elif x < 0:
        print('numar negativ')
    else:
        print('numarul e neutru ')

#ex_04 Verifica si afiseaza daca x este intre -2 si 13
x = int(input('Type number : '))
if x >= -2 and x <= 13:
    print('nr corect')
else:
    print('nr nu se situeaza intre -2 si 13')

#ex_05 Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = 10
y = 3
if x-y < 5:
    print('diferenta mai mica decat 5')

else:
    print('try again !')

#ex_06 Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = int(input('introduceti numarul: '))
if not(x >= 5 and x <= 27):
    print('try again !')
else:
    print('nr intre 5 si 27')

#ex_07 x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
x = 4
y = 5
if x == y:
    print('x egal cu y')
elif x > y:
    print(x)
else:
    print(y)

#ex_08 X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare
x = 3
y = 3
z = 2
if x == y and x == z and y == z :
    print('triunghi echilateral')
elif x !=y and x != z and y != z :
    print('triunghi oarecare')
else:
    print('triunghi isoscel')


#ex_09 Citeste o litera de la tastatura
#Verifica si afiseaza daca este vocala sau nu
x = input('Introdu litera: ')
vocale = ('a', 'e', 'i', 'o', 'u', 'y')
if x.lower() in vocale:
    print ('Vocala !')
else:
    print ('Nu este o vocala !')

# ex_10 Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = int(input('Nota este : '))
if nota >= 9 and nota <= 10:
    print('echivalentul in sistem american este A')
elif nota >= 8 and nota < 9:
    print('echivalentul in sistem american este B')
elif nota >=7 and nota < 8:
    print('echivalentul in sistem american este C')
elif nota >= 6 and nota < 7:
    print('echivalentul in sistem american este D')
elif nota >=4 and nota < 6:
    print('echivalentul in sistem american este E')
elif nota < 4:
    print('echivalentul in sistem american este F')
else:
    print('Nota invalida ')


#ex_11 Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = input('introdu nr :')
if len(x) >= 4 :
    print('Nr are minim 4 cifre ')
elif x[0] == 0:            #vroiam sa fac o completare
    print('mai incearca !')     #aici nu reusesc, in caz ca nr introdus de la tastatura incepe cu 0
else:
    print('mai incearca !')


#ex_12 .Verifica daca x are exact 6 cifre
x = input('introdu nr :')
if len(x) == 6:
    print('Nr are 6 cifre')

#ex_13 Verifica daca x este numar par sau impar
x = int(input('introdu nr :'))
if x % 2 == 0 :
    print('nr par')
else:
    print('nr impar')

#ex_14 x, y, z (int) Afiseaza care este cel mai mare dintre ele?
x = int(input('introdu x :'))
y = int(input('introdu y :'))
z = int(input('introdu z :'))
if x > y and x > z:
    print (f'cel mai mare numar este {x}')
elif y > x and y > z:
    print (f'cel mai mare numar este {y}')
else:
    print (f'cel mai mare numar este {z}')


#ex_15 X, y, z - reprezinta unghiurile unui triunghi Verifica si afiseaza daca triunghiul este valid sau nu
x = int(input('Introduceti unghiul x: '))
y = int(input('Introduceti unghiul y: '))
z = int(input('Introduceti unghiul z: '))

if x + y + z < 180 :           # suma unghiurilor nu trebuie sa depaseasca 179° ca sa fie un triunghi
    print ('Triunghi valid')
else:
    print('Triunghiul nu este valid')

# la ex 16 nu prea am inteles