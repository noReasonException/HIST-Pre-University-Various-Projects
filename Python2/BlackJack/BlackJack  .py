#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
#Values
run1 = True
run2 = True

point1 = 0
point2 = 0

def drawcard(point):
	if point < 10 :
		print ".------."
		print "|"+str(point)+".--. |"
		print "| (\/) |"
		print "| :\/: |"
		print "| '--'"+str(point)+"|"
		print "`------'"
	if point == 10:
		print """
.------.
|10--. |
| (\/) |
| :\/: |
| '--10|
`------'
"""

print """
.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'

Coded by El Sonador
"""
while True:
	#Player 1
	if run1 == True:
		input1 = raw_input("Player 1 do you want card ? (y/n)")
		if input1 == "y":
			add1 = random.randint(1,10)
			point1 = add1 + point1
			drawcard(add1)
			print "Your total points are ", point1
			#Player 1 wins
			if point1 == 21:
				print "Player 1 wins ! "
				break
			#Player 2 wins
			if point1 > 21:
				print "Player 2 wins ! "
				break
		#Player 1 give up
		if input1 == "n":
			run1 = False
		
	if run2 == True:
		input2 = raw_input("Player 2 do you want card ? (y/n)")
		if input2 == "y":
			add2 = random.randint(1,10)
			point2 = add2 + point2
			drawcard(add2)
			print "Your total points are", point2
			#Player 2 wins
			if point2 == 21:
				print "Player 2 wins ! "
				break
			#Player 1 wins
			if point2 > 21:
				print "Player 1 wins ! "
				break
		#Player 2 give up
		if input2 == "n":
			run2 = False
			
		#if both players give up
		if run1 == False and run2 == False:
			if point1 > point2:
				print "Player 1 wins !"
				break
			if point2 > point1:
				print "Player 2 wins ! "
				break
			if point1 == point2:
				print "Player 1 and player 2 have the same points "
				print "Tie !"
				break
	
