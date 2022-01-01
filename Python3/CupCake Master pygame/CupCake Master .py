import pygame
from pygame.locals import * 
from sys import exit
import random




    

pygame.init() #αρχικοποιηση pygame
windows_size = (800,650) #μεγεθος παραθυρου σε pixels  ειναι απλη μεταβλητη με turple

screen = pygame.display.set_mode(windows_size,DOUBLEBUF,32) #αναλυση #διπλη buffer #?

pygame.display.set_caption("The CupCake Master 0.01") # Παραθυρικος Τιτλος

background_color_rgb = (0,0,0)#ειναι ενα turple το οποιο περιεχει το χρωμα σε R G B  

background_color = (250,250,250)

#Εικονες μενου,γραφικα και παρουσιασεις
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

thefont = pygame.font.SysFont("Arial",48)        
cake_load = pygame.image.load("Chocolate-Orange-Cupcake-icon.png")#φορτωσε εικονα
cake_one_of_the_kind = pygame.image.load("Ocean-Cupcake-icon.png")#το ιδιο

#δηλωση ποντων
points = 0
#θεση επιλογης μενου
choice_position = 1
while True:
    screen.fill (background_color) #γεμσε οθονη με χρωμα οθονης    
    #Μενου
    #Χειρισμός με events κληκρολογιου και + η - μεταβλητη 
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            #αυξανεται η μεταβλητη
            choice_position = choice_position + 1
            #αν ειναι >4
            if choice_position > 4:
                #απο την επιλογη 1 [=1]
                choice_position = 1
        
        #αν πατηθει το αριστερο κλικ
        if pygame.mouse.get_pressed() == (True,False,False): 
            #..και η επιλογη ειναι 1
            if choice_position == 1:
                #ΠΑΙΞΕ
                #Θεσεις 
                                  #ΔΠ      ΔΜ       ΔΚ        ΜΠ       ΜΜ        ΜΚ        ΑΠ        ΑΜ       ΑΚ
                possiblemoves = [(200,70),(200,220),(200,395),(350,70),(350,220),(350,395),(520,70),(520,200),(520,395)]
                #Τυχαια επιλογη θεσης για το ξεχωριστο cupcake
                random = random.randint(0,8)
                #χρονικο διαστημα σε κυκλους [ 13000 ~ 60sec]
                timer = 0
                while True:
                    #αυξηση χρόνου
                    timer = timer + 1
                    #οταν ο χρονος ειναι >13000[1 λεπτο]
                    if timer > 13000:
                        while True:
                            #συνεχιση αυξησης χρονου!
                            timer = timer + 1
                            #γεμισμα με ασπρο
                            screen.fill((255,255,255))
                            #οταν ειναι < 14000
                            if timer < 14000 :
                                #διαλογος GameOver
                                screen.blit(GamOver,(100,100))
                            #οταν ειναι μεγαλυτερο απο 14000
                            if timer > 14000:
                                #κενος διαλογος
                                screen.blit(GamOverPoints,(100,100))
                                #κεντραρισμα ποντων
                                screen.blit(thepoints , (330,200))
                            #εκτυπωση καρε
                            pygame.display.update()
                            
                    #γεμισε ασπρο        
                    screen.fill((255,255,255))
                    #λογοτυπο
                    screen.blit(name,(150,10))
                    #διαβασμα possiblemoves
                    for inp in possiblemoves:
                        #διαδοχικη εισαγωγη στην inp
                        #διαδοχικη εκτυπωση στις θεσεις[turples] 
                        screen.blit(cake_load,inp)
                    #απο πανω εκτυπωση στην τυχαια θεση random(0,8)
                    screen.blit(cake_one_of_the_kind,possiblemoves[random])
                    #συμβαντα πληκρολογιου
                    for event in pygame.event.get():
                        #αν το w ειναι πατημενο [πανω δεξια] και η τυχαια θεση ειναι 0 [επισης πανω δεξια]
                        if pygame.key.get_pressed()[K_w] and random == 0:
                            #εισαγωγη βιβλιοθηκης random
                            import random
                            #random (0,8) αλλη θεση
                            random = random.randint(0,8)
                            #αυξησε ποντους
                            points = points + 1
                        #αντοιστοιχως για w
                        if pygame.key.get_pressed()[K_e] and random == 3:
                            import random
                            random = random.randint(0,8)
                            points = points + 1
                        #αντοιστοιχως για w
                        if pygame.key.get_pressed()[K_r] and random == 6:
                            import random
                            random = random.randint(0,8)
                            points = points + 1
                        #αντοιστοιχως για w
                        if pygame.key.get_pressed()[K_s] and random == 1:
                            import random
                            random = random.randint(0,8)
                            points = points + 1
                        #αντοιστοιχως για w
                        if pygame.key.get_pressed()[K_d] and random == 4:
                            import random
                            random = random.randint(0,8)
                            points = points + 1
                        #αντοιστοιχως για w
                        if pygame.key.get_pressed()[K_f] and random == 7:
                            import random
                            random = random.randint(0,8)
                            points = points + 1
                        #αντοιστοιχως για w
                        if pygame.key.get_pressed()[K_x] and random == 2:
                            import random
                            random = random.randint(0,8)
                            points = points + 1
                        #αντοιστοιχως για w
                        if pygame.key.get_pressed()[K_c] and random == 5:
                            import random
                            random = random.randint(0,8)
                            points = points + 1
                        #αντοιστοιχως για w
                        if pygame.key.get_pressed()[K_v] and random == 8:
                            import random
                            random = random.randint(0,8)
                            points = points + 1
                        #αντοιστοιχως για w
                    #δημιουργια εικονας για ποντους
                    thepoints = thefont.render(str(points),True,(0,0,0),(255,255,255))
                    #κεντραρισμα της σε 50,20
                    screen.blit(thepoints,(50,20))
                    #εκτυπωση καρε
                    pygame.display.update()
                    
            #..και η επιλογη ειναι 2
            if choice_position == 2:
                #ΔΕΙΞΕ CREDITS
                while True:
                    screen.fill((255,255,255))
                    screen.blit(credits_menu,(100,100))
                    pygame.display.update()
            #..και η επιλογη ειναι 3
            if choice_position == 3:
                #ΔΕΙΞΕ INFO
                while True:
                    screen.fill((255,255,255))
                    screen.blit(info_menu,(100,100))
                    pygame.display.update()
            #..και η επιλογη ειναι 4
            if choice_position == 4:
                #ΕΞΟΔΟΣ
                exit()
        
    #Ζωγραφισμα ολων [χωρις επιλογη]
    screen.blit(play,(25,25))
    screen.blit(credits_,(25,150))
    screen.blit(info,(25,275))
    screen.blit(exit_,(25,400))
    #Πατημα απο πανω του επιλεγμένου[αναλογα με choice_position]
    #αν η επιλογη ειναι 1
    if choice_position == 1:
        #χρωματισε το PLAY
        screen.blit(play_ch,(25,25))
    #αν η επιλογη ειναι 2
    if choice_position == 2:
        #χρωματισε το CREDITS
        screen.blit(credits_ch,(25,150))
    #αν η επιλογη ειναι 3
    if choice_position == 3:
        #χρωματισε το INFO
        screen.blit(info_ch,(25,275))
    #αν η επιλογη ειναι 4
    if choice_position == 4:
        #χρωματισε το EXIT
        screen.blit(exit_ch,(25,400))

    
    screen.blit(Pres_Dialog,(250,300))
    screen.blit(name,(200,10))
    pygame.display.update() #εκτυπωση καρε  μολις ετοιμαστει

    
     
    
            


