from Tkinter import *
import Tkinter
import tkMessageBox
import os
def donothing():
   pass
def save_file():
   File = open(E.get() + ".txt", "wb")
   File.write(T.get(CURRENT, INSERT));
   File.close()
#-----------------------------------------------------------------------------   
def help_command():
   tkMessageBox.showinfo("Help", "A useful simple notepad for quick writing anything you want...")
   print "Create Win32 Gui Window <<Help>> ........[DONE]"
#-----------------------------------------------------------------------------
def about():
   tkMessageBox.showinfo("About", "Simple Notepad by El Sonador version 2.0")
   print "Create Win32 Gui Window <<About>> .......[DONE]"

root = Tk()   
L = Label(root, text="File name")
L.pack( side = TOP)
E = Entry(root, bd =5)
E.pack(side = TOP)
#-----------------------------------------------------------------------------
root.title("Simple Notepad v2") 
Scr = Tkinter.Scrollbar(root)
T = Tkinter.Text(root)
T.focus_set()
Scr.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
T.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
Scr.config(command=T.yview)
T.config(yscrollcommand=Scr.set)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save_file", command=save_file)
filemenu.add_command(label="Exit", command=root.quit)
#=-----------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=help_command)
helpmenu.add_command(label="About...", command=about)
helpmenu.add_command(label="Download updates",command=donothing)
#-----------------------------------------------------------------------------  
root.config(menu=menubar)
root.mainloop()
