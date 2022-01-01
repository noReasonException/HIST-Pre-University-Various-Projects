import time
import sys
import os
v = ["       ","       ","       ","       ","       ","       ","       ","       ","       "]
def ResetV():
#Reser Positions 
    v[0] = "       "
    v[1] = "       "
    v[2] = "       "
    v[3] = "       "
    v[4] = "       "
    v[5] = "       "
    v[6] = "       "
    v[7] = "       "
    v[8] = "       "
def DrawWindow():
#DrawFrame with cls and re-Draw...
    os.system("cls")
    print """
+------------------------------------------------------------------------------+
The Triliza Game
Player 1 plays with charater X
Player 2 plays with charater O
For exit press 'EXIT'
"""
    print "  A         B           C     "
    print "        |       |"
    print "1"+v[0]+"|" +v[1]+ "|" +v[2]
    print "----------------------------"
    print "2"+v[3]+"|" +v[4]+ "|" +v[5]
    print "----------------------------"
    print "3"+v[6]+"|"+ v[7]+ "|" +v[8]
    print "        |       |"
        
def VictoryX():
    time.sleep(0.5)
    os.system("cls")
    print"""
.______    __           ___   ____    ____
|   _  \  |  |         /   \  \   \  /   /
|  |_)  | |  |        /  ^  \  \   \/   /
|   ___/  |  |       /  /_\  \  \_    _/
|  |      |  `----. /  _____  \   |  |
| _|      |_______|/__/     \__\  |__|
"""
    time.sleep(0.5)
    os.system("cls")
    print """
.______    __           ___   ____    ____  _______ .______          __  
|   _  \  |  |         /   \  \   \  /   / |   ____||   _  \        /_ | 
|  |_)  | |  |        /  ^  \  \   \/   /  |  |__   |  |_)  |        | | 
|   ___/  |  |       /  /_\  \  \_    _/   |   __|  |      /         | | 
|  |      |  `----. /  _____  \   |  |     |  |____ |  |\  \----.    | | 
| _|      |_______|/__/     \__\  |__|     |_______|| _| `._____|    |_|                                  
"""
    time.sleep(2)
    os.system("cls")
    os.system("color 0F")
    print """
____    __    ____  __  .__   __.      _______.
\   \  /  \  /   / |  | |  \ |  |     /       |
 \   \/    \/   /  |  | |   \|  |    |   (----`
  \            /   |  | |  . `  |     \   \    
   \    /\    /    |  | |  |\   | .----)   |   
    \__/  \__/     |__| |__| \__| |_______/    
                                               
"""
    time.sleep(1)
    os.system("cls")
    os.system("color F0")
    print """
____    __    ____  __  .__   __.      _______.
\   \  /  \  /   / |  | |  \ |  |     /       |
 \   \/    \/   /  |  | |   \|  |    |   (----`
  \            /   |  | |  . `  |     \   \    
   \    /\    /    |  | |  |\   | .----)   |   
    \__/  \__/     |__| |__| \__| |_______/    
                                               
                                                                  
"""
    time.sleep(1)
    os.system("cls")
    os.system("color 0F")
    print """
____    __    ____  __  .__   __.      _______.
\   \  /  \  /   / |  | |  \ |  |     /       |
 \   \/    \/   /  |  | |   \|  |    |   (----`
  \            /   |  | |  . `  |     \   \    
   \    /\    /    |  | |  |\   | .----)   |   
    \__/  \__/     |__| |__| \__| |_______/    
                                               
                                                                  
"""
    time.sleep(1)
    os.system("cls")
    os.system("color F0")
    print """
____    __    ____  __  .__   __.      _______.
\   \  /  \  /   / |  | |  \ |  |     /       |
 \   \/    \/   /  |  | |   \|  |    |   (----`
  \            /   |  | |  . `  |     \   \    
   \    /\    /    |  | |  |\   | .----)   |   
    \__/  \__/     |__| |__| \__| |_______/    
                                               
"""
    DrawWindow()
    os.system("color 0E")
