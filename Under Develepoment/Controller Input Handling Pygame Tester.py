import pygame
import time
import os

pygame.init()
pygame.joystick.init()
try:
    controller1 = pygame.joystick.Joystick(0)
    controller1.init()
except:
    print ("Controller Not Intialised")
try:
    controller2 = pygame.joystick.Joystick(1)
    controller2.init()
    print ("DOUBLE CONTROLL DETECTED")
except:
    pass

while True:
    
    pygame.event.get()
    #GET AXIS
    AXIS_X_controller1 = controller1.get_axis(0) #AXIS_X
    AXIS_Y_controller1 = controller1.get_axis(1) #AXIS_Y
    print(str(AXIS_X_controller1))
    print (str(AXIS_Y_controller1))
    #GET_ID (pygame.joystick.Joystick.get_id)
    print("DEVICE ID > "+str(controller1.get_id()))
    #GET_NAME(pygame.joystick.Joystick.get_name)
    print ("DEVICE NAME" + str(controller1.get_name()))
    #GET NUM AXES(pygame.joystick.Joystick.get_numaxes)
    print ("NUMAXES > "+str(controller1.get_numaxes()))
    #GET BUTTON(pygame.joystick.Joystick.get_button)
    #for check in range(1,12):
        #print ("BUTTON" +str (check) + " > " + str(controller1.get_button(check)))
    time.sleep(1)
    os.system("cls")
