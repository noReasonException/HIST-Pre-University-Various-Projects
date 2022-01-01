import random
import pygame
from sys import exit
from pygame.locals import *



pygame.init() #Αρχικοποιηση Pygame

windows_size = (900,600) #Μεγεθος παραθυρου Turple

screen = pygame.display.set_mode(windows_size,DOUBLEBUF,32) #δημιουργια οθονης

#Φορτωση εικονων
ship = pygame.image.load("SpaceCraft.png")

rock = pygame.image.load("Rock.png")

Game_Over_Image = pygame.image.load("GO.png")
Game_Over_Image2 = pygame.image.load("GO2.png")
showpoints = pygame.image.load("POINTS.png")
thefont = pygame.font.SysFont("Arial",20)


#Τοποθεσιες
shipx = 400
shipy = 400 #Παντα σταθερο

rockx = 400
rocky = 100

rockx2 = 400
rocky2 = 100
#χρωμα RBG παρασκηνιου 
Background = (0,0,0)

points = 0


while 1:
    
    #εκτελεση της pygame.event.get()
    for event in pygame.event.get():
        pass
    #αριστερο κλικ αριστερα διαστημοπλοιο
    key=pygame.key.get_pressed()  #checking pressed keys
    if key[pygame.K_LEFT]:
        if shipx < 100:
            continue
        shipx = shipx - 1
    #δεξι κλικ δεξια διαστημοπλοιο
    key=pygame.key.get_pressed()  #checking pressed keys
    if key[pygame.K_RIGHT]:
        if shipx > 700:
            continue
        shipx = shipx + 1

    #Πορεια Πετρας    
    rocky = rocky + 1
    #Πορεια Πετρας    2 
    rocky2 = rocky2 + 1
    #Ορια πιστας
    if rocky > 700:
        rocky = 100
        rockx = random.randint(200,700)
    for near in range(0,100):
        if rockx + near and rocky + near  == shipy:
            while True:
                screen.fill((0,0,0))
                screen.blit(Game_Over_Image,(200,200))
                screen.blit(Game_Over_Image2,(100,100))
                screen.blit(showpoints,(320,500))
                screen.blit(thepoints,(800,525))
                pygame.display.update()
    if rocky2 > 700:
        rocky2 = 100
        rockx = random.randint(200,700)
    for near in range(1,100):
        if rockx2 + near  == shipx and rocky2 + near == shipy:
            while True:
                screen.fill((0,0,0))
                screen.blit(Game_Over_Image,(200,200))
                screen.blit(Game_Over_Image2,(100,100))
                pygame.display.update()
        
            
    #ζωγραφισμα καρε
    thepoints = thefont.render(str(points),False,(0,0,0),(255,255,255))
    screen.fill(Background)
    screen.blit(thepoints,(50,50))
    screen.blit(ship,(shipx,shipy))
    screen.blit(rock,(rockx,rocky))
    if points > 10000:
        screen.blit(rock,(rockx2,rocky2))
    #Εκτυπωση 
    pygame.display.update()
    
    points = points + 1
    

