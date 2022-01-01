#****************calc by stefanos stefanou
#************************** TEST 02
calc = input("θες να προσθέσεις [1] ή να αφαιρέσεις [2] να πολλ/σεις [3] ή να διερέσεις [4]")
data1 = input("δωσε εναν αριθμο ")
data2 = input("δωσε δέυτερο αριθμο ")
add = 1
rem = 2
mul = 3
div = 4
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
    
