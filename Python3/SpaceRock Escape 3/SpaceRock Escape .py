import os
import time
import random
#χρώμα γραμμάτων
os.system("color E")
#εκκίνηση του cockpit.py
os.system("start cockpit.py")
#δήλωση λιστών
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
#καθαρισμός λιστων
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
#γέμισμα λιστών
def fullmap ():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9
    for full in range(11):
        x1.append("      ")
        x2.append("      ")
        x3.append("      ")
        x4.append("      ")
        x5.append("      ")
        x6.append("      ")
        x7.append("      ")
        x8.append("      ")
        x9.append("      ")
#εκτυπωση χάρτη
def printmap():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,points,shoots,lives,destroy
    print ("""
____ ___  ____ ____ ____ ____ ____ ____ _  _    ____ ____ ____ ____ ___  ____ 
[__  |__] |__| |    |___ |__/ |  | |    |_/     |___ [__  |    |__| |__] |___ 
___] |    |  | |___ |___ |  \ |__| |___ | \_    |___ ___] |___ |  | |    |___ 
                                                                              
""")
    print("Points :" + str(points))
    print("Shoots :" + str(shoots))
    print("Destroyed Asteroids :" + str(destroy))
    print("Lives :" + str(lives))
    print("+------------------------------------------------------------------------------+")
    print(x1[0]+x1[1]+x1[2]+x1[3]+x1[4]+x1[5]+x1[6]+x1[7]+x1[8]+x1[9])
    print(x2[0]+x2[1]+x2[2]+x2[3]+x2[4]+x2[5]+x2[6]+x2[7]+x2[8]+x2[9])
    print(x3[0]+x3[1]+x3[2]+x3[3]+x3[4]+x3[5]+x3[6]+x3[7]+x3[8]+x3[9])
    print(x4[0]+x4[1]+x4[2]+x4[3]+x4[4]+x4[5]+x4[6]+x4[7]+x4[8]+x4[9])
    print(x5[0]+x5[1]+x5[2]+x5[3]+x5[4]+x5[5]+x5[6]+x5[7]+x5[8]+x5[9])
    print(x6[0]+x6[1]+x6[2]+x6[3]+x6[4]+x6[5]+x6[6]+x6[7]+x6[8]+x6[9])
    print(x7[0]+x7[1]+x7[2]+x7[3]+x7[4]+x7[5]+x7[6]+x7[7]+x7[8]+x7[9])
    print(x8[0]+x8[1]+x8[2]+x8[3]+x8[4]+x8[5]+x8[6]+x8[7]+x8[8]+x8[9])
    print(x9[0]+x9[1]+x9[2]+x9[3]+x9[4]+x9[5]+x9[6]+x9[7]+x9[8]+x9[9])
    print("+------------------------------------------------------------------------------+")

                    
#αποτυπωση χάρτη
def navigatemap(x,y,obj):
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,points
    if (x == 1):
        x1[y] = obj
    if (x == 2):
        x2[y] = obj
    if (x == 3):
        x3[y] = obj
    if (x == 4):
        x4[y] = obj
    if (x == 5):
        x5[y] = obj
    if (x == 6):
        x6[y] = obj
    if (x == 7):
        x7[y] = obj
    if (x == 8):
        x8[y] = obj
    if (x == 9):
        x9[y] = obj
#συναρτηση startup
def startup():
    os.system("cls")
    print("""







                              +-+-+
                              |w e|
                              +-+-+

""")
    time.sleep(1)
    os.system("cls")
    print ("""







                              +-+-+-+-+
                              |w e l c|
                              +-+-+-+-+

""")
    time.sleep(1)
    os.system("cls")
    print("""







                              +-+-+-+-+-+-+-+ 
                              |w e l c o m e| 
                              +-+-+-+-+-+-+-+ 

""")
    time.sleep(1)
    os.system("cls")
    print("""







                              +-+-+-+-+-+-+-+ +-+-+-+
                              |w e l c o m e| |t o !|
                              +-+-+-+-+-+-+-+ +-+-+-+
""")
    time.sleep(1)
    menu()