def VictoryO():
    time.sleep(0.5)
    os.system("cls")
    print"""
.______    __           ___   ____    ____
|   _  \  |  |         /   \  \   \  /   /
|  |_)  | |  |        /  ^  \  \   \/   /
|   ___/  |  |       /  /_\  \  \_    _/
|  |      |  `----. /  _____  \   |  |
| _|      |_______|/__/     \__\  |__|
"""
    time.sleep(0.5)
    os.system("cls")
    print """
.______    __           ___   ____    ____  _______ .______          ___   
|   _  \  |  |         /   \  \   \  /   / |   ____||   _  \        |__ \  
|  |_)  | |  |        /  ^  \  \   \/   /  |  |__   |  |_)  |          ) | 
|   ___/  |  |       /  /_\  \  \_    _/   |   __|  |      /          / /  
|  |      |  `----. /  _____  \   |  |     |  |____ |  |\  \----.    / /_  
| _|      |_______|/__/     \__\  |__|     |_______|| _| `._____|   |____| 
                                                                                                       
"""
    time.sleep(1)
    os.system("cls")
    os.system("color 0F")
    print """
____    __    ____  __  .__   __.      _______.
\   \  /  \  /   / |  | |  \ |  |     /       |
 \   \/    \/   /  |  | |   \|  |    |   (----`
  \            /   |  | |  . `  |     \   \    
   \    /\    /    |  | |  |\   | .----)   |   
    \__/  \__/     |__| |__| \__| |_______/    
                                               
"""
    time.sleep(1)
    os.system("cls")
    os.system("color F0")
    print """
____    __    ____  __  .__   __.      _______.
\   \  /  \  /   / |  | |  \ |  |     /       |
 \   \/    \/   /  |  | |   \|  |    |   (----`
  \            /   |  | |  . `  |     \   \    
   \    /\    /    |  | |  |\   | .----)   |   
    \__/  \__/     |__| |__| \__| |_______/    
                                               
                                                                  
"""
    time.sleep(1)
    os.system("cls")
    os.system("color 0F")
    print """
____    __    ____  __  .__   __.      _______.
\   \  /  \  /   / |  | |  \ |  |     /       |
 \   \/    \/   /  |  | |   \|  |    |   (----`
  \            /   |  | |  . `  |     \   \    
   \    /\    /    |  | |  |\   | .----)   |   
    \__/  \__/     |__| |__| \__| |_______/    
                                               
                                                                  
"""
    time.sleep(1)
    os.system("cls")
    os.system("color F0")
    print """
____    __    ____  __  .__   __.      _______.
\   \  /  \  /   / |  | |  \ |  |     /       |
 \   \/    \/   /  |  | |   \|  |    |   (----`
  \            /   |  | |  . `  |     \   \    
   \    /\    /    |  | |  |\   | .----)   |   
    \__/  \__/     |__| |__| \__| |_______/    
                                               
"""
    DrawWindow()
    os.system("color 0E") 
                                                     
def Win():
#Player1 Rules
    if v[0] == "   X   "  and  v[1] == "   X   " and  v[2] == "   X   ":
        VictoryX()
    if v[3] == "   X   "  and  v[4] == "   X   " and  v[5] == "   X   ":
        VictoryX()
    if v[6] == "   X   "  and  v[7] == "   X   " and  v[8] == "   X   ":
        VictoryX()
    if v[0] == "   X   "  and  v[3] == "   X   " and  v[6] == "   X   ":
        VictoryX()
    if v[1] == "   X   "  and  v[4] == "   X   " and  v[7] == "   X   ":
        VictoryX()
    if v[2] == "   X   "  and  v[5] == "   X   " and  v[8] == "   X   ":
        VictoryX()
    if v[0] == "   X   "  and  v[4] == "   X   " and  v[8] == "   X   ":
        VictoryX()
    if v[2] == "   X   "  and  v[4] == "   X   " and  v[6] == "   X   ":
        VictoryX()
#Player2 Rules
    if v[0] == "   O   "  and  v[1] == "   O   " and  v[2] == "   O   ":
        VictoryO()
    if v[3] == "   O   "  and  v[4] == "   O   " and  v[5] == "   O   ":
        VictoryO()
    if v[6] == "   O   "  and  v[7] == "   O   " and  v[8] == "   O   ":
        VictoryO()
    if v[0] == "   O   "  and  v[3] == "   O   " and  v[6] == "   O   ":
        VictoryO()
    if v[1] == "   O   "  and  v[4] == "   O   " and  v[7] == "   O   ":
        VictoryO()
    if v[2] == "   O   "  and  v[5] == "   O   " and  v[8] == "   O   ":
        VictoryO()
    if v[0] == "   O   "  and  v[4] == "   O   " and  v[8] == "   O   ":
        VictoryO()
    if v[2] == "   O   "  and  v[4] == "   O   " and  v[6] == "   O   ":
        VictoryO()
    
