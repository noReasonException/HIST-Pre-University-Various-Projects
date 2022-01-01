#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
from Tkinter import *
import time
#Καθορισμός χάρτη και διαστημοπλοίου
spaceship = "}=~"
rock = "@"
#συνάρτηση ανακατέυθυνσης στα μενού
def wait():
	x = raw_input("Press Enter key to continue!")
	if x == "":
		menu()
	else:
		menu()
#ποντοι,ζωες
lives = 3
points = 0
#how_to_play συνάρτηση
def how_to_play():
	os.system("clear")
	print """
+-----------------------------------------------------------+
|Escape from the spacerocks with no touch your spaceship    
|Open the flight control before you start play
|For control your spaceship just open flight control and
|click in the window top or bottom
|Note Dont delete the moves.txt file!
|Enjoy
+-----------------------------------------------------------+
"""
	wait()
#Credits συνάρτηση
def credit():
	os.system("clear")
	print """
   _   _   _   _   _   _   _   _   _      _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \    / \ / \ / \ / \ / \ / \ 
 ( S | p | a | c | e | R | o | c | k )  ( E | s | c | a | p | e )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/    \_/ \_/ \_/ \_/ \_/ \_/         
+-------------------------------------+
Written By El_Sonador
Version 1.0
"""
	wait()
#Συνάρτηση menu
def menu():
	#αναπληρωση ζωής,μηδενισμός πόντων
	global lives
	lives  = 3
	global points
	points = 0
	os.system("clear")
	print """
   _   _   _   _   _   _   _   _   _      _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \    / \ / \ / \ / \ / \ / \ 
 ( S | p | a | c | e | R | o | c | k )  ( E | s | c | a | p | e )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/    \_/ \_/ \_/ \_/ \_/ \_/ 
+-------------------------------------+
Welcome to SpaceRock Escape!
Written by El_Sonador

1)Play
2)How to play
3)Credits
4)Exit
"""
	#επιλογή
	choice = raw_input("Enter your Choice ~ ")
	if int(choice) == 1:
		return 1
	if int(choice) == 2:
		how_to_play()
	if int(choice) == 3:
		credit()
	if int(choice) == 4:
		exit()
	else:
		menu()
#δίαβασμα της προβλέπομενης κίνησης απο τον flight control 
def move():
	move = open("move.txt","r")
	return int(move.read())
	move.close
#Καθορισμός χάρτη
ya = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yb = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yc = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yd = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
ye = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yf = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yg = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yh = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yi = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yj = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yk = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
yl = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "] 
#GameOver Fuction
def draw_game_over(point):
	os.system("clear")
	print """
   ______                     ____                 
  / ____/___ _____ ___  ___  / __ \_   _____  _____
 / / __/ __ `/ __ `__ \/ _ \/ / / / | / / _ \/ ___/
/ /_/ / /_/ / / / / / /  __/ /_/ /| |/ /  __/ /    
\____/\__,_/_/ /_/ /_/\___/\____/ |___/\___/_/     
                                                   
"""
	print "Your Total Points Are:",point
#Καθορισμός σχηματισμού καρέ
#update!
def draw_map():
	os.system("clear")
	print "SpaceRock Escape!"
	print "Points :"+str(points)
	print "Frames :4"
	print "Lives  :"+str(lives)
	print "[------------------------------------------------------------------------------]"
	print ya[0],ya[1],ya[2],ya[3],ya[4],ya[5],ya[6],ya[7],ya[8],ya[9],ya[10],ya[11],ya[12]
	print yb[0],yb[1],yb[2],yb[3],yb[4],yb[5],yb[6],yb[7],yb[8],yb[9],yb[10],yb[11],yb[12]
	print yc[0],yc[1],yc[2],yc[3],yc[4],yc[5],yc[6],yc[7],yc[8],yc[9],yc[10],yc[11],yc[12]
	print yd[0],yd[1],yd[2],yd[3],yd[4],yd[5],yd[6],yd[7],yd[8],yd[9],yd[10],yd[11],yd[12]
	print ye[0],ye[1],ye[2],ye[3],ye[4],ye[5],ye[6],ye[7],ye[8],ye[9],ye[10],ye[11],ye[12]
	print yf[0],yf[1],yf[2],yf[3],yf[4],yf[5],yf[6],yf[7],yf[8],yf[9],yf[10],yf[11],yf[12]
	print yg[0],yg[1],yg[2],yg[3],yg[4],yg[5],yg[6],yg[7],yg[8],yg[9],yg[10],yg[11],yg[12]
	print yh[0],yh[1],yh[2],yh[3],yh[4],yh[5],yh[6],yh[7],yh[8],yh[9],yh[10],yh[11],yh[12]
	print yi[0],yi[1],yi[2],yi[3],yi[4],yi[5],yi[6],yi[7],yi[8],yi[9],yi[10],yi[11],yi[12]
	print yj[0],yj[1],yj[2],yj[3],yj[4],yj[5],yj[6],yj[7],yj[8],yj[9],yj[10],yj[11],yj[12]
	print yk[0],yk[1],yk[2],yk[3],yk[4],yk[5],yk[6],yk[7],yk[8],yk[9],yk[10],yk[11],yk[12]
	print yl[0],yl[1],yl[2],yl[3],yl[4],yl[5],yl[6],yl[7],yl[8],yl[9],yl[10],yl[11],yl[12]
	print "[------------------------------------------------------------------------------]"
