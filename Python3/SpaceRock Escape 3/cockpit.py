import tkinter
top = tkinter.Tk()

custom_value_x = 5
custom_value_y = 2
fire = 0



def UP():
      global custom_value_x
      if custom_value_x < 10 and custom_value_x > 0:
            with open("movesx.txt","w") as write:
                  custom_value_x = custom_value_x - 1
                  write.write(str(custom_value_x))
def DOWN():
      global custom_value_x
      if custom_value_x < 10 and custom_value_x > 0:
            with open("movesx.txt","w") as write:
                  custom_value_x = custom_value_x + 1
                  write.write(str(custom_value_x))

def FRONT():
      global custom_value_y
      if custom_value_y < 10 and custom_value_y > 0:
            with open("movesy.txt","w") as write:
                  custom_value_y = custom_value_y + 1
                  write.write(str(custom_value_y))


def BACK():
      global custom_value_y
      if custom_value_y < 10 and custom_value_y > 0:
            with open("movesy.txt","w") as write:
                  custom_value_y = custom_value_y - 1
                  write.write(str(custom_value_y))

def FIRE():
      global fire
      with open("FIRE.txt","w") as write:
            fire = 1
            write.write(str(fire))






UP = tkinter.Button(top, text ="-UP-", command = UP)
UP.pack()
FRONT = tkinter.Button(top, text ="-FRONT-", command = FRONT)
FRONT.pack()
FIRE = tkinter.Button(top, text ="FIRE", command = FIRE)
FIRE.pack()
BACK = tkinter.Button(top, text ="BACK", command = BACK)
BACK.pack()
DOWN = tkinter.Button(top, text ="DOWN", command = DOWN)
DOWN.pack()



top.mainloop()
