import Tkinter
import tkMessageBox
from Tkinter import *

top = Tkinter.Tk()

def ADD():
   first = int(ENTRY1.get())
   second = int(ENTRY2.get())
   result = first + second
   tkMessageBox.showinfo("Result",str(first) + " + " + str(second) + " = " + str(result))
def REV():
   first = int(ENTRY1.get())
   second = int(ENTRY2.get())
   result = first - second
   tkMessageBox.showinfo("Result",str(first) + " - " + str(second) + " = " + str(result))
def MUL():
   first = int(ENTRY1.get())
   second = int(ENTRY2.get())
   result = first * second
   tkMessageBox.showinfo("Result",str(first) + " * " + str(second) + " = " + str(result))
def DIV():
   first = int(ENTRY1.get())
   second = int(ENTRY2.get())
   result = first / second
   tkMessageBox.showinfo("Result",str(first) + " / " + str(second) + " = " + str(result))

ENTRY1 = Entry(top, bd =5)

ENTRY1.pack(side = RIGHT)

ENTRY2 = Entry(top, bd =5)

ENTRY2.pack(side = LEFT)

ADD = Tkinter.Button(top, text =" + ", command = ADD)
ADD.pack()


REV = Tkinter.Button(top, text =" - ", command = REV)
REV.pack()


MUL = Tkinter.Button(top, text =" * ", command = MUL)
MUL.pack()


DIV = Tkinter.Button(top, text =" / ", command = DIV)
DIV.pack()



top.mainloop()
