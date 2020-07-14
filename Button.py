'''
    @This is the Button module for  Pacman
                                                             @BY kUTULL0
'''

import pygame
import Resources
pygame.init ()

#Button class for pacman
class Button ():

    def __init__ (self , surface, text="button", fonttype="comicsansms", x=210, y=145):
        self.surface = surface
        self.text = text
        self.font = pygame.font.SysFont(fonttype, 21)
        self.textColor = Resources.white
        self.textrander = self.font.render(str(self.text), True, self.textColor)
        self.x = (self.surface.get_width()/2) -(self.textrander.get_width()/2)
        self.y = y
        self.l = self.y+self.textrander.get_height()
        self.b = self.x+self.textrander.get_width()


    def OnHover (self ):
        (xpos,ypos)=pygame.mouse.get_pos()
        if (self.x < xpos < self.b) and (self.y < ypos < self.l):
            self.textColor = Resources.yellow
            return True
        else:
            self.textColor = (255, 255, 255)
            return False

    def on_click(self ):
        if self.OnHover()==True :
            self.textColor = (214, 214, 50)
            return True
        return False


    def draw (self):
        self.textrander = self.font.render(str(self.text), True, self.textColor)
        self.surface.blit(self.textrander, (self.x, self.y))
