import os
import time
os.system("color E")
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []

def clearmap():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    x8 = []
    x9 = []

def fullmap ():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9
    for full in range(10):
        x1.append("      ")
        x2.append("      ")
        x3.append("      ")
        x4.append("      ")
        x5.append("      ")
        x6.append("      ")
        x7.append("      ")
        x8.append("      ")
        x9.append("      ")

def printmap():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9
    print(x1[0]+x1[1]+x1[2]+x1[3]+x1[4]+x1[5]+x1[6]+x1[7]+x1[8]+x1[9])
    print(x2[0]+x2[1]+x2[2]+x2[3]+x2[4]+x2[5]+x2[6]+x2[7]+x2[8]+x2[9])
    print(x3[0]+x3[1]+x3[2]+x3[3]+x3[4]+x3[5]+x3[6]+x3[7]+x3[8]+x3[9])
    print(x4[0]+x4[1]+x4[2]+x4[3]+x4[4]+x4[5]+x4[6]+x4[7]+x4[8]+x4[9])
    print(x5[0]+x5[1]+x5[2]+x5[3]+x5[4]+x5[5]+x5[6]+x5[7]+x5[8]+x5[9])
    print(x6[0]+x6[1]+x6[2]+x6[3]+x6[4]+x6[5]+x6[6]+x6[7]+x6[8]+x6[9])
    print(x7[0]+x7[1]+x7[2]+x7[3]+x7[4]+x7[5]+x7[6]+x7[7]+x7[8]+x7[9])
    print(x8[0]+x8[1]+x8[2]+x8[3]+x8[4]+x8[5]+x8[6]+x8[7]+x8[8]+x8[9])
    print(x9[0]+x9[1]+x9[2]+x9[3]+x9[4]+x9[5]+x9[6]+x9[7]+x9[8]+x9[9])

def navigatemap(x,y,obj):
    global x1,x2,x3,x4,x5,x6,x7,x8,x9
    if x == 1:
        x1[y] = obj
    if x == 2:
        x2[y] = obj
    if x == 3:
        x3[y] = obj
    if x == 4:
        x4[y] = obj
    if x == 5:
        x5[y] = obj
    if x == 6:
        x6[y] = obj
    if x == 7:
        x7[y] = obj
    if x == 8:
        x8[y] = obj
    if x == 9:
        x9[y] = obj

xship = 5
yship = 5

xrock = 5
yrock = 9


while True:
    time.sleep(0.2)
    os.system("cls")
    clearmap()
    fullmap()
    #ανιχνευση συγρουσης
    if y == yrock and x == xrock:
        x = input("GAME OVERRRRRRR :) ")
    #Αποτυπωση αντικειμένων
    navigatemap(x,y,"<-}")
    navigatemap(xrock,yrock,"@")
    #εκτυπωση χαρτη 
    printmap()
    






    

    
