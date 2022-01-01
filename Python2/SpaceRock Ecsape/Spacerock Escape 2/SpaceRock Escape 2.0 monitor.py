# -*- coding: utf-8 -*-
import random
import time
import os

points = 0
lives  = 5

#Δήλωση χάρτη
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x10 = []
#Γέμισμα του χάρτη με κενά ή επαναδημιουργία χάρτη
def DRAW_map():
	for appendmap in range (11):
		x1.append("   ")
		x2.append("   ")
		x3.append("   ")
		x4.append("   ")
		x5.append("   ")
		x6.append("   ")
		x7.append("   ")
		x8.append("   ")
		x9.append("   ")
		x10.append("   ")
#Σβήσιμο προηγούμενων δεδόμένων
def RESET_map():
	global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10
	x1 = []
	x2 = []
	x3 = [] 
	x4 = []
	x5 = []
	x6 = []
	x7 = []
	x8 = []
	x9 = []
	x10 = []
#Εκτύπωση πίστας
def PRINT_map():
	os.system("cls")
	print "      Points",points
	print "      Lives",lives
	print "     |",x10[0],x10[1],x10[2],x10[3],x10[4],x10[5],x10[6],x10[7],x10[8],x10[9],x10[10]," |"
	print "     |",x9[0],x9[1],x9[2],x9[3],x9[4],x9[5],x9[6],x9[7],x9[8],x9[9],x9[10]," |"
	print "     |",x8[0],x8[1],x8[2],x8[3],x8[4],x8[5],x8[6],x8[7],x8[8],x8[9],x8[10]," |"
	print "     |",x7[0],x7[1],x7[2],x7[3],x7[4],x7[5],x7[6],x7[7],x7[8],x7[9],x7[10]," |"
	print "     |",x6[0],x6[1],x6[2],x6[3],x6[4],x6[5],x6[6],x6[7],x6[8],x6[9],x6[10]," |"
	print "     |",x5[0],x5[1],x5[2],x5[3],x5[4],x5[5],x5[6],x5[7],x5[8],x5[9],x5[10]," |"
	print "     |",x4[0],x4[1],x4[2],x4[3],x4[4],x4[5],x4[6],x4[7],x4[8],x4[9],x4[10]," |"
	print "     |",x3[0],x3[1],x3[2],x3[3],x3[4],x3[5],x3[6],x3[7],x3[8],x3[9],x3[10]," |"
	print "     |",x2[0],x2[1],x2[2],x2[3],x2[4],x2[5],x2[6],x2[7],x2[8],x2[9],x2[10]," |"
	print "     |",x1[0],x1[1],x1[2],x1[3],x1[4],x1[5],x1[6],x1[7],x1[8],x1[9],x1[10]," |"

#Μετατροπή τοποθεσίας x σε κατάληλες λίστες(η y μεταφράζεται ως θέσεις των λίστων x}
def NAVIGATE_obj(posx,posy,typeof):
      if posx == 10:
            x10[posy] = typeof
      if posx == 9:
            x9[posy] = typeof
      if posx == 8:
            x8[posy] = typeof
      if posx == 7:
            x7[posy] = typeof
      if posx == 6:
            x6[posy] = typeof
      if posx == 5:
            x5[posy] = typeof
      if posx == 4:
            x4[posy] = typeof
      if posx == 3:
            x3[posy] = typeof
      if posx == 2:
            x2[posy] = typeof
      if posx == 1:
            x1[posy] = typeof

def read_pos():
        with open("moves.txt","r") as read:
                return int(read.read())
spaceship = "}=>"
rock = "@"

player_x = 5
player_y = 0
Create_rock = True
rock_x = 5
rock_y = 5

while True:
        #Επανασχεδίαση χάρτη
        RESET_map()
        DRAW_map()
        #Χρονοκαθυστέρηση
        time.sleep(0.25)
        #Αυξηση πόντων
        points = points + 1
        #Διάβασμα τοποθεσίας x
        player_x = read_pos()
        #σχεδίαση διαστημοπλοίου
        NAVIGATE_obj(player_x,player_y,spaceship)
        #δημιουργία πέτρας
        if Create_rock == True:
                rock_x = random.randint(1,10)
                rock_y = 10
                Create_rock = False
        #Συντήρηση πορείας πέτρας
        if Create_rock == False:
                rock_y = rock_y - 1
                NAVIGATE_obj(rock_x,rock_y,"@  ")
                if rock_y < 0 :
                        Create_rock = True
        #Απαγόρευση εξόδου διαστημοπλοίου απο την πίστα
        if player_x > 10:
                player_x = 10
        if player_y > 10:
                player_y = 10
        if player_x < 0:
                player_x = 0
        if player_y < 0:
                player_y = 0
        #Ανίχνευση σύγρουσης
        if player_x == rock_x and player_y == rock_y :
                lives = lives - 1
        #GameOver
        if lives < 0 :
                print "GameOver"
                print "Your points are",points
                break
        #Εκτύπωση χάρτη
        PRINT_map()
                
        
        


