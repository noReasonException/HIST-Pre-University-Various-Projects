import tkinter
top = tkinter.Tk()

custom_value_x = 6
custom_value_y = 6

def UP():
      global custom_value_x
      if custom_value_x < 10 and custom_value_x > 0:
            with open("movesx.txt","w") as write:
                  custom_value_x = custom_value_x + 1
                  write.write(str(custom_value_x))
      else:
            pass

def DOWN():
      global custom_value_x
      if custom_value_x < 10 and custom_value_x > 0:
            with open("movesx.txt","w") as write:
                  custom_value_x = custom_value_x - 1
                  write.write(str(custom_value_x))
      else:
            pass

def FRONT():
      global custom_value_y
      if custom_value_y < 10 and custom_value_y > 0:
            with open("movesy.txt","w") as write:
                  custom_value_y = custom_value_y + 1
                  write.write(str(custom_value_y))
      else:
            pass

def BACK():
      global custom_value_y
      if custom_value_y < 10 and custom_value_y > 0:
            with open("movesy.txt","w") as write:
                  custom_value_y = custom_value_y - 1
                  write.write(str(custom_value_y))
      else:
            pass

UP = tkinter.Button(top, text ="-UP-", command = UP)
UP.pack()

DOWN = tkinter.Button(top, text ="DOWN", command = DOWN)
DOWN.pack()

UP = tkinter.Button(top, text ="-FRONT-", command = FRONT)
UP.pack()

DOWN = tkinter.Button(top, text ="BACK", command = BACK)
DOWN.pack()

top.mainloop()
