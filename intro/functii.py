#functie(metoda)=logiva delimitata care poate fi refolositao #
#functie simpla care ne prinreaza ceva pe ecran si nu returneaza nici un raspuns
#nu are parametri
#nu putem folosi spatii in nume
#nu putem defini o functie in alta functie

def printGreeting():
    print ('Buna ziua! Bine ati venit !')

def printGreetingByName(nume,prenume):
    print(f'Buna ziua {nume} {prenume} !')

def mediaNr(a, b, c):
    return(a+b+c)/3

def piValue():
    return 3.14


#exercitiu
#daca pers e majora , altfel False
def verificareMajor(varsta):
    if varsta>=18:
        return True
    else:
        return False






#zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('Ghiurco', 'Cristian')
printGreetingByName('Ghiurco', 'Ramona')
printGreetingByName('Ghiurco', 'Melissa')
print(mediaNr(3,4,3))
print(piValue())

print(verificareMajor(18))

#se ia varsta utilizatorului
age= int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat, bine ai venit in aplicatie')
else:
    print('nu ai varsta minima necesara(18) pt a paria ')
