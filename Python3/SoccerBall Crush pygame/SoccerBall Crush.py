import pygame
from pygame.locals import *
from sys import exit
#13/5/2014
windowsize = (1000,700)

def centerMessage(surface):
    return (windowsize[0] - surface.get_width()) / 2
def getQuit():
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
def main():
    pygame.init()
    surfacecolor = (0,0,0)
    screen = pygame.display.set_mode(windowsize,DOUBLEBUF,32)
    pygame.display.set_caption("Hello Pygame!")
    textfont = pygame.font.SysFont("Arial",48)
    thetext = textfont.render("Hello World!",True,(255,0,0),(255,255,0))
    """
    textx = centerMessage(thetext)
    texty = 40
    """
    x1 = 10
    y1 = 50
    x2 = 900
    y2 = 50
    way = True
    endprogramm = False
    while not endprogramm:
        ball = pygame.image.load("Soccer.png")
        screen.fill(surfacecolor)
        screen.blit(ball,(x1,y1))
        screen.blit(ball,(x2,y2))
        if way == True:
            x1 = x1 + 0.5
            x2 = x2 - 0.5
            if x1 > 900 or x2 < 10:
                way = False
        if way == False:
            x1 = x1 - 0.5
            x2 = x2 + 0.5
            if x2 > 900 or x1 < 10:
                way = True
        endprogramm=getQuit()
        pygame.display.update()
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
