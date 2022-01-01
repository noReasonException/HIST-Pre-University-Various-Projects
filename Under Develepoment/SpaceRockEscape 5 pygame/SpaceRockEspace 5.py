from pygame.locals import *
import random
import pygame
import time
import os

winsize = (1000,700) #μέγεθος παραθύρου
screen = pygame.display.set_mode(winsize,DOUBLEBUF,32)#δημιουργία κεντρικού αντικειμένου της pygame[video ]
pygame.display.set_caption("SpaceRockEscape Version 5.0")
#Φόρτωση Sprites
i1 = pygame.image.load("1.png")
i2 = pygame.image.load("2.png")
i3 = pygame.image.load("3.png")
i4 = pygame.image.load("4.png")
i5 = pygame.image.load("5.png")
i6 = pygame.image.load("6.png")
i7 = pygame.image.load("7.png")
i8 = pygame.image.load("8.png")
i9 = pygame.image.load("9.png")
i10 = pygame.image.load("10.png")
i11 = pygame.image.load("11.png")
i12 = pygame.image.load("12.png")
i13 = pygame.image.load("13.png")
i14 = pygame.image.load("14.png")
i15 = pygame.image.load("15.png")
i16 = pygame.image.load("16.png")
i17 = pygame.image.load("17.png")
bullet = pygame.image.load("bullet.png")
star = pygame.image.load("Star.png")
Rock = pygame.image.load("Rock.png")
RockSmash1 = pygame.image.load("Rock_Snash1.png")
RockSmash2 = pygame.image.load("Rock_Snash2.png")
RockSmash3 = pygame.image.load("Rock_Snash3.png")


global xspaceship
xspaceship = 500
global yspaceship
yspaceship = 350
global bulletx
bulletx = 50
global bullety
bullety = 50
global reload_cannon_counter
reload_cannon_counter = 0
#Κώδικας κίνησης Πληκρολογιου
"""
def move_keyboard():
    global x,y
    for check in pygame.event.get():
        pass
    check = pygame.key.get_pressed()
    if check[K_RIGHT]:
        x = x + 10
    if check[K_LEFT]:
        x = x - 10
    if check[K_UP]:
        y = y - 10
    if check[K_DOWN]:
        y = y + 10
"""
#Κωδικας κίνησης Controller
def move_Controller():
    global xspaceship , yspaceship #Δημόσιες x,y
    global reload_cannon_counter
    pygame.joystick.init() #Αρχικοποίηση της Joystick
    controller1 = pygame.joystick.Joystick(0) #Δημιουργια αντικειμένου controller1 για το Joystick με ID = 0
    controller1.init() #Αρχικοποίηση του controller1
    pygame.event.get() #Πάρε Γεγονότα 
    if int(controller1.get_button(3)) == 1: # Αν το button 3 γυρισει Status True
        xspaceship = xspaceship - 10 
    if int(controller1.get_button(1)) == 1: # Αν το button 1 γυρισει Status True
        xspaceship = xspaceship + 10
    if int(controller1.get_button(2)) == 1: #Αν το button 2 Γυρίσει Status True
        yspaceship = yspaceship + 10
    if int(controller1.get_button(8)) == 1: # Αν το button 8 Γυρισει Status True
        yspaceship = yspaceship - 10
    if int(controller1.get_button(7)) == 1:
        reload_cannon_counter = 0
def check_spaceship_inlevel():
    global xspaceship,yspaceship
    if xspaceship > 830:
        xspaceship = 830
    if xspaceship < 0:
        xspaceship = 0
    if yspaceship > 700:
        yspaceship = 0
    if yspaceship < 0:
        yspaceship = 700

#================================================================================Κωδικας Για Εκκίνηση Scrolling BackGround
def start_scrolling_BG():
    global dots_pin_x #Δημοσιος πινακας Dots_pin_x [Dots_pinakas_x (θεσεις x) ]
    dots_pin_x = []   #Δήλωση του ως κενού 
    global dots_pin_y #Δημόσιος Πίνακας Dots_pin_y[Dots_pinakas_y(θεσεις y ) ]
    dots_pin_y = []   #Δήλωση του ως κενού
    #Δημιουργία θέσεων
    for create in range(0,100): #Generate 0,100 
        dots_pin_x.append(0) #προσθηκη θεσης στο x
        dots_pin_y.append(0) # - \\ - \\ - στο y
    #Πέρασμα των πρώτων τυχαίων τοποθεσιών 
    for give_random_positions in range(0,100): #Generate 0 , 100
        dots_pin_x[give_random_positions] = random.randint(1,1000) # στο x δώσε απο 0 ως 1000
        dots_pin_y[give_random_positions] = random.randint(1,700) # στο y δώσε απο το 0 ως το 700 
#Κώδικας για συνέχιση του Scrolling Background        
def scrolling_BG_UPDATE():
    screen.fill((0,0,0)) # Μάυρο BackGround
    for dots_move in range(0,100): # Μετακίνηση των y κάθε Dot
        dots_pin_y[dots_move] = dots_pin_y[dots_move] + 1
    for check in range(0,100): #Ελενχος αν είναι στα όρια της πίστας και επαναπροσδιορισμος τυχαίων τοποθεσιών
        if dots_pin_x[check] < 0 or dots_pin_x[check] > 1000:
            dots_pin_x[check] = random.randint(1,1000)
        if dots_pin_y[check] < 0 or dots_pin_y[check] > 700:
            dots_pin_y[check] = random.randint(1,700)
    for draw in range(1,100): # Εκτύπωση Dots
        screen.blit(star,(dots_pin_x[draw] , dots_pin_y[draw]))
