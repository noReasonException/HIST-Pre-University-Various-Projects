#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Εισαγωγή βιβλιοθηκών
import time
import os
#Παρουσίαση
def draw ():
	os.system("cls")
	print """
    ____        __       __       ________              __  
   / __ )____ _/ /______/ /_     / ____/ /_  ___  _____/ /__
  / __  / __ `/ __/ ___/ __ \   / /   / __ \/ _ \/ ___/ //_/
 / /_/ / /_/ / /_/ /__/ / / /  / /___/ / / /  __/ /__/ ,<   
/_____/\__,_/\__/\___/_/ /_/   \____/_/ /_/\___/\___/_/|_|  
    
+-----------------------------------------------------------+
BatchCheck Version 0.01
Written by El_Sonador
"""
#Κεντρικός βρόνχος
while True:
	draw()
	usrinput = raw_input("Enter the Batch file name ~ ")
	filename = usrinput + ".bat"
	try:#Ελενχος αν το αρχειο υπάρχει
		Open = open (filename, "r")
	except:
		filename = usrinput + ".cmd"
		try:
			Open = open (filename , "r")
		except:
			print "File not found .. input the name without file excension"
			time.sleep(2)
			continue
			
		else:
			pass
	else:
		pass 
	#Διάβασμα και απόδοση περιεχόμενου αρχείου σε μεταβλητή
	Logs = Open.read()
	warnings = 0
	linecount = -1
	reportlist = []
	#Ελενχος
	while True:
		linecount = linecount + 1 #Μετρητής θέσης
		del_command_count = linecount + 3 #Μεταβλητή διαβάσματος λέξης del{μαζί και με την linecount}
		format_command_count = linecount + 6#Μεταβλητή διαβάσματος λέξης format{μαζί και με την linecount}
		copy_command_count = linecount + 4#Μεταβλητή διαβάσματος λέξης copy{μαζί και με την linecount}
		xcopy_command_count = linecount + 5#Μεταβλητή διαβάσματος λέξης xcopy{μαζί και με την linecount}
		move_command_count = linecount + 4#Μεταβλητή διαβάσματος λέξης move{μαζί και με την linecount}
		attrib_command_count = linecount + 6#Μεταβλητή διαβάσματος λέξης attrib{μαζί και με την linecount}
		#Ελενχος επικύνδυνων εντολών
		if Logs[linecount : del_command_count] == "del":
			warnings = warnings + 1
			print "~del command found~"
			reportlist.append(" ~del command found~ ")
		if Logs[linecount : format_command_count] == "format":
			warnings = warnings + 1
			print "~format command found~"
			reportlist.append(" ~format command found~ ")
		if Logs[linecount : copy_command_count] == "copy":
			warnings = warnings + 1
			print "~copy command found~"
			reportlist.append(" ~copy command found~ ")
		if Logs[linecount : xcopy_command_count] == "xcopy":
			warnings = warnings + 1
			print "~xcopy command found~"
			reportlist.append(" ~xcopy command found~ ")
		if Logs[linecount : move_command_count] == "move":
			warnings = warnings + 1
			print "~move command found~"
			reportlist.append(" ~move command found~ ")
		if Logs[linecount : attrib_command_count] == "attrib":
			warnings = warnings + 1
			print "~attrib command found~"
			reportlist.append(" ~attrib command found~ ")
		if linecount > 200 and warnings > 0:
			print "Posible the file is virus"
			report_answer = raw_input("Do you want to make report.txt ?(y/n) ~ ")
			if report_answer == "y":
				Reportfile = open("Report.txt" , "w")
				#Εγραφή στο αρχείο την λίστα προβλημάτων
				for pos in reportlist:
					Reportfile.write(pos)	
				Reportfile.close
				print "Report created successful"
				#Εξοδος
				exitchoice = raw_input("Do you want to exit ?(y/n) ")
				if exitchoice == "y":
					Open.close()
					exit()
				if exitchoice == "n":
					Open.close()
					reportlist = []
					print "------------Restart----------------"
					time.sleep(1)
					draw()
					break
			#Εξοδος
			if report_answer == "n":
				exitchoice = raw_input("Do you want to exit ?(y/n) ")
				if exitchoice == "y":
					Open.close()
					exit()
				if exitchoice == "n":
					Open.close()
					reportlist = []
					print "------------Restart----------------"
					time.sleep(1)
					draw()
					break
				
		#Περίπτωση το αρχείο να είναι καθαρό		
		if linecount >200 and warnings == 0:
			print "The Batch File is Clear !"
			exitchoice = raw_input("Do you want to exit ?(y/n) ")
			if exitchoice == "y":
				Open.close()
				exit()
			if exitchoice == "n":
				Open.close()
				reportlist = []
				print "------------Restart----------------"
				time.sleep(1)
				draw()
				break
		
			
			
