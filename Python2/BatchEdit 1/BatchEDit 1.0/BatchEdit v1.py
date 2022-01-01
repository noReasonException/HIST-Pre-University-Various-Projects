from Tkinter import *
import ScrolledText
import tkFileDialog
import Tkinter
import tkMessageBox
import time
import os
#-------------------------------------------------------------------------------------------------------------
def Help():
    tkMessageBox.showinfo("Help", """
BatchEdit is a simple Batch IDE for quick develop
Scripts and programms easy and without the classic
notepad written in Python programming language
is a very Useful tool for every programmer
Easy to use
Simple interface
Quick Developing
""") 
def About():
    tkMessageBox.showinfo("About..","""
BatchEdit
Version 1.0
By El_Sonador
""")
def Close():
    sys.exit()
def Open():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a Script')
    if file != None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()
        print "Script Load"
    else:
        print "Error in script loading..."
def Save():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        print "Script Saved"
    else:
        print "Error in script saving.."
def Run():
   File = open("Script.bat", "wb")
   File.write(textPad.get(CURRENT, INSERT));
   File.close()
   os.startfile("Script.bat")
   print "Script.bat Run successful "
def Commands():
    COM = open("Commands.BE")
    commands = COM.read()
    top = Tk()
    top.title("Batch Commands")
    textPad = ScrolledText.ScrolledText(top,bd=5,bg="white",font="arial",width=100, height=30)
    textPad.insert(INSERT, commands)
    print "Commands Loaded"
    textPad.pack()
    top.mainloop()
def BatchHelp():
    os.startfile("BatchHelp.bat")
    print "BatchHelp Started "
#-----------------------------------------------------------------------------------------------------------
root = Tkinter.Tk()
root.title("BatchEdit Version 1.0")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save Script", command=Save)
filemenu.add_command(label="Open Script",command=Open)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Close)
#=----------------------------------------------------------------------------------------------------------
menubar.add_cascade(label="Run ",command=Run)
menubar.add_cascade(label="BatchHelp",command=BatchHelp)
#=----------------------------------------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Commands list", command=Commands)
helpmenu.add_command(label="Help", command=Help)
helpmenu.add_command(label="About...", command=About)
#-----------------------------------------------------------------------------------------------------------
textPad = ScrolledText.ScrolledText(root,bd=0,bg="white",font="arial",width=100, height=30)
textPad.insert(INSERT, """@Echo off
Title Test Script
Color 0A
echo hello world
pause >nul
""")
textPad.pack()
root.config(menu=menubar)
root.mainloop()

