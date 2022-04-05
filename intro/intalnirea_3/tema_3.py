# ex_1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# a)	Afiseaz-o
# b)	Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# c)	Printeaza varianta actuala (inversata)
# d)	Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# e)	Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

note_muzicale1 = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale1)
note_muzicale2 = note_muzicale1[::-1]
print(note_muzicale2)
note_muzicale2.reverse()
print(note_muzicale2)

# ex_2 De cate ori apare ‘do’?
print(note_muzicale1.count('do'))

# ex_3 Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista
lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista = lista_1 + lista_2
print(lista)
lista_1.extend(lista_2)
print(lista_1)

# ex_4 Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista
lista.sort()
print(lista)
lista.remove(0)
print(lista)

# ex_5 Folosind un if verificati lista generata la ex3 si afisati
# -	Lista este goala
# -	Lista nu este goala
if len(lista) <= 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala')

# ex_6 Folositi o functie care sa stearga lista de la ex3
lista.clear()
print(lista)

# ex_7 Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala
if len(lista) <= 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala')

# ex_8 Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

# ex_9 Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")

# ex_10 Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare
dict1['Dorel'] = 6
print(dict1)

# ex_11 Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati dictionarul schimbat
dict1.pop('Gigel')
print(dict1)
dict1.update({'Ionica' : 9})
print(dict1)

# ex_12 Set # Adaugati in zilele_sapt ‘luni’  # # Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt |= {'luni'}
print(zile_sapt)     # in set nu se repeta elementul la printare

# ex_13 Folositi un if si verificati daca
# -	Weekend este un subset al zilelor din sapt
# -	Weekend nu este un subset al zilelor din sapt
if zile_sapt & weekend :
    print('Weekend este un subset al zilelor din sapt')
else:
    print('Weekend nu este un subset al zilelor din sapt')

# ex_14 Afisati diferentele dintre aceste 2 seturi (exercitiu 12)
print(zile_sapt - weekend)

# ex_15 Afisati intersectia elementelor din aceste 2 seturi (exercitiu 12)
print(zile_sapt & weekend)

# ex_16


# ex_17 Se da o lista cu nume de fructe: fruits = ["apple", "banana", "cherry", "kiwi", "mango"] . Returnati lista formata doar din fructele care contin litera ‘e’: ['apple', 'cherry'].


# ex_18 Folosindu`va de lista anterioara (fruits) returnati acele fructe care au exact 6 litere.