#συνάρτηση σχηματισμού αντικείμένων στον χάρτη{δηλωνώντας ισοτητες πάνω στη κατάλληλη λίστα και κάνοντας τη reset}
#σχεδίαση
def draw_objects(typeof,x,pos):
	if typeof == "spaceship":
		if pos < 12 and pos > -1:
			x[pos] = spaceship
		else:
			if pos > 12:
				pos == 12
			if pos < -1:
				pos = 0
	if typeof == "rock":
		if pos < 12 and pos > -1:
			x[pos] = rock
		else:
			if pos > 12:
				pos == 12
			if pos < -1:
				pos = 0
#σχηματισμός διαστημοπλοιου στην κατάλληλη θέση!
#σχεδίαση
def navigate(typeof,pos,pos_of_obj = "-"):
	if typeof == "spaceship":
		if pos == 0:
			draw_objects("spaceship",yl,0)
		if pos == 1:
			draw_objects("spaceship",yk,0)
		if pos == 2:
			draw_objects("spaceship",yj,0)
		if pos == 3:
			draw_objects("spaceship",yi,0)
		if pos == 4:
			draw_objects("spaceship",yh,0)
		if pos == 5:
			draw_objects("spaceship",yg,0)
		if pos == 6:
			draw_objects("spaceship",yf,0)
		if pos == 7:
			draw_objects("spaceship",ye,0)
		if pos == 8:
			draw_objects("spaceship",yd,0)
		if pos == 9:
			draw_objects("spaceship",yc,0)
		if pos == 10:
			draw_objects("spaceship",yb,0)
		if pos == 11:
			draw_objects("spaceship",ya,0)
	if typeof == "rock":
		if pos == 0:
			draw_objects("rock",yl,pos_of_obj)
		if pos == 1:
			draw_objects("rock",yk,pos_of_obj)
		if pos == 2:
			draw_objects("rock",yj,pos_of_obj)
		if pos == 3:
			draw_objects("rock",yi,pos_of_obj)
		if pos == 4:
			draw_objects("rock",yh,pos_of_obj)
		if pos == 5:
			draw_objects("rock",yg,pos_of_obj)
		if pos == 6:
			draw_objects("rock",yf,pos_of_obj)
		if pos == 7:
			draw_objects("rock",ye,pos_of_obj)
		if pos == 8:
			draw_objects("rock",yd,pos_of_obj)
		if pos == 9:
			draw_objects("rock",yc,pos_of_obj)
		if pos == 10:
			draw_objects("rock",yb,pos_of_obj)
		if pos == 11:
			draw_objects("rock",ya,pos_of_obj)
	
create_rock = True
start = menu()	
#κεντρικός βρόνχος
while True:
	ya = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yb = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yc = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yd = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	ye = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yf = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yg = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yh = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yi = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yj = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yk = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	yl = ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
	#αυξηση πόντων ανα δευτερολεπτο
	points = points + 1
	#δίαβασμα της θέσης απο το αρχείο
	spaceship_position = move()
	#μετάφραση θέσης σε κατάλληλη λίστα
	navigate("spaceship",spaceship_position)
	#καθορισμός αναμονής {frames = 4 per second!}
	time.sleep(0.25)
	
	#δημιουργίας πέτρας( αλήθής για πρώτη φορά)
	if create_rock == True:
		#αρχικη θέση πέτρας
		rock_start_pos = random.randint(0,11)
		#αρχική τοποθεσία{πρωσωρινή } πέτρας
		rock_position = rock_start_pos
		#μετάφραση στις κατάλληλες λίστες
		navigate("rock",rock_start_pos,rock_position)
		#αφού έχει δημιουργηθεί ηδη η πέτρα γυρνάμε σε ψευδής και στο if που συντηρεί την πορεία της πετρας
		create_rock = False
		continue
	#συντήρηση πορείας της πέτρας	
	if create_rock == False:
		#μείωση τοποθείας για να ζηγώσει το διαστημόπλοιο
		rock_position = rock_position - 1
		#μετάφραση position στις κατάλληλες λίστες
		navigate("rock",rock_start_pos,rock_position)
		#άν η πέτρα έχει ολοκλήρώση της πορεία της
		if rock_position < 0:
			#σχεδίαση άλλης πέτρας
			create_rock = True
	#ανίχνευση σύγρουσης		
	if rock_position == spaceship_position :
		#μείωση ζωής
		lives = lives - 1
	#αν οι ζώες έχουν τελειώσει...
	if lives == -1:
		#Gameover
		draw_game_over(points)
		#αναμονή
		wait()
	#σχεδίαση
	draw_map()
	
	
		
		
	
	
	
	
	
	
	
