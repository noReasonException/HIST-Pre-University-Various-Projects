#****************calc by stefanos stefanou
#************************** TEST 03
calc = input("θες να προσθέσεις [1],να αφαιρέσεις [2],να πολλ/σεις [3],να διερέσεις [4] ή να υψώσεις σε δύναμη??[5] ")
data1 = input("δωσε τον πρώτο αριθμό ")
data2 = input("δωσε τον δέυτερο αριθμό")
add = 1
rem = 2
mul = 3
div = 4
potn = 5
if calc == add:
    print data1 + data2
if calc == rem:
    print data1 - data2
if calc == mul:
    print data1 * data2
if calc == div:
 if data1 > data2:
    print data1 / data2
if data1 < data2:
    print "first input smaller than second input"
if calc == potn:
    print data1 ** data2


    
