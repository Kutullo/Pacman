import pygame
import Resources
import random


from Images import image
from Levels import Lavel

vec=pygame.math.Vector2

#Loading players images


class Player() :
    def __init__(self,main_surface,x=8,y=12,tile=Lavel,player_img= image):
        self.main_surface=main_surface
        self.pos=vec(x,y)
        self.grid =tile.listOfLines
        self.player_color=Resources.yellow
        self.direction =vec(0,0)
        self.currentdirection =vec(0,0)
        self.nextdirection = vec(0, 0)
        self.speed = 2
        self.level_speed = 2;
        self.radius = 10
        self.cell_height = 20
        self.cell_width = 20
        self.player_img = player_img
        #Animation index for pacmn
        self.pac_count = 0
        self.prev_pos = vec(0, 0)

    def draw(self):
        #pacman animation image count
        if self.pac_count >= 20:
            self.pac_count = 0

        #if pac hits  a wall or is static,dont animate ...else animate
        if self.collusion(self.direction):
            self.drawImage()
        else:

            if self.pac_count//10 == 0:
                self.drawImage()
            if self.pac_count//10 == 1:
                pygame.draw.circle(self.main_surface, (self.player_color),
                                   ((int(self.pos.x) + 10), (int(self.pos.y) + 10)),
                                   self.radius)
        #animation count
        self.pac_count += 1

        pygame.display.update()

    def drawImage(self):
        if self.direction == (0, 0):
            pygame.draw.circle(self.main_surface, (self.player_color), ((int(self.pos.x) + 10), (int(self.pos.y) + 10)),
                               self.radius)
        if self.direction == (-1, 0):
            self.main_surface.blit(self.player_img.left, (self.pos.x, self.pos.y))
        if self.direction == (1, 0):
            self.main_surface.blit(self.player_img.right, (self.pos.x, self.pos.y))
        if self.direction == (0, -1):
            self.main_surface.blit(self.player_img.up, (self.pos.x, self.pos.y))
        if self.direction == (0, 1):
            self.main_surface.blit(self.player_img.down, (self.pos.x, self.pos.y))
        self.prev_pos = self.pos

    def move(self, direction=vec(0, 0)):
        self.nextdirection = direction

    def update(self):

        if not self.collusion(self.direction):
            self.pos += self.direction*self.speed

        if self.pos.x % 20 == 0 and self.pos.y % 20 == 0 :
            if not self.collusion(self.nextdirection):
                self.currentdirection=self.nextdirection

        if self.pos.x % 20 == 0:
            if self.direction == (1, 0) or self.direction == (-1, 0):
                self.direction = self.currentdirection


        if self.pos.y  % 20 == 0:
            if self.direction == (0, 1) or self.direction == (0, -1):
                self.direction = self.currentdirection

        if self.direction==vec(0,0):
            self.direction = self.currentdirection

    def logic(self, x=0, y=0, direction=vec(0, 0)):
        self.speed=self.level_speed
        pass

    def collusion(self, direction=vec(0, 0)):
        nextdirection = vec(0, 0)
        nextdirection = self.pos + direction*self.speed

        # Wall collusion detection from up and left direction
        if direction==vec(-1,0)  or  direction==vec(0,-1):
            if self.grid[int(nextdirection.y / 20)][int(nextdirection.x / 20)] == 1:
                return True

      # Wall collusion detection from right and down direction
        if direction==vec(1, 0):
            if self.pos.x % 20 == 0:
                if self.grid[int(nextdirection.y / 20)][int(nextdirection.x / 20)+1] == 1:
                    return True

        if direction==vec(0, 1):
            if self.pos.y % 20 == 0:
                if self.grid[int(nextdirection.y / 20)+1][int(nextdirection.x / 20)] == 1:
                    return True

        return False







