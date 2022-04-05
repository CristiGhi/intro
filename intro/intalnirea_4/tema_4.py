# ex_01 Avand lista
# a)	Folositi un for ca sa iterati prin toata lista si sa afisati  ‘Masina mea preferata este x’
# b)	Faceti acelasi lucru cu range-ul listei
# c)	Faceti acelasi lucru cu un while
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for elem in masini:
    print(f'Masina mea preferata este {elem}')
print('_______________________________________')
for x in range(len(masini)):
    print(f'Masina mea preferata este {masini[x]}')
print('_______________________________________')

x=len(masini)
a=0
while x>0:
    print(f'Masina mea preferata este {masini[a]}')
    a+=1
    x-=1
print('_______________________________________')

# ex_02 Aceeasi lista
# Folositi un for else
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# In else
#    Printati lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in range(1, len(masini) - 1):
    masini[masina] =masini[masina].upper()
else:
    print(masini)
print('_______________________________________')

# ex_03 Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel (else apartine de if, nu de for)
#    Printam Am gasit masina X. Mai cautam
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for elem in masini:
    if elem=='Mercedes':
        print('am gasit masina dorita de dvs')
        break
    else:
        print(f'am gasit masina {elem} .Mai cautam')
print('_______________________________________')

# ex_04 Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x
for elem in masini:
    if elem=='Trabant' or elem=='Lastun':
        continue
    else:
        print(f'S-ar putea sa va placa masina {elem}')
print('_______________________________________')

# ex_05 Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# -	Salvati aceste masini in masini_vechi
# -	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
masini_vechi=[]
for elem in masini:
    if elem == 'Trabant' or elem == 'Lastun':
        masini_vechi.append(elem)
        masini[masini.index(elem)]='Tesla'
print(masini_vechi)
print(masini)
print('_______________________________________')

# ex_06 Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
# Iterati prin lista
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for elem, pret in pret_masini.items():
    if pret <= 15000:
        print(elem, pret)
        print(f'Pentru un buget de sub 15000 euro puteti alege masina {elem}')
print('_______________________________________')

# ex_07 Avand lista; Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
n = 0
for elem in numere:
    if elem == 3:
       n = n+1
print(f'3 apare de {n} ori')
print('_______________________________________')

# ex_08 Aceeasi lista; Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)
n=0
for elem in numere:
    n+=elem
print(f'suma numerelor este {n}')
print('_______________________________________')

# ex_09 Aceeasi lista; Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
n=numere[0]
for elem in numere:
    if elem > n:
        n=elem
print(f'cel mai mare numar este {n}')
print('_______________________________________')

# ex_10 Aceeasi lista; Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
n = []
for elem in numere:
    if elem > 0:
        elem = -elem
        n.append(elem)
print(n)
print('_______________________________________')

# ex_11 # Iterati prin lista alte_numere
# # Populati corect celelalte liste
# # Afisati cele 4 liste la final
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for elem in alte_numere:
    if elem % 2 == 0:
        numere_pare.append(elem)
    if elem % 2 != 0:
        numere_impare.append(elem)
    if elem >0:
        numere_pozitive.append(elem)
    else:
        numere_negative.append(elem)
print(f'numere pare : {numere_pare}')
print(f'numere impare : {numere_impare}')
print(f'numere pozitive : {numere_pozitive}')
print(f'numere negative : {numere_negative}')
print('_______________________________________')

# ex_12 Aceeasi lista; Ordonati crescator lista fara sa folositi sort
