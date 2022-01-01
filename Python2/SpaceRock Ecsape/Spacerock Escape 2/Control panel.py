import Tkinter
import tkMessageBox
top = Tkinter.Tk()

custom_value = 6

def UP():
      global custom_value
      if custom_value < 10 and custom_value > 0:
            with open("moves.txt","w") as write:
                  custom_value = custom_value + 1
                  write.write(str(custom_value))
      else:
            pass

def DOWN():
      global custom_value
      if custom_value < 10 and custom_value > 0:
            with open("moves.txt","w") as write:
                  custom_value = custom_value - 1
                  write.write(str(custom_value))
      else:
            pass

UP = Tkinter.Button(top, text ="-UP-", command = UP)
UP.pack()

DOWN = Tkinter.Button(top, text ="DOWN", command = DOWN)
DOWN.pack()

top.mainloop()
