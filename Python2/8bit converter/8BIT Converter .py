# -*- coding: cp1253 -*-
import os
os.system("Title 8BITcoverter by El Sonador")
os.system("color 0A")
os.system("cls")
b1 = "0"
b2 = "0"
b4 = "0"
b8 = "0"
b16 = "0"
b32 = "0"
b64 = "0"
b128 = "0"
Number_List = [128,64,32,16,8,4,2,1]
def Draw_Window():#εκτύπωση παραθύρου
    os.system("cls")
    print "+-------------------------------+"
    print "The 8BIT Converter by El_Sonador+"
    print "Version 1.0			+"
    print "+-------------------------------+"
    print ""
    print Number_List
    print "  ",b128," ",b64," ",b32," ",b16,"",b8,"",b4,"",b2,"",b1
    print ""
def Convert_into_():#συνάρτηση που ελένχει πιος αριθμός χρησιμοποιείται και τον αθροίζει στο συνολικό αποτέλεσμα
    Result = 0
    if b1 == "1":
        Result = Result + 1
    if b2 == "1":
        Result = Result + 2
    if b4 == "1":
        Result = Result + 4
    if b8 == "1":
        Result = Result + 8
    if b16 == "1":
        Result = Result + 16
    if b32 == "1":
        Result = Result + 32
    if b64 == "1":
        Result = Result + 64
    if b128 == "1":
        Result = Result + 128
    print "The Result is :",Result
while True:
    try:
        Draw_Window()
        bits = raw_input("Please Input a 8bit number ")
        if bits[0] == "0" or bits[0] == "1":
            b1 = bits[0]
        if bits[1] == "0" or bits[1] == "1":
            b2 = bits[1]
        if bits[2] == "0" or bits[2] == "1":
            b4 = bits[2]
        if bits[3] == "0" or bits[3] == "1":
            b8 = bits[3]
        if bits[4] == "0" or bits[4] == "1":
            b16 = bits[4]
        if bits[5] == "0" or bits[5] == "1":
            b32 = bits[5]
        if bits[6] == "0" or bits[6] == "1":
            b64 = bits[6]
        if bits[7] == "0" or bits[7] == "1":
            b128 = bits[7]
        Draw_Window()
        Convert_into_()
        print "Press any key to continue"
        os.system("pause >nul")
    except:
        continue
    else:
        pass
    

