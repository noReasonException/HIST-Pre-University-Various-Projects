import pygame
from pygame.locals import *
import random

#������� ���������[turple]
windowssize = (997,500)
#����������� ������[������� set_mode]
screen = pygame.display.set_mode(windowssize,DOUBLEBUF,32)

#������� �������
bird = pygame.image.load("flappy.png")
back = pygame.image.load("BackGround.png")
rock1 = pygame.image.load("Rock1.png") 
rock2 = pygame.image.load("Rock2.png") 
rock3 = pygame.image.load("Rock3.png") 
rock4 = pygame.image.load("Rock4.png")

#������ ���������� bird
birdx = 50
birdy = 50
#���� ����������� ������
rocktype = 1
#������ ������ �� ����� 1
rockinlevel = False
#������ ���������
rocky = 366 #������
rockx = 900 #���������!

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
    

#��������� �������
while True :#Mainloop
    #Logs
    print "Rock There is   :" ,rockinlevel
    print "Rock Position x :" , rockx
    print "Rock Position y :" , rocky
    print "Bird Position x :" , birdx
    print "Bird Position y :" , birdy
    #����������
    screen.blit(back,(0,0))
    #Bird[������� blit]
    screen.blit(bird,(birdx,birdy))
    #�������� ��� event.get() [���������� ��� �� ������ ��� key_pressed ��������]
    for event in pygame.event.get():
        pass #������
    #�� ���� ��� return [����� ������] ��� get_pressed() ������� ������� �� �� attritude pygame.K_UP
    if pygame.key.get_pressed()[pygame.K_UP]:
        #������ ��� bird [���� y] ���� 9 [���� �� �����]
            birdy = birdy - 13
    if birdy < 10:
        birdy = 10
    if birdy > 400:
        birdy = 400
    #���� �� ���� 
    birdy = birdy + 5
    #�� ������ ������ ���� �� ����� ==������
    if rockinlevel == False:
        #���� ������� ==������
        rockinlevel = True
        #������ ���� y [��� 100]
        rocky = random.randint(1,450) #������
        #������ ���� y [���� �������� ��������� ��� �� ��������� �� bird]
        rockx = 900 #���������!
        #������������ ����������� ������
        rocktype = 1
    #�� ������ ������ ���� �� ����� ==������[1]
    if rockinlevel == True:
        #������ x [������������ bird]
        rockx = rockx - 3
        #���������� ������
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
        #��������� ������ ���� ����� [������� blit]
        screen.blit(rock1,(rockx,rocky))
    #�� ��� ����� ���� ��� ���� ��� ������!
    if rockx < 5 or rocky < 5 :
        rockinlevel = False
    #Game Over
    for check in range(10):
        if birdx + check == rockx:
            GameOver()
    #buffer update!
    pygame.display.update()
       
