from Tkinter import *
import tkMessageBox
import webbrowser
import Tkinter
import tkFont
import Image
import PIL
import os


#GUI SETTINGS BELOW
#Tk header
top = Tk()
#BACKROUND SETTINGS WINDOW 1
background = "ORANGE"
textColor = ""
top.configure(bg=background)
top.title("Image Resizer and Converter by El Sonador")
top["padx"] = 40
top["pady"] = 20
#FILE NAME ENTRY
A1 = Label(top, text="Fille name ==>")
A1.pack( side = LEFT)
B1 = Entry(top, bd =5)
B1.pack(side = LEFT)
#FILE TYPE ENTRY
A2 = Label(top, text="file type ==>")
A2.pack( side = LEFT)
B2 = Entry(top, bd =5)
B2.pack(side = LEFT)
#WIDTH VALUE ENTRY
A3 = Label(top, text=" <== width")
A3.pack( side = RIGHT)
B3 = Entry(top, bd =5)
B3.pack(side = RIGHT)
#HEIGHT VALUE ENTRY
A4 = Label(top, text="<== height")
A4.pack( side = RIGHT)
B4 = Entry(top, bd =5)
B4.pack(side = RIGHT)
#VALUES
width = B3.get()
height = B4.get()
#FUNCTIONS--------------
def Set_Viewer(): #HERE
    os.startfile("Details.py")
def Download_Updates():
    webbrowser.open("http://www.example.com")
def Download_Software():
    webbrowser.open("http://www.example.com")
def Action():
    im1 = Image.open(B1.get().strip())
    im2 = im1.resize((int(B3.get().strip()), int(B4.get().strip())), Image.NEAREST)  #HERE
    ext = B2.get().strip()
    im2.save("Output" + ext)
def Help():
    tkMessageBox.showinfo("Help", "this is useful program can magnify or shrink your image or even change the file extension of image .... source code is completely free and constantly updated located in site www.example.com")
def About():
    tkMessageBox.showinfo("About... ", "Version 2.0 Gui mode")
    tkMessageBox.showinfo("About... ", "By El Sonador")
#MENY SETTINGS 
menubar = Menu(top)
action_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="More..", menu = action_menu)
action_menu.add_command(label="Download more software by El sonador", command= Download_Software)
action_menu.add_command(label="Download updates", command= Download_Updates)
menubar.add_cascade(label="Image details", command = Set_Viewer)
menubar.add_cascade(label="Help", command = Help)
menubar.add_cascade(label="About", command = About)
menubar.add_cascade(label="Quit", command = top.quit)
#BUTTON IN WINDOW
Button = Tkinter.Button(top, text =" ==> Save changes <== ", command = Action)
Button.pack()
#TOP.MAINLOOP - CONFIG MENU{MENUBAR}
top.config(menu=menubar)
top.mainloop()



