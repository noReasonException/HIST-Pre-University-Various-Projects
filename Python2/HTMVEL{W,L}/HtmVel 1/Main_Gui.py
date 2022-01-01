from Tkinter import *
import ScrolledText
import tkFileDialog
import Tkinter
import tkMessageBox
import os
#-------------------------------------------------------------------------------
def Nothing():
    pass
def Help():
    tkMessageBox.showinfo("Help", "Hello and welcome to my html IDE v01 This simple IDE can help you to develop your website easy and without any problems in this version you can only save/load your file and of cource a quicly preview on it.If the commands copy-paste don't work you can do copy with Ctrl+C and paste with Ctrl+V")    
    print "Help Dialog  Created..........................|DONE|"
def About():
    tkMessageBox.showinfo("About..","HTMVEL version 01 By El_Sonador")
    print "About Dialog Created......................... |DONE|"
def Close():
    root.quit
def Open_file():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()
        print "Html File Saved as {user_choice}..........|DONE|"
def Save_and_run():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        data = self.textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
def fast_view():
   File = open("output.html", "wb")
   File.write(textPad.get(CURRENT, INSERT));
   File.close()
   print "Html File Saved as output.html.................|DONE|"
   os.startfile("output.html")
def Copy():
    pass
def Paste():
    pass
#----------------------------------------------------------------------------
root = Tkinter.Tk(className="Htmvel IDE v01")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="fast preview",command=fast_view)
filemenu.add_command(label="Save html file", command=Save_and_run)
filemenu.add_command(label="Open html file",command=Open_file)
filemenu.add_command(label="Exit", command=Close)
#=-----------------------------------------------------------------------------
setmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Settings",menu=setmenu)
setmenu.add_command(label="Copy",command=Nothing)
setmenu.add_command(label="Paste",command=Paste)
#=-----------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=Help)
helpmenu.add_command(label="About...", command=About)
#-----------------------------------------------------------------------------------
textPad = ScrolledText.ScrolledText(root,bd=5,bg="white",font="arial",width=160, height=70)
textPad.insert(INSERT, """<html>
<head>
<title> </title>
""")
textPad.pack()
root.config(menu=menubar)
root.mainloop()

