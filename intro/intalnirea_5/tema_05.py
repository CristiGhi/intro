# ex_01 Functie care sa calculeze si sa returneze suma a 2 numere
def sum(a,b):
    return a+b
s1 = sum(7, 9)
s2 = sum (15, 35)
print (s1)
print (s2)
print('______________________________')

# ex_02 Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def par(nr):
    if nr % 2 == 0:
        return True
    else:
        return False
nr1 = par(8)
nr2 = par(9)

print(nr1)
print(nr2)
print('______________________________')

# ex_03 Functie care returneaza numarul total de caractere din numele tau complet. (nume, prenume, nume_mijlociu)
def  name(nume, prenume, nume_mijlociu):
    return f"Numele complet are {len(nume+prenume+nume_mijlociu)}"
nume = name('Ghiurco', 'Cristian', 'Mircea')
print(nume)
print('______________________________')

# ex_04 Functie care returneaza aria dreptunghiului
def aria(lungime, latime):
    return lungime * latime
aria_dreptunghiului = aria(10,5)
print(aria_dreptunghiului)
print('______________________________')

# ex_05 Functie care returneaza aria cercului
def aria_cercului(raza, pi=3.14):
    return pi*raza*raza
cerc = aria_cercului(7)
print(cerc)
print('______________________________')

# ex_06 Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
# caracter = input('Introduceti un caracter: ')
# def char(string):
#     if caracter  and caracter.upper() in string:
#         return True
#     else:
#         return False
# cuvant = char('Tema_05')
# print(cuvant)
# print('______________________________')

# ex_07 Functie fara return, primeste un string si printeaza pe ecran:
# -	Nr de caractere lower case este x
# -	Nr de caractere upper case este y

def char_nr(str):
    min = 0
    maj = 0
    for x in str:
        if x.islower():
            min += 1
        elif x.isupper():
            maj += 1
    print(f'Numarul de caractere lower case este {min}')
    print(f'Numarul de caractere upper case este  {maj}')
char_nr('Bine ati venit la ITF !')
print('______________________________')

# ex_08 Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
def numPoz(nr):
    nrPoz = []
    for x in nr:
        if x >= 0:
            nrPoz.append(x)
    return nrPoz
print(numPoz([7, 6, -8, -1]))
print('______________________________')

# ex_09 Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# -	Primul numar x este mai mare decat al doilea nr y
# -	Al doilea nr y este mai mare decat primul nr x
# -	Numerele sunt egale.
def printeaza(x,y):
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea nr {y}")
    elif x <y:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}")
    else:
        print(f"Numarul {x} si {y} sunt egale")
printeaza(4,6)
print('______________________________')

# ex_10 Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
def nrSet(nr,setNr):
    if nr in setNr:
        print("nu am adaugat numarul in set. Acesta exista deja")
        return False
    else:
        print("am adaugat numarul nou in set")
        return True
nrSet(6,[1,2,3,4,5,])
print('______________________________')