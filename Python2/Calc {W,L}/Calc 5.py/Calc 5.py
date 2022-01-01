#****************calc by stefanos stefanou
#************************** TEST 05
from math import *
print "********************************"
print "Πρόσθεση [1]                  *"
print "Αφαίρεση [2]                  *"
print "Πολλαπλασιασμός [3]           *"
print "Διαίρεση [4]                  *"
print "Δύναμη [5]                    *"
print "Ρίζα (του πρώτου αριθμού) [6] *"
print "********************************"
calc = input("επιλογή ~ ")
data1 = input("Εισάγετε τον πρώτο αριθμό ~ ")
data2 = input("Εισάγετε τον δέυτερο αριθμό ~ ")
add = 1
rem = 2
mul = 3
div = 4
pon = 5
nun = 6
if calc == add:
    print "Το αποτέλεσμα της πρόσθεσης ειναι", data1 + data2
if calc == rem:
    print "Το αποτέλεσμα της αφαίρεσης είναι", data1 - data2
if calc == mul:
    print "Το αποτέλεσμα του πολλαπλασιασμού είναι", data1 * data2
if calc == div:
 if data1 > data2:
   print "Το αποτέλεσμα της διαίρεσης είναι", data1 / data2
   print "Με υπόλοιπο διαίρεσης", data1 % data2
if calc == div:
 if data1 == data2:
   print "Το αποτέλεσμα της διαίρεσης είναι", data1 / data2
   print "Με αποτέλεσμα διαίρεσης", data1 % data2
if calc == pon:
    print "Το αποτέλεσμα της δύναμης είναι", data1 ** data2
if calc == nun:
    print "Η Ρίζα είναι", sqrt(data1)
if calc < add:
    print "η εντολή",calc,"δεν υφίσταται"
if calc > nun:
    print "η εντολή",calc,"δεν υφίσταται"

     


    
