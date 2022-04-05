from datetime import date

#ex_1.  Clasa Cerc
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()


class Cerc:
    raza = 1
    culoare = "verde"

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        print(f"{self.raza} {self.culoare}")

    def aria(self, raza):
        self.raza = raza
        return self.raza**2*3.14

    def diametru(self,raza):
        self.raza = raza
        return 2*self.raza*3.14


cerc_nou = Cerc(5,"negru")
print(cerc_nou.aria(1))
print(cerc_nou.diametru(1))
print("--------------------------")

# ex_2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie() va PRINTA lungime, latime, culoare
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().


class Dreptungi:
    lungime = 0
    latime = 0
    culoare = "alba"

    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f"Avem lungimea de {self.lungime}  cu latimea de {self.latime} si culoarea {self.culoare}")

    def aria(self,lungime,latime):
        self.lungime = lungime
        self.latime = latime
        formula = self.lungime * self.latime
        return formula

    def perimetru(self,lungime,latime):
        self.lungime = lungime
        self.latime = latime
        formula = 2 * self.lungime + 2 * self.latime
        return formula

    def schimba_culoarea(self,culoare):
        self.culoare = culoare
        return f"Ti-ai schimbat culoarea in {self.culoare}"


drept = Dreptungi(4,9,"galben")
print(drept.aria(4,6))
print(drept.perimetru(4,6))
print(drept.schimba_culoarea("albastru"))
print(drept.descriere())
print("--------------------------")

# ex_3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor() pt toate atributele // constructor reprezinta __init__
# Metode:
# descrie() print nume, prenume, salariu
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)


class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f" {self.nume}  {self.prenume} are salariul de {self.salariu}")

    def nume_complet(self,nume,prenume):
        self.nume = nume
        self.prenume = prenume
        formula = self.nume + " " + self.prenume
        return formula

    def salariu_lunar(self,salariu):
        self.salariu = salariu
        return self.salariu

    def salariu_anual(self):
        formula = self.salariu * 12
        return formula

    def marire_de_salariu(self,procent):
        self.procent = procent
        self.salariu = self.salariu + (self.salariu * procent / 100)
        return self.salariu

angajat1 = Angajat("Ghiurco","Cristi", 1000)
print(angajat1.nume_complet("Ghiurco", "Cristi"))
print(angajat1.descriere())
print(angajat1.marire_de_salariu(30))
print("--------------------------")

# ex_4. Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total “
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

class Factura:
    seria = "SER"
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        return f"Acum ai cantitatea de {self.cantitate}"

    def schimba_pretul(self, pret_buc):
        self.pret_buc = pret_buc
        return f"Noul tau pret este {self.pret_buc}"

    def schimba_nume_produs(self, nume_produs):
        self.nume_produs = nume_produs
        return f"Noul tau nume al produsului este {self.nume_produs}"

    def genereaza_factura(self):
        self.data = date.today()
        self.total = self.cantitate * self.pret_buc
        return f""" 
            Factura seria {self.seria} numar {self.numar}
                     {self.data}            
        Produs | cantitate  | pret bucata | Total 
         {self.nume_produs}|     {self.cantitate}    |      {self.pret_buc}      |  {self.total}"""


factura1 = Factura(125, "curent", 190, 6)
print(factura1.genereaza_factura())
print("--------------------------")

# 5. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)

class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self,iban,titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold


    def afisare_sold(self):
        return f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei"

    def debitare_cont(self, suma):
        self.suma = suma
        self.sold = self.sold + self.suma
        return f"Ai alimentat cu {self.suma} de lei"

    def creditare_cont(self,suma):
        self.suma = suma
        if self.suma <= self.sold:
            self.sold = self.sold - self.suma
            return f"A-ti retras suma de  {self.suma} de lei"
        else:
            return "Nu ai suficienti bani in cont"



cristi = Cont("RO7500", "Ghiurco Cristi",47000)
print(cristi.afisare_sold())
print(cristi.debitare_cont(20000))
print(cristi.afisare_sold())
print(cristi.creditare_cont(10000))
print(cristi.afisare_sold())
print("--------------------------")
