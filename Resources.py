'''
    @This is the resource module for  Pacman
    @Resources such as Images,audio ,color settings
    will be loaded/stored/assigned  on this class
                                                             @BY kUTULL0
'''

import pygame
from Levels import Lavel

pygame.init()

#color settings
blue = (0, 0, 250)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
pink =(250, 105, 180)
cyan = (0, 171, 169)
amber = (240, 163, 10)

#Images of the game Level
gridImg =pygame.image.load("images/background.png")
menuImg =pygame.image.load("images/menu.jpg")
frightImg1 = pygame.image.load("images/frightened/fright1.png")
frightImg1 = pygame.transform.scale(frightImg1, (20, 20))
frightImg2 = pygame.image.load("images/frightened/fright2.png")
frightImg2 = pygame.transform.scale(frightImg2, (20, 20))
fightAmn = [frightImg1, frightImg2]


#Rendering text
def text(str ="text here", size=18, color=(white)):
    font = pygame.font.SysFont("comicsansms", size)
    fontrander=font.render(str, True, color)
    return fontrander


