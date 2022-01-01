import pygame
import sys
import time
import os

pygame.init()
size = (635,365)
black = 2, 6, 4
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HTMVEL v02 load in progress....")
ball = pygame.image.load("StartupLogo.gif")
ballrect = ball.get_rect()
screen.fill(black)
screen.blit(ball, ballrect)
pygame.display.flip()
time.sleep(5)
os.startfile("Main_Gui.py")
sys.exit()




