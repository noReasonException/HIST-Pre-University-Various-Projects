import pygame
from pygame.locals import *

from sys import exit
import random
import time




    

pygame.init() 
windows_size = (800,650) 

screen = pygame.display.set_mode(windows_size,DOUBLEBUF,32) 

pygame.display.set_caption("The CupCake Master 1.1") 

background_color_rgb = (0,0,0)

background_color = (250,250,250)


name = pygame.image.load("name.png")
play = pygame.image.load("play.png")
credits_ = pygame.image.load("credits.png")
info = pygame.image.load("info.png")
exit_ = pygame.image.load("exit.png")

play_ch = pygame.image.load("play_choice.png")
credits_ch = pygame.image.load("credits_choice.png")
info_ch = pygame.image.load("info_choice.png")
exit_ch = pygame.image.load("exit_choice.png")
credits_menu = pygame.image.load("Credits2.png")
info_menu = pygame.image.load("info2.png")
GamOver = pygame.image.load("GameOverDialog1.jpg")
GamOverPoints = pygame.image.load("GameOverDialog2.jpg")
Pres_Dialog = pygame.image.load("PresDialog.jpg")
ExitDialog = pygame.image.load("ExitDialog.jpg")
ExitDialog2 = pygame.image.load("ExitDialog2.jpg")
timer100 = pygame.image.load("timer100.png")
timer75 = pygame.image.load("timer75.png")
timer50 = pygame.image.load("timer50.png")
timer25 = pygame.image.load("timer25.png")
timer15 = pygame.image.load("timer15.png")
BG = pygame.image.load("BG.jpg")
Yes = pygame.image.load("Yes.png")
No = pygame.image.load("No.png")
Yes_Pressed = pygame.image.load("Yes_Pressed.png")
No_Pressed= pygame.image.load("No_Pressed.png")
thefont = pygame.font.SysFont("Arial",48)        
cake_load = pygame.image.load("Chocolate-Orange-Cupcake-icon.png")
cake_one_of_the_kind = pygame.image.load("Ocean-Cupcake-icon.png")

def Terminate_Programm():
    position_menu = 1
    while True:
                
        screen.fill((255,255,255)) 
        screen.blit(ExitDialog,(150,150))
        screen.blit(Yes,(200,450))
        screen.blit(No,(500,450)) 
        for event in pygame.event.get():
            
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]: 
                position_menu = position_menu + 1 
            if position_menu > 2: 
                position_menu = 1 
            if key[pygame.K_LEFT]:
                position_menu = position_menu - 1
                if position_menu < 1:
                    position_menu = 2
            if position_menu == 1:
                screen.blit(Yes_Pressed,(200,450)) 
            if position_menu == 2:
                screen.blit(No_Pressed,(500,450))
            if key[pygame.K_RETURN]:
                if position_menu == 1:
                    screen.fill((255,255,255))
                    screen.blit(ExitDialog2,(150,150))
                    pygame.display.update()
                    time.sleep(2)
                    exit()
                if position_menu == 2: 
                    return False   
            
            pygame.display.update()

def pres():
    """
    import pygame.Movie

    FPS = 60

    pygame.init()
    clock = pygame.time.Clock()
    movie = pygame.movie.Movie('Presentation.mpg')
    screen = pygame.display.set_mode(movie.get_size())
    movie_screen = pygame.Surface(movie.get_size()).convert()

    movie.set_display(movie_screen)
    movie.play()


    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movie.stop()
                playing = False

        screen.blit(movie_screen,(0,0))
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
pres()
"""

points = 0

