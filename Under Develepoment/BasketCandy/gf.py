import pygame #Κανει εισαγωγη ολη την pygame!
from pygame.locals import * #Κανει καπιες σημαντικες μεταβλητες/σταθερες import στο προγραμμα μας

import random

pygame.init() #Αρχικοποιεί το Pygame

screen = pygame.display.set_mode((745,480),DOUBLEBUF,32)
candy = pygame.image.load("candy.png")
gun = pygame.image.load("gun.png")
gk = pygame.image.load("ab.png")
bg = pygame.image.load("bg.jpg")

x=325
y=400

xgk = 290
ygk = 80



onshoot = False
counter = 0
move = True
movebucket=True
speed = 6
score = 0
lives = 6
while True:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    
    screen.blit(candy,(x,y))
    screen.blit(gun,(310,385))
    screen.blit(gk,(xgk,ygk))

    if move==True and movebucket==True:
        xgk+=speed
        if (xgk>=542):
            move=False
    if move==False and movebucket==True:
        xgk-=speed
        if (xgk<=50):
            move=True

    if movebucket==False and xgk!=x:
        lives-=1
        movebucket=True
        onshoot = False
        y=400
        

    if lives<=0:
        movebucket=False
        onshoot = False
        break #(!)
    speed=lives
        
    
    print("LIV : ",lives)
        
    for event in pygame.event.get():
        if pygame.mouse.get_pressed() == (True,False,False):
            onshoot=True

    
    if onshoot==True:
        counter+=1
        y = y - 6
        if y<=100:
            onshoot = False
            movebucket=False
            
    
    pygame.display.update()
    
    
    
