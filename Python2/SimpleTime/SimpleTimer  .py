#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
def drawframe(s,m,h):
	os.system("clear")
	print """
 _____ _                 _        _____ _                     
/  ___(_)               | |      |_   _(_)                    
\ `--. _ _ __ ___  _ __ | | ___    | |  _ _ __ ___   ___ _ __ 
 `--. \ | '_ ` _ \| '_ \| |/ _ \   | | | | '_ ` _ \ / _ \ '__|
/\__/ / | | | | | | |_) | |  __/   | | | | | | | | |  __/ |   
\____/|_|_| |_| |_| .__/|_|\___|   \_/ |_|_| |_| |_|\___|_|   
                  | |                                         
                  |_|                                         
Coded By El_Sonador

"""
	print "+------------------------------------------------+"
	print "| Seconds 		Minutes		Hours    +"
	print "|["+s+"]			["+m+"]             ["+h+"]      +"
	print "+------------------------------------------------+"
	
sv = 0
mv = 0
hv = 0
while True:
	sv = sv + 1
	time.sleep(1)
	drawframe(str(sv),str(mv),str(hv))
	if sv == 59:
		sv = 0
		mv = mv + 1
		if mv == 59:
			mv = 0
			hv = hv + 1
	
