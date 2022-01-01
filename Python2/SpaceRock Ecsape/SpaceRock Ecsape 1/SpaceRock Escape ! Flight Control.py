#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import os
def drawFrame():
	print """
   ___ _ _       _     _       ___            _             _ 
  / __\ (_) __ _| |__ | |_    / __\___  _ __ | |_ _ __ ___ | |
 / _\ | | |/ _` | '_ \| __|  / /  / _ \| '_ \| __| '__/ _ \| |
/ /   | | | (_| | | | | |_  / /__| (_) | | | | |_| | | (_) | |
\/    |_|_|\__, |_| |_|\__| \____/\___/|_| |_|\__|_|  \___/|_|
           |___/                                                                                                                                   
				For SpaceRock Escape!
				Written by El_Sonador
"""

root = Tk()


position = 6
def save(logs):
	savefile = open("move.txt","w")
	savefile.write(str(logs))
	savefile.close

def callback(event):
    frame.focus_set()
    x = event.x
    y = event.y
    if int(y) < 50:
		global position
		position = position + 1
		if position > 11:
			position = position - 1
		if position < 0:
			position = position + 1
		save(position)
		print "SpaceShip Position :",position
    if int(y) > 50:
		global position
		position = position - 1
		if position > 11:
			position = position - 1
		if position < 0:
			position = position + 1
		save(position)
		print "SpaceShip Position :",position
		
	

drawFrame()
frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
