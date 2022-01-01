
#****************calc by stefanos stefanou
#************************** TEST 05
from math import *
print """
        CCCCCCCCCCCCC lllllll                                  66666666   
     CCC::::::::::::C l:::::l                                 6::::::6    
   CC:::::::::::::::C l:::::l                                6::::::6     
  C:::::CCCCCCCC::::C l:::::l                               6::::::6      
 C:::::C       CCCCCC  l::::l     cccccccccccccccc         6::::::6       
C:::::C                l::::l   cc:::::::::::::::c        6::::::6        
C:::::C                l::::l  c:::::::::::::::::c       6::::::6         
C:::::C                l::::l c:::::::cccccc:::::c      6::::::::66666    
C:::::C                l::::l c::::::c     ccccccc     6::::::::::::::66  
C:::::C                l::::l c:::::c                  6::::::66666:::::6 
C:::::C                l::::l c:::::c                  6:::::6     6:::::6
 C:::::C       CCCCCC  l::::l c::::::c     ccccccc     6:::::6     6:::::6
  C:::::CCCCCCCC::::C l::::::lc:::::::cccccc:::::c     6::::::66666::::::6
   CC:::::::::::::::C l::::::l c:::::::::::::::::c      66:::::::::::::66 
     CCC::::::::::::C l::::::l  cc:::::::::::::::c        66:::::::::66   
        CCCCCCCCCCCCC llllllll    cccccccccccccccc          666666666
|\__________________________________________________________________________/|
|Καλωσωρίσατε στην αριθμομηχανή Calc 6	                                     |
|                                    Απο τον El_Sonador	                     |
|____________________________________________________________________________|
|Για προσθεση πιεστε το 1
|Για αφαίρεση πιεστε το 2
|Για πολλαπλασιασμό πιεστε το 3
|Για διαίρεση πιέστε το 4
|Για δύναμη πιέστε το 5
|Για ρίζα πίεστε το 6
"""
add = 1
rem = 2
mul = 3
div = 4
pon = 5
nun = 6 
while True:
    calc = input("Η επιλογή σας είναι η : ")
    if calc == nun:
        data1 = input("Εισάγετε τον αριθμό ~ ")
        res = sqrt(data1)
        print "Η Ρίζα είναι", res
    data1 = input("Εισάγετε τον πρώτο αριθμό ~ ")
    data2 = input("Εισάγετε τον δέυτερο αριθμό ~ ")
    if calc == add:
        res = data1 + data2
        print "Το αποτέλεσμα της πρόσθεσης ειναι", res
    if calc == rem:
        res = data1 - data2
        print "Το αποτέλεσμα της αφαίρεσης είναι", res
    if calc == mul:
        res = data1 * data2
        print "Το αποτέλεσμα του πολλαπλασιασμού είναι", res
    if calc == div:
     if data1 > data2:
       res = data1 / data2
       print "Το αποτέλεσμα της διαίρεσης είναι", res
       rem = data1 % data2
       print "Με υπόλοιπο διαίρεσης", rem
    if calc == div:
     if data1 == data2:
       res = data1 / data2
       print "Τo αποτέλεσμα της διαίρεσης είναι", res
       rem = data1 % data2
       print "Με υπόλοιπο διαίρεσης", rem
    if calc == pon:
        res = data1 ** data2
        print "Το αποτέλεσμα της δύναμης είναι",res
    if calc < add:
        print "Η επιλογή ",calc," δεν υφίσταται"
    if calc > nun:
        print "Η επιλογή ",calc," δεν υφίσταται"

     


    