#=================================================================================Τέλος κώδικα για Scrolling Background
        
def StartRockAttack():
    global Rocky
    Rocky = -50
    global Rockx
    Rockx = []
    for Create_List_Pos in range(0,1):
        Rockx.append(0)
    for Give_First_Random_pos in range(0,1):
        Rockx[Give_First_Random_pos] = random.randint(1,1000)

def RockAttack_UPDATE():
    global Rocky
    global Rockx
    Rocky = Rocky + 1
    for Check_if_inlevel in range(0,1):
        if Rocky > 700 or Rocky < 0:
            Rocky = 0
            Rockx[Check_if_inlevel] = random.randint(1,700)
            
    for Draw_inlevel in range(0,1):
        screen.blit(Rock,(Rockx[Draw_inlevel],Rocky))
#==========================================================================Κώδικας ελένχου σύγρουσης και καταστροφής πέτρας
def Bullet_on_Rock():
    for detect_area in range(0,300):
        for rock_number in range(0,1):
            if bulletx == Rockx[rock_number] + detect_area and bullety == Rocky + detect_area:
                for destroy_rock in range(1,3):
                    scrolling_BG_UPDATE()
                    RockAttack_UPDATE()
                    move_Controller()
                    exec("screen.blit(RockSmash"+str(destroy_rock)+",(Rockx[rock_number],Rocky))")
                    screen.blit(i1,(xspaceship,yspaceship))
                    pygame.display.update()
                StartRockAttack()
def Spaceship_on_Rock():
    for detect_area in range(0,300):
        for rock_number in range(0,1):
            if xspaceship == Rockx[rock_number] + detect_area and yspaceship == Rocky + detect_area:
                print ("SpaceShip On Rock!")
#===============================================================================Κώδικας εκπυρσοκρότησης
def Fire_MainLoop():
    global reload_cannon_counter
    if reload_cannon_counter <= 120:
        reload_cannon_counter = reload_cannon_counter + 1
        global bulletx
        global bullety
        global xspaceship
        global yspaceship
        move_Controller() #κλήση της move_Controller
        bulletx = xspaceship + 90 #χ της σφαίρας ίδιο με του διαστημοπλοίου + 90 [ακριβώς πάνω απο το κανόνι]
        bullety = yspaceship      #y της σφαίρας ιδιο με του διαστημοπλοίου
        for i in range(1,17): #17 καρέ εκπυρσοκρότησης
            time.sleep(0.003)
            scrolling_BG_UPDATE() #κλήση της scrolling_BG_UPDATE
            RockAttack_UPDATE() #κληση της RockAttack_UPDATE
            bullety = bullety - 30 #μείωση του bullety κατα 20
            exec("screen.blit(i" + str(i) + ",(xspaceship,yspaceship))") # αποτύπωση διαστημοπλοίου
            screen.blit(bullet,(bulletx,bullety)) #αποτύπωση σφαίρας
            Bullet_on_Rock() #Κλήση της Bullet_on_Rock!
            Spaceship_on_Rock()
            show_bullet_remaining_UPDATE()
            pygame.display.update() #UPDATE του buffer
    
def Start_show_bullet_remaining():
    global thefont
    global reloading_message
    pygame.init()
    thefont = pygame.font.SysFont("Arial",25)
    reloading_message = thefont.render("Reload Cannon! [R2]",True,(255,255,255),(0,0,0))
def show_bullet_remaining_UPDATE():
    global thefont
    global reloading_message
    global reload_cannon_counter
    thebullets = thefont.render("Bullets >" + str(reload_cannon_counter) + "/121",True,(255,255,255),(0,0,0))
    screen.blit(thebullets,(0,0))
    if reload_cannon_counter == 121:
        screen.blit(reloading_message,(0,0))

        
start_scrolling_BG() #Κλήση της start_scrolling
StartRockAttack()    #Κλήση της  StartRockAttack
Start_show_bullet_remaining() #Κλήση της Start_show_bullet_remaining
#Κεντρικός Βρόνχος
while True:
    time.sleep(0.003)
    check_spaceship_inlevel()
    move_Controller()#Events Τηλεκοντρόλ για μετακίνηση
    scrolling_BG_UPDATE() #κλήση της scrolling_BG_UPDATE()
    RockAttack_UPDATE()#κλήση της RockAttack_UPDATE
            
    pygame.joystick.init() #Αρχικοποιήση του Joystic
    controller1 = pygame.joystick.Joystick(0) #Δημιουργια αντικειμένου controller1 για το Joystick με ID = 0
    if controller1.get_button(5) == 1:#αν το button 5 γυρίσει Status True [R1]
            Fire_MainLoop()
    Spaceship_on_Rock()
    show_bullet_remaining_UPDATE()
    screen.blit(i1,(xspaceship,yspaceship)) #αποτύπωση διαστημοπλοίου [εκτος εκπυρσοκρότησης]
    pygame.display.update() #UPDATE του buffer
    
        
    
    
