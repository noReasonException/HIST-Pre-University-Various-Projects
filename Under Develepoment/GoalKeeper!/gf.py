import pygame #Κανει εισαγωγη ολη την pygame!
from pygame.locals import * #Κανει καπιες σημαντικες μεταβλητες/σταθερες import στο προγραμμα μας

import random

pygame.init() #Αρχικοποιεί το Pygame

screen = pygame.display.set_mode((745,480),DOUBLEBUF,32)
ball1 = pygame.image.load("ball.png")
ball2 = pygame.image.load("ball2.png")
ball3 = pygame.image.load("ball3.png")
ball4 = pygame.image.load("ball4.png")
ball5 = pygame.image.load("ball5.png")
can = pygame.image.load("can.png")
gk = pygame.image.load("ab.png")
bg = pygame.image.load("a.png")

x=120
y=380

xgk = 299
ygk = 220

defalt_ball = ball1

onshootL = False
onshootR = False
counter = 0
move = random.randint(1,2)
while True:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    
    screen.blit(defalt_ball,(x,y))
    screen.blit(can,(361,230))

    screen.blit(gk,(xgk,ygk))

    if move==1:
        if onshootL==True or onshootR == True:
            xgk-=0.17
    if move==2:
        if onshootL==True or onshootR == True:
            xgk+=0.17
        
    for event in pygame.event.get():
        if pygame.mouse.get_pressed() == (True,False,False):
            onshootL=True
        if pygame.mouse.get_pressed() == (False,False,True):
            onshootR=True

    
    if onshootL==True:
        counter+=1
        x = x + 1
        y = y - 1
        if y<=220:
            onshootL = False
        if counter > 60:
            defalt_ball = ball2
        if counter > 80:
            defalt_ball = ball3
        if counter > 120: #συνολικά καρέ σουτ = 180
                                    #180/4=45
            defalt_ball = ball4
        if counter > 180:
            defalt_ball = ball5
            
        
    if onshootR==True:
        counter+=1
        x = x + 1.3
        y = y - 1
        if y<=210:
            onshootR = False
        if counter > 60:
            defalt_ball = ball2
        if counter > 80:
            defalt_ball = ball3
        if counter > 120: #συνολικά καρέ σουτ = 180
                                    #180/4=45
            defalt_ball = ball4
        if counter > 180:
            defalt_ball = ball5
    print(x)
    
    pygame.display.update()
    
    
    
