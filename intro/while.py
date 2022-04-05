#while-loop, ciclu repetitiv
#zona de cod care se repeta atat timp cat o conditie e True
# problema: masina merge cat timp inaca are benzina
litri_benzina=10
while litri_benzina>0:
    #accelaram
    print('Vruum Vruum')
    #scadem benzina
    litri_benzina=litri_benzina-1
    if litri_benzina<=3:
        print('beculetul rosu')
print('STOP !')