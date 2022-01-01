from Tkinter import *
import Tkinter
import webbrowser
import tkMessageBox
import time
def Set_link():
   global entryWidget
   if entryWidget.get().strip() == "":
        tkMessageBox.showerror("Message", "Enter a Link")
   else:
        tkMessageBox.showinfo("Message", "Link set = " + entryWidget.get().strip())
#----------------------------------------------------------------------------
def Time_Set():
 master = Tk()
 w = Scale(master, from_=0, to=100)
 w.pack()
 mainloop()
#----------------------------------------------------------------------------
def donothing():
   pass
#----------------------------------------------------------------------------
def Start_task():
    Task_run = True
    while Task_run == True:
     webbrowser.open(entryWidget.get().strip())
     time.sleep(w.get().strip()) #εδω εχω το πρόβλημα
#-----------------------------------------------------------------------------
def Kill_task():
   Task_run = False
   tkMessageBox.showinfo( "Message", "successfully stopped")
#-=-----------------------------------------------------------------------------
def Help():
   tkMessageBox.showinfo( "Help", "This programm calls every 5,10,15 or 20 seconds an link its Open Source and you can change it copy it whatever you want byt you cant sell it.......Enjoy :) :)")
#------------------------------------------------------------------------------
def About():
   tkMessageBox.showinfo( "About", "the N.M.C")
   tkMessageBox.showinfo( "About", "by Sebax")
   tkMessageBox.showinfo( "About", "version 1.0")
#------------------------------------------------------------------------------


root = Tk()
root.title("N.M.C")
root["padx"] = 40
root["pady"] = 20       
textFrame = Frame(root)
entryLabel = Label(textFrame)
entryLabel["text"] = "Enter the link:"
entryLabel.pack(side=LEFT)
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()
button = Button(root, text="Set Link", command=Set_link)
button.pack()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Action", menu=filemenu)
filemenu.add_command(label="Start", command=Start_task)
filemenu.add_command(label="Stop", command=Kill_task)
#------------------------------------------------------------------------------
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu=editmenu)
editmenu.add_command(label="Set Time", command=Time_Set)
#=----------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=Help)
helpmenu.add_command(label="About...", command=About)
helpmenu.add_command(label="Download updates",command=donothing)
#--------------------------------------------------------------------  
root.config(menu=menubar)
root.mainloop()
