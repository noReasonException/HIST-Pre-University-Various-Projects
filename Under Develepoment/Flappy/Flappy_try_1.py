import pygame
from pygame.locals import *
import random

#μεγεθος παραθυρου[turple]
windowssize = (997,500)
#αντικειμενο οθονης[μεθοδος set_mode]
screen = pygame.display.set_mode(windowssize,DOUBLEBUF,32)

#Φορτωση Εικόνων
bird = pygame.image.load("flappy.png")
back = pygame.image.load("BackGround.png")
rock1 = pygame.image.load("Rock1.png") 
rock2 = pygame.image.load("Rock2.png") 
rock3 = pygame.image.load("Rock3.png") 
rock4 = pygame.image.load("Rock4.png")

#Αρχικη τροποθεσια bird
birdx = 50
birdy = 50
#Φαση περιστροφης πέτρας
rocktype = 1
#ύπαρξη πετρας σε πιστα 1
rockinlevel = False
#Αρχική τοποθεσία
rocky = 366 #τυχαιο
rockx = 900 #Μειώνεται!

def GameOver():
    """
    global birdx,birdy
    while birdy != 400:
        birdy = birdy - 10
        screen.blit(bird,(birdx,birdy))
        screen.blit(back,(0,0))
        pygame.display.update()
    screen.blit(back,(0,0))
    pygame.display.update
    exit()
    """
    pass
    

#Κεντρικός Βρόνχος
while True :#Mainloop
    #Logs
    print "Rock There is   :" ,rockinlevel
    print "Rock Position x :" , rockx
    print "Rock Position y :" , rocky
    print "Bird Position x :" , birdx
    print "Bird Position y :" , birdy
    #Παρασκήνιο
    screen.blit(back,(0,0))
    #Bird[μεθοδος blit]
    screen.blit(bird,(birdx,birdy))
    #Εκτέλεση της event.get() [απαραίτητο για να έχουμε την key_pressed αργοτερα]
    for event in pygame.event.get():
        pass #Τιποτα
    #Αν μεσα στο return [Μορφη λιστας] της get_pressed() Υπάρχει ισότητα με το attritude pygame.K_UP
    if pygame.key.get_pressed()[pygame.K_UP]:
        #Μείωση του bird [θεση y] κατα 9 [προς τα επανω]
            birdy = birdy - 13
    if birdy < 10:
        birdy = 10
    if birdy > 400:
        birdy = 400
    #Πρός τα κάτω 
    birdy = birdy + 5
    #Αν υπαρξη πετρας μεσα σε πίστα ==ΨΕΥΔΗΣ
    if rockinlevel == False:
        #τοτε γίνεται ==ΑΛΗΘΗΣ
        rockinlevel = True
        #τυχαία θεση y [ανα 100]
        rocky = random.randint(1,450) #τυχαιο
        #Αρχική τιμή y [στην συνέχεια μειώνεται για να πλησιάζει το bird]
        rockx = 900 #Μειώνεται!
        #Αρχικοποίηση Περιστροφής Πέτρας
        rocktype = 1
    #Αν ύπαρξη Πέτρας μεσα σε πίστα ==ΑΛΗΘΗΣ[1]
    if rockinlevel == True:
        #Μείωση x [πλησιάζοντας bird]
        rockx = rockx - 3
        #Περιστροφη πέτρας
        """
        rocktype = rocktype + 1
        if rocktype > 4:
            rocktype == 1
        if rocktype == 1:
            screen.blit(rock1,(rockx,rocky))
        elif rocktype == 2:
            screen.blit(rock2,(rockx,rocky))
        elif rocktype == 3:
            screen.blit(rock3,(rockx,rocky))
        elif rocktype == 4:
            screen.blit(rock4,(rockx,rocky))
        """
        #Αποτύπωση πέτρας στην οθόνη [μεθοδος blit]
        screen.blit(rock1,(rockx,rocky))
    #Αν δεν είναι μέσα στα όρια της πίστας!
    if rockx < 5 or rocky < 5 :
        rockinlevel = False
    #Game Over
    for check in range(10):
        if birdx + check == rockx:
            GameOver()
    #buffer update!
    pygame.display.update()
       
