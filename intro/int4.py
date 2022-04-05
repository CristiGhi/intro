# # Given the lists: lst1 = ["Black", "White", "Red"] and lst2 = ["Red", "Green"].
# # What do I write to get: "Black", "White" ? Using some relation between the 2 lists
# lst1 = ["Black", "White", "Red"]
# lst2 = ["Red", "Green"]
#
# print(set(lst1) - set(lst2))
#
#
# # Remove the duplicates from this list please! lst = [1,2,3,3,1,1,4,5,5] => [1,2,3,4,5]
# lst = [1,2,3,3,1,1,4,5,5]
# lst_n = []
# for n in lst:
#     if n not in lst_n:
#         lst_n.append(n)
# print(lst_n)
# print(s)
# print(list(set(lst)))


# Sa da o lista cu nume names_list = ["Valentina", "Raluca", Cristian", "Arthur", "Vlad", "Florina", "Dan", "Tudor", "Gabi"].
# Iterati lista, verificati daca numele incepe cu litera 'V', in caz afirmativ, sariti peste numele respectiv.
# In caz contrar afisati o structura de date formata din nume si indexul din lista unde a fost intalnit.

# names_list = ["Valentina", "Raluca", "Cristian", "Arthur", "Vlad", "Florina", "Dan", "Tudor", "Gabi"]
# # V1
# for nume in names_list:
#     if nume[0] == "V":
#         continue
#     print(nume, names_list.index(nume))
# #V2
# for idx_nume, nume in enumerate(names_list):
#     if nume[0] == "V":
#         continue
#     print(nume, idx_nume)
#
# Se dau 2 numere naturale a si b introduse de la tastatura, cu proprietatea ca a<b.
# Sa se construiasca lista formata din numerele din intervalul [a,b] care sunt divizibile fie cu 3 fie cu 17.
# Daca se gaseste un numar care este divizibil cu ambele, se intrerupe executia programului.
# Daca se ajunge la capatul intervalului se afiseaza mesajul "Ati ajuns la finalul intervalului" (folositi`va de conditia invatata adineaori)
#
# a = int(input('Introduceti inceputul intervalului'))
# b = int(input('Introduceti sfarsitul intervalului'))
# lst_nr = []
# for nr in range(a,b):
#     if (nr % 3 == 0) and (nr % 17 == 0):
#         break
#     elif (nr % 3 == 0) or (nr % 17 == 0):
#         lst_nr.append(nr)
# else:
#     print('Ati ajuns la finalul intervalului')
# print (lst_nr)
#
# # Se da un numar n=15, scrieti o bucla care printeaza numarul si il decrementeaza
# # pana cand acesta atinge 0. Decrementarea se face astfel:
# # - cu 2 daca numarul e divizibil cu 5;
# # - cu 3 daca e numar par;
# # - cu 1 daca e numar impar.
#
# n = 15
# while n>0 :
#     print(n)
#     if n % 5 == 0:
#         n -=2
#     elif n % 2 ==0:
#         n -=3
#     else:
#         n-=1


# Print all the natural numbers lower than a keyboard inputed one. If the number is not natural, raise an exception!
# Test with 15 then test with 'qwe'
a = int(input('introdu nr'))
for nr in range(a):
if a