#συναρτηση Game over    
def gameover():
    global points,shoots,lives
    os.system("cls")
    os.system("color FC")
    print ("""


   _____                         ____                 _ 
  / ____|                       / __ \               | |
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)
                                                        
                                                        
""")
    
    time.sleep(1)
    os.system("cls")
    os.system("color B")
    print ("""


   _____                         ____                 _ 
  / ____|                       / __ \               | |
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)
                                                        
                                                        
""")
    time.sleep(1)
    os.system("cls")
    os.system("color EC")
    print ("""


   _____                         ____                 _ 
  / ____|                       / __ \               | |
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)
                                                        
                                                        
""")
    time.sleep(1)
    os.system("cls")
    os.system("color E")
    print ("""


   _____                         ____                 _ 
  / ____|                       / __ \               | |
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)
                                                        
                                                        
    Total Points :""" + str(points))
    time.sleep(5)
    os.system("cls")
    menu()
#συναρτησεις μενου
def howto():
    os.system("cls")
    print ("""
                  +---------------------------------------------+
                  |You Trying to escape from rock using the     |
                  |UP,DOWN,FRONT,BACK buttons.You can Destroy   |
                  |Rock if you shoot it with Fire Button!       |
                  |                              Good Luck ;)   |
                  +---------------------------------------------+
""")
    wait = input("Press any key to continue")
    menu()
def info():
    os.system("cls")
    print ("""

                  +---------------------------------------------+
                  |              SpaceRock Escape               |
                  |Last Version 3.0                             |
                  +----------Info-------------------------------+
                  |Date :15/4/2014                              |
                  |Programming Language : Python and Tkinter    |
                  |Written by Stefanos Stefanou                 |
                  |For non-commercial use 2014                  |
                  +---------------------------------------------+
""")
    wait = input("Press any key to continue")
    menu()


def my_exit():
    os.system("cls")
    print("""

                  +---------------------------------------------+
                  |Thanks For Playing :)                        |
                  +---------------------------------------------+
""")
    wait = input("Press any key to continue")
    exit()

def menu():
    #χρώμα γραμμάτων
    os.system("color E")
    os.system("cls")
    print ("""
 ____ ___  ____ ____ ____ ____ ____ ____ _  _    ____ ____ ____ ____ ___  ____ 
 [__  |__] |__| |    |___ |__/ |  | |    |_/     |___ [__  |    |__| |__] |___ 
 ___] |    |  | |___ |___ |  \ |__| |___ | \_    |___ ___] |___ |  | |    |___ 
                                                                              


                                                                  Version 3.0!
                         ~Menu Choices 
                   +-----------------------------------------+
                   |1)Play Game                              |
                   |2)How to Play                            |
                   |3)Credits                                |
                   |4)Exit                                   |
                   +-----------------------------------------+

""")
    ask = input("What is your choice? ")
    if (ask == "1"):
        playgame()
    if (ask == "2"):
        howto()
    if (ask == "3"):
        info()
    if (ask == "4"):
        my_exit()
        
    
