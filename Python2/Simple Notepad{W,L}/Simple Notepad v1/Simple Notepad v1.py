from Tkinter import *
import tkMessageBox
import os
def donothing():
   pass
def save_file():
   File = open(E1.get().strip() + ".txt", "wb")
   File.write(entryWidget.get().strip());
   File.close()
   
def help_command():
   tkMessageBox.showinfo("Help", "A useful simple notepad for quick writing anything you want...")
   print "Create Win32 Gui Window <<Help>> ........[DONE]"
def about():
   tkMessageBox.showinfo("About", "Simple Notepad by El Sonador version 1.0")
   print "Create Win32 Gui Window <<About>> .......[DONE]"
   
root = Tk()
#--------------------------
L1 = Label(root, text="File name")
L1.pack( side = TOP)
E1 = Entry(root, bd =5)
E1.pack(side = TOP)
#----------------------------
background = "dark sea green"
textColor = "black"
root.configure(bg=background)
root.title("Simple Notepad v1")
root["padx"] = 50
root["pady"] = 50      
textFrame = Frame(root)
entryWidget = Entry(textFrame)
entryWidget["width"] = 100
entryWidget.pack(ipady = 100)
textFrame.pack()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save_file", command=save_file)
filemenu.add_command(label="Exit", command=root.quit)
#------------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=help_command)
helpmenu.add_command(label="About...", command=about)
helpmenu.add_command(label="Download updates",command=donothing)
#--------------------------------------------------------------------  
root.config(menu=menubar)
root.mainloop()