#Main Fuction    
def PlayGame():
    ResetV()
    def Mark(pos,char):
        v[pos] = "   "+char+"   "
        DrawWindow()
        Win()
    while True:
        DrawWindow()
        MoveX = raw_input("Player 1 Move ~ ")
        if MoveX == "A1" and v[0] =="       ":
            Mark(0,"X")
        if MoveX == "A2" and v[3] =="       ":
            Mark(3,"X")
        if MoveX == "A3" and v[6] =="       ":
            Mark(6,"X")
        if MoveX == "B1" and v[1] =="       ":
            Mark(1,"X")
        if MoveX == "B2" and v[4] =="       ":
            Mark(4,"X")
        if MoveX == "B3" and v[7] =="       ":
            Mark(7,"X")
        if MoveX == "C1" and v[2] =="       ":
            Mark(2,"X")
        if MoveX == "C2" and v[5] =="       ":
            Mark(5,"X")
        if MoveX == "C3" and v[8] =="       ":
            Mark(8,"X")
        if MoveX =="EXIT":
            break
        else:
            pass
        MoveO = raw_input("Player 2 Move ~ ")
        if MoveO == "A1" and v[0] =="       ":
            Mark(0,"O")
        if MoveO == "A2" and v[3] =="       ":
            Mark(3,"O")
        if MoveO == "A3" and v[6] =="       ":
            Mark(6,"O")
        if MoveO == "B1" and v[1] =="       ":
            Mark(1,"O")
        if MoveO == "B2" and v[4] =="       ":
            Mark(4,"O")
        if MoveO == "B3" and v[7] =="       ":
            Mark(7,"O")
        if MoveO == "C1" and v[2] =="       ":
            Mark(2,"O")
        if MoveO == "C2" and v[5] =="       ":
            Mark(5,"O")
        if MoveO == "C3" and v[8] =="       ":
            Mark(8,"O")
        if MoveO =="EXIT":
            break
        else:
            pass
        
        
        
        
    
#Frames(On StartUp)    
os.system("color 0E")
print """
+-+-+-+
|W|e|l| 
+-+-+-+
"""
time.sleep(0.5)
os.system("cls")
print """
+-+-+-+-+-+
|W|e|l|c|o|
+-+-+-+-+-+
"""
time.sleep(0.5)
os.system("cls")
print """
+-+-+-+-+-+-+-+ +-+-+
|W|e|l|c|o|m|e| |t|o|
+-+-+-+-+-+-+-+ +-+-+
"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
1)Play Triliza

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
            1)Play Triliza

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
2)How to play

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
          2)How to play

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
                          2)How to play

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
                          2)How to play
3)Credits

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
                          2)How to play
            3)Credits

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
                          2)How to play
                          3)Credits

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
                          2)How to play
                          3)Credits
4)Exit

"""
time.sleep(0.5)
os.system("cls")
print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
                          2)How to play
                          3)Credits
            4)Exit

"""
#Main Menu Loop
while True:
    time.sleep(0.5)
    os.system("cls")
    print """
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||       |||T |||r |||i |||l |||i |||z |||a ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||g |||a |||m |||e ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|
                                        Coded By El_Sonador
                           MAIN MENU
                          1)Play Triliza
                          2)How to play
                          3)Credits
                          4)Exit

"""
    Choice = raw_input("Enter Your Choice ~ ")
    if Choice =="1":
        PlayGame()
    if Choice =="2":
        os.system("cls")
        print """
        +--------------------How To Play----------------------------------+
        |Triliza is a  strategy game .. the only thing you can do is to   |
        |form a 3 x or 3 o in the series blocking the opponent to do      |
        |this to you .... Usually the motion of a round does not exceed   |
        |4 So in 4 moves must find ways to unlock your opponent ...       |
        +-----------------------------------------------------------------+
                         Press Any Key to continue.... 
"""
        os.system("pause>nul")
        time.sleep(0.05)
        os.system("cls")
    if Choice =="3":
        os.system("cls")
        print """
                    +---------Credits---------------+
                    |The Triliza Game               |
                    |Coded By El_Sonador            |
                    |Version 1.0                    |
                    +-------------------------------+
                       Press Any Key to continue
"""
        os.system("pause >nul") 
    if Choice =="4":
        os.system("cls")
        print """

                +---------Thank You----------------+
                |Thanks For Using The Triliza game |
                +----------------------------------+
                     Press Any Key to continue
"""
        os.system("pause>nul") 
        sys.exit()
        
    