choice_position = 1
while True:
    screen.fill (background_color)  

    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if  key[pygame.K_UP]:

            choice_position = choice_position - 1

            if choice_position > 4:

                choice_position = 1
        if  key[pygame.K_DOWN]:

            choice_position = choice_position + 1

            if choice_position < 1:

                choice_position = 1

        if event.type == QUIT:
            ask = Terminate_Programm()
            if ask == False:
                pass
        
        if key[pygame.K_RETURN]:

            if choice_position == 1:


                possiblemoves = [(200,100),(200,250),(200,420),(350,100),(350,250),(350,420),(520,100),(520,250),(520,420)]

                random = random.randint(0,8)

                timer = 0
                while True:

                    screen.fill((255,255,255))
                    screen.blit(BG,(0,0))


                    timer = timer + 1
                    if timer < 2600:
                        screen.blit(timer100,(1,625))
                    if timer > 2600 and  timer < 5200  :
                        screen.blit(timer75,(1,625))
                    if timer > 5200 and timer < 7800:
                        screen.blit(timer50,(1,625))
                    if timer > 7800 and timer < 10400 :
                        screen.blit(timer25,(1,625))
                    if timer > 10400 and timer < 13000:
                        screen.blit(timer15,(1,625))

                    if timer > 13000:
                        while True:

                            timer = timer + 1

                            screen.fill((255,255,255))

                            if timer < 14000 :

                                screen.blit(GamOver,(100,100))

                            if timer > 14000:

                                screen.blit(GamOverPoints,(100,100))

                                screen.blit(thepoints , (330,200))

                            pygame.display.update()
                            
                          
                    

                    screen.blit(name,(150,10))

                    for inp in possiblemoves:


                        screen.blit(cake_load,inp)

                    screen.blit(cake_one_of_the_kind,possiblemoves[random])

                    for event in pygame.event.get():

                        if pygame.key.get_pressed()[K_w] and random == 0:

                            import random

                            random = random.randint(0,8)

                            points = points + 1

                        if pygame.key.get_pressed()[K_e] and random == 3:
                            import random
                            random = random.randint(0,8)
                            points = points + 1

                        if pygame.key.get_pressed()[K_r] and random == 6:
                            import random
                            random = random.randint(0,8)
                            points = points + 1

                        if pygame.key.get_pressed()[K_s] and random == 1:
                            import random
                            random = random.randint(0,8)
                            points = points + 1

                        if pygame.key.get_pressed()[K_d] and random == 4:
                            import random
                            random = random.randint(0,8)
                            points = points + 1

                        if pygame.key.get_pressed()[K_f] and random == 7:
                            import random
                            random = random.randint(0,8)
                            points = points + 1

                        if pygame.key.get_pressed()[K_x] and random == 2:
                            import random
                            random = random.randint(0,8)
                            points = points + 1

                        if pygame.key.get_pressed()[K_c] and random == 5:
                            import random
                            random = random.randint(0,8)
                            points = points + 1

                        if pygame.key.get_pressed()[K_v] and random == 8:
                            import random
                            random = random.randint(0,8)
                            points = points + 1

                    thepoints = thefont.render(str(points),True,(0,0,0),(255,255,255))

                    screen.blit(thepoints,(50,20))

                    pygame.display.update()
                    

            if choice_position == 2:

                while True:
                    screen.fill((255,255,255))
                    screen.blit(credits_menu,(100,100))
                    pygame.display.update()

            if choice_position == 3:

                while True:
                    screen.fill((255,255,255))
                    screen.blit(info_menu,(100,100))
                    pygame.display.update()

            if choice_position == 4:
                ask = Terminate_Programm()
                if ask == False:
                    pass
        

    screen.blit(play,(25,25))
    screen.blit(credits_,(25,150))
    screen.blit(info,(25,275))
    screen.blit(exit_,(25,400))


    if choice_position == 1:

        screen.blit(play_ch,(25,25))

    if choice_position == 2:

        screen.blit(credits_ch,(25,150))

    if choice_position == 3:

        screen.blit(info_ch,(25,275))

    if choice_position == 4:

        screen.blit(exit_ch,(25,400))

    
    screen.blit(Pres_Dialog,(250,300))
    screen.blit(name,(200,10))
    pygame.display.update() 

    
     
    
            


