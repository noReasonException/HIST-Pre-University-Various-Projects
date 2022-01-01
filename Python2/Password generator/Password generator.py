#password generator\
import time
import random
from random import randint
print "**********************************"
print " PASSWORD GENERATOR              *"
print "--------------------             *"
print "                 BY EL SONADOR   *"
print "                 --------------  *"
print "**********************************"
print "start generation ?? "
data = input("1 for yes or 2 for not ~ ")
choice1 = 1
choice2 = 2
password = random.randint( 10000000 , 100000000000 )
if data == choice1 :
 print "your password is " , password
 time.sleep(520)
if data == choice2 :
    print "thanks for using password generator by el sonador"
    time.sleep(5)
    