def playgame():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,points,shoots,lives,destroy
    #Ζωές
    lives = 3
    #βολές
    shoots = 0
    #ποντοι
    points = 0
    #Επιτυχείς βολές
    destroy = 0
    #τοποθεσία Διαστημοπλοίου
    xship = 5
    yship = 2
    #Τοποθεσια αστεροιδη 1
    x1rock = 5
    y1rock = 9
    #Τοποθεσια αστεροιδη 2
    x2rock = 5
    y2rock = 8
    #Τοποθεσια αστεροιδη 3
    x3rock = 5
    y3rock = 7
    #Τοποθεσία Σφαίρας
    xbullet = xship
    ybullet = yship + 1
    #Υπάρξη αστεροιδη 1, 2 , 3 [ True υπάρχει,False δεν υπάρχει]
    rock1 = True
    rock2 = True
    rock3 = True 
    #Υπάρξη Σφαίρας [ 0 δεν υπάρχει,1 υπάρχει]
    bullet = 0
    #Αρχικοποιηση τιμών στα αρχεία
    with open("movesx.txt" , "w") as writex:
        writex.write(str(xship))
    with open("movesy.txt" , "w") as writey:
        writey.write(str(yship))
    with open("FIRE.txt" , "w" ) as writebullet:
        writebullet.write(str(bullet))
    while True:
        
        #Αυξηση Πόντων
        points = points + 1
        #καρε
        time.sleep(0.5)
        #καθαρισμός παραθυρου
        os.system("cls")
        #Καθαρισμός λιστών
        clearmap()
        #Φόρτωση Λιστών
        fullmap()
        #Διάβασμα θέσης διαστημοπλοιου
        with open("movesx.txt" , "r") as readx:
            xship = int(readx.read())
        with open("movesy.txt" , "r") as ready:
            yship = int(ready.read())
        #Αποτύπωση Χαρακτήρα  
        navigatemap(xship,yship,">-")
        #Μηχανισμός αστεροιδή 1
        if (rock1 == True):
            y1rock = y1rock - 1
            navigatemap(x1rock,y1rock,"@")
            if (y1rock <= 0):
                rock1 = False
        if (rock1 == False):
            y1rock = 9
            x1rock = random.randint(1,8)
            rock1 = True
        #Μηχανισμός Αστεροιδή 2
        if (points > 60):
            if (rock2 == True):
                y2rock = y2rock - 1
                navigatemap(x2rock,y2rock,"@")
                if (y2rock <= 0):
                    rock2 = False
            if (rock2 == False):
                y2rock = 9
                x2rock = random.randint(1,8)
                rock2 = True
        #Μηχανισμός Αστεροιδή 3
        if (points > 110):
            if (rock3 == True):
                y3rock = y3rock - 1
                navigatemap(x3rock,y3rock,"@")
                if (y3rock <= 0):
                    rock3 = False
            if (rock3 == False):
                y3rock = 9
                x3rock = random.randint(1,8)
                rock3 = True
        #μηχανισμός Σφαίρας
        with open("FIRE.txt" , "r") as readfire:
            try:
                #Αν ειναι κενό...
                bullet = int(readfire.read())
            except:
                #εγραφεται η τιμη 0
                bullet = 0
        #Αν η σφαιρα ειναι 1[σημαινει οτι ο παιχτεις εχει ηδη πυροβολησει]
        if (bullet == 1):
            #το y μειωνεται
            ybullet = ybullet + 1
            #αποτυπωση
            navigatemap(xbullet,ybullet,"-")
            #αν βρισκεται στα ορια πιστας
        if (ybullet >= 8): 
            #Σφαιρα εξαφανιζεται
            bullet = 0
            #Και οι βολές αυξανονται
            shoots = shoots + 1
            #Ανίχνευση Σύγρουσης με αστεροιδη 1[σφαιρα - πετρα]
        if  ((ybullet -1 == y1rock) and (xbullet == x1rock)):
            #αστεροιδης εκτος
            rock1 = False
            #Και οι κατεστραμένες πέτρες επίσης
            destroy = destroy + 1
            #Ανίχνευση Σύγρουσης με αστεροιδη 2[σφαιρα - πετρα]
        if  ((ybullet -1 == y2rock) and (xbullet == x2rock)):
            #αστεροιδης εκτος
            rock2 = False
            #Και οι κατεστραμένες πέτρες επίσης
            destroy = destroy + 1
            #Ανίχνευση Σύγρουσης με αστεροιδη 3[σφαιρα - πετρα]
        if  ((ybullet -1 == y3rock) and (xbullet == x3rock)):
            #αστεροιδης εκτος
            rock3 = False
            #Και οι κατεστραμένες πέτρες επίσης
            destroy = destroy + 1
            #αν η bullet ειναι != 1
        if (bullet != 1):
            #εγραφη τιμης 0
            with open("FIRE.txt","w") as writefire:
                writefire.write("0")
                #αποδοση νεας τοποθεσιας διαστημοπλοιου στις μεταβλητες σε περιπτωση που θελει να πυροβολησει
                xbullet = xship
                ybullet = yship + 1
         #Μειωση Ζωής
         #συγρουση με αστεροιδη 1 [διαστημοπλοιο - πετρα]
        if (yship == y1rock) and (xship == x1rock):
            lives = lives - 1
            rock1 = False
         #συγρουση με αστεροιδη 2[διαστημοπλοιο - πετρα]
        if (yship == y2rock) and (xship == x2rock):
            lives = lives - 1
            rock2 = False
        #συγρουση με αστεροιδη 3[διαστημοπλοιο - πετρα]
        if (yship == y3rock) and (xship == x3rock):
            lives = lives - 1
            rock3 = False
         #Τέλος παιχνιδίου     
        if (lives == -1):
            gameover()
         #εκτυπωση χαρτη 
        printmap()
        
#Εκκίνηση Κεντρικης Συνάρτησης
startup()







    

    
