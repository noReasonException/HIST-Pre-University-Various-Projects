from Tkinter import *
import ScrolledText
import tkMessageBox
import Tkinter
import sys
import os
def Files_Communicate_in(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def Save_Logs():
    Configfile=open('Configpass.pmsf')
    lines=Configfile.readlines()
    Pass = lines[0]
    Userinput = textpass.get()
    if(Userinput == Pass):
        TEXT = MainText.get('1.0', END+'-1c')
        Log = open("Logs.txt", "wb")
        Log.write(TEXT);
        Log.close()
    else:
        tkMessageBox.showinfo("Warning","Invalid Password")


def Load_Logs():
    Configfile=open('Configpass.pmsf')
    lines=Configfile.readlines()
    Pass = lines[0]
    Userinput = textpass.get()
    if(Userinput == Pass):
        Logfile = open("Logs.txt")
        Logs = Logfile.read()
        MainText.insert('1.0',Logs)
        Logfile.close()
    else:
        tkMessageBox.showinfo("Warning","Invalid Password")
def Change_Password():
    def Config_Save():
        lines = open("Configpass.pmsf", 'r').readlines()
        lines[0] = passnew.get()
        out = open("Configpass.pmsf", 'w')
        out.writelines(lines)
        out.close()
    tkMessageBox.showinfo("Information","Some Settings need restart of Password Manager")
    root = Tk()
    labelpass = Label(root, text="Enter Password")
    labelpass.pack( side = TOP)
    passnew = Entry(root, bd =8,)
    passnew.pack(side = TOP)
    button = Button(root, text="Save", command= Config_Save)
    button.pack(side = TOP)
    root.mainloop
def Change_Bg_Color():
    def Config_Save(text):
        lines = open("Config.pmsf", 'r').readlines()
        lines[0] = text
        out = open("Config.pmsf", 'w')
        out.writelines(lines)
        out.close()
    def RED():
        background = "RED"
        textColor = ""
        root.configure(bg=background)
        Config_Save("red")
    def BLUE():
        background = "BLUE"
        textColor = ""
        root.configure(bg=background)
        Config_Save("blue")
    def ORANGE():
        background = "ORANGE"
        textColor = ""
        root.configure(bg=background)
        Config_Save("orange")
    def BLACK():
        background = "BLACK"
        textColor = ""
        root.configure(bg=background)
        Config_Save("black")
    def GREY():
        background = "GREY"
        textColor = ""
        root.configure(bg=background)
        Config_Save("GREY")
    tkMessageBox.showinfo("Information","Some Settings need restart of Password Manager")
    top = Tk()
    top.title("Backround Color")
    A = Tkinter.Button(top, text ="Red      ", command = RED,fg="red")
    A.pack(side = LEFT)
    B = Tkinter.Button(top, text ="Blue     ", command = BLUE,fg="blue")
    B.pack(side = RIGHT)
    C = Tkinter.Button(top, text ="Orange", command = ORANGE,fg="Orange")
    C.pack(side = BOTTOM)
    D = Tkinter.Button(top, text ="Black    ", command = BLACK,fg="Black")
    D.pack(side = TOP)
    E = Tkinter.Button(top, text ="Silver  ", command = GREY,fg="GREY")
    E.pack()
    top.mainloop
def View_Config_File():
    tkMessageBox.showinfo("Warning","Open with notepad")
    os.startfile("Config.pmsf")

def Help():
    tkMessageBox.showinfo("Help","""This software is a safe Password Manager programm
You can save your passwords and othrer personal data with safe....
""")

def About():
    tkMessageBox.showinfo("About","""
Password Manager
Version 1.0
By El Sonador
""")
def Exit():
    sys.exit()

root = Tk()
root.title("Password Manager v1")
root["padx"] = 30
root["pady"] = 30
Configfile=open('Config.pmsf')
lines=Configfile.readlines()
Background = lines[0]
root.configure(bg=Background)
MainText = ScrolledText.ScrolledText(root,bd=5,bg="white",font="arial",width=70, height=30)
MainText.pack(side = LEFT)
labelpass = Label(root, text="Enter Password")
labelpass.pack( side = TOP)
textpass = Entry(root, bd =8,show="*")
textpass.pack(side = TOP)
load = Button(root, text="Load passwords   ", command=Load_Logs)
load.pack(side = TOP)
save = Button(root,text="Save Passwords    ",command=Save_Logs)
save.pack(side = TOP)
LAB = Label(root, text="----Password Manager Settings-----")
LAB.pack( side = TOP)
button = Button(root, text="Change password ", command=Change_Password)
button.pack(side = TOP)
button = Button(root, text="Change BG color   ", command=Change_Bg_Color)
button.pack(side = TOP)
button = Button(root, text="View config file     ", command=View_Config_File)
button.pack(side = TOP)
LAB = Label(root, text="-------Support and Credits-------")
LAB.pack( side = TOP)
button = Button(root, text="Help                         ", command=Help)
button.pack(side = TOP)
button = Button(root, text="About                      ", command=About)
button.pack(side = TOP)
button = Button(root, text="Exit                           ", command=Exit)
button.pack(side = TOP)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Choices", menu=filemenu)
filemenu.add_command(label="Exit",command=Exit)
#----------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=Help)
helpmenu.add_command(label="About...", command=About)
#----------------------------------------------------
root.config(menu=menubar)
root.mainloop()








