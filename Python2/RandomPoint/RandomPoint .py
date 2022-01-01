#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import os
#Values

point = 0
times = 0
def welcomescreen():
	os.system("clear")
	print """
	______                _                  ______     _       _       
	| ___ \              | |                 | ___ \   (_)     | |      
	| |_/ /__ _ _ __   __| | ___  _ __ ___   | |_/ /__  _ _ __ | |_ ___ 
	|    // _` | '_ \ / _` |/ _ \| '_ ` _ \  |  __/ _ \| | '_ \| __/ __|
	| |\ \ (_| | | | | (_| | (_) | | | | | | | | | (_) | | | | | |_\__ \
             \_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_| \_|  \___/|_|_| |_|\__|___/
	
+-----------------------------+
|Welcome to RandomPoints 1.0  |
|Written by El_sonador        |
|Day : 21/11/2013             |
+-----------------------------+
"""                                     
      
def try_again():
	os.system("clear")
	print """
 _____             ___              _       
|_   _|           / _ \            (_)      
  | |_ __ _   _  / /_\ \ __ _  __ _ _ _ __  
  | | '__| | | | |  _  |/ _` |/ _` | | '_ \ 
  | | |  | |_| | | | | | (_| | (_| | | | | |
  \_/_|   \__, | \_| |_/\__, |\__,_|_|_| |_|
           __/ |         __/ |              
          |___/         |___/               
                         __                 
                      _ / /                 
                     (_) |                  
                       | |                  
                      _| |                  
                     (_) |                  
                        \_\   
"""
	print "Points > " + str(point)
	print "Times  > " + str(times)
                                            
                                
def success():
	os.system("clear")
	print"""
 _____                             _ 
/  ___|                           | |
\ `--. _   _  ___ ___ ___  ___ ___| |
 `--. \ | | |/ __/ __/ _ \/ __/ __| |
/\__/ / |_| | (_| (_|  __/\__ \__ \_|
\____/ \__,_|\___\___\___||___/___(_)
                                     
                                     
      __    __    __                 
      \ \   \ \   \ \                
     (_) | (_) | (_) |               
       | |   | |   | |               
      _| |  _| |  _| |               
     (_) | (_) | (_) |               
      /_/   /_/   /_/          
"""
	print "Points > " + str(point)
	print "Times  > " + str(times)      
                                          
                                                                    
def printmap(pos1,pos2,pos3):
	os.system("clear")
	print pos1 + pos2 +pos3
 




possibleobj = ["""
                         ,d88b.d88b,
                         88888888888
                         `Y8888888Y'
                           `Y888Y'
			     `Y'
""","""
		          +------+      
                          |`.    |`.   
                          |  `+--+---+   
                          |   |  |   |  
                          +---+--+   | 
                           `. |   `. |  
                             `+------+  
""","""
                            _________
                         _ /_|_____|_\ _
                           '. \   / .'
                             '.\ /.'
                               '.'
"""]

welcomescreen()
while True:
	x = raw_input("Enter for start or 'exit' for close > ")
	
	if x == "exit":
		break
	else:
		pass
	posible1 = random.randint(1,50)
	posible2 = random.randint(1,50)
	posible3 = random.randint(1,50)
	
	if posible1 > 0 and posible1 < 15:
		pos1 = possibleobj[0]
	if posible1 > 15 and posible1 < 35:
		pos1 = possibleobj[1]
	if posible1 > 35 and posible1 < 50:
		pos1 = possibleobj[2]
		
	if posible2 > 0 and posible2 < 15:
		pos2 = possibleobj[0]
	if posible2 > 15 and posible2 < 35:
		pos2 = possibleobj[1]
	if posible2 > 35 and posible2 < 50:
		pos2 = possibleobj[2]
		
	if posible3 > 0 and posible3 < 15:
		pos3 = possibleobj[0]
	if posible3 > 15 and posible3 < 35:
		pos3 = possibleobj[1]
	if posible3 > 35 and posible3 < 50:
		pos3 = possibleobj[2]
		
		
	printmap(pos1,pos2,pos3)
	
	
	if pos1 == pos2 == pos3:
		time.sleep(1)
		point = point + 1000
		success()
	else:
		time.sleep(1)
		point = point - 100
		try_again()
	
	
