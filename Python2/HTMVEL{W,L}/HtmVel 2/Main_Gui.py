from Tkinter import *
import ScrolledText
import tkFileDialog
import Tkinter
import tkMessageBox
import os
#-------------------------------------------------------------------------------------------------------------
def Help():
    tkMessageBox.showinfo("Help", "Hello and welcome to my html IDE v02 This simple IDE can help you to develop your website easy and without any problems in this version you can only save/load your file and of cource a quicly preview on it.If the commands copy-paste don't work you can do copy with Ctrl+C and paste with Ctrl+V")    
    print "Help Dialog  Created..........................|DONE|"
def About():
    tkMessageBox.showinfo("About..","HTMVEL version 02 By El_Sonador")
    print "About Dialog Created......................... |DONE|"
def Close():
    sys.exit()
def Open():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()
        print "Html File Open .............|DONE|"
    else:
        print "Html File Open.............|ERROR|"
def Save():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        print "Html File Saved As {user choice}.........|DONE|"
    else:
        print "Html File Saved As {user choice}.........|ERROR|"
            
def Quick_Preview():
   File = open("Quick_Preview.html", "wb")
   File.write(textPad.get(CURRENT, INSERT));
   File.close()
   os.startfile("Quick_Preview.html")
   print "Html File Saved as Quick_Preview.html.....................|DONE|"
def Copy():
    pass
def Paste():
    pass
#-----------------------------------------------------------------------------------------------------------
root = Tkinter.Tk(className="Htmvel IDE v02")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Quick_Preview",command=Quick_Preview)
filemenu.add_separator()
filemenu.add_command(label="Save html file", command=Save)
filemenu.add_command(label="Open html file",command=Open)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Close)
#=----------------------------------------------------------------------------------------------------------
setmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Settings",menu=setmenu)
setmenu.add_command(label="Copy",command=Copy)
setmenu.add_command(label="Paste",command=Paste)
#=----------------------------------------------------------------------------------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=Help)
helpmenu.add_command(label="About...", command=About)
#-----------------------------------------------------------------------------------------------------------
textPad = ScrolledText.ScrolledText(root,bd=15,bg="white",font="arial",width=160, height=70)
textPad.insert(INSERT, """<html>
<head>
<title>MyPage</title>
""")
textPad.pack()
root.config(menu=menubar)
root.mainloop()

