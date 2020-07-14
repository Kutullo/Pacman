import pygame
import Resources
import random


from Images import image
from Levels import Lavel

vec=pygame.math.Vector2


class Ghost() :
    def __init__(self, main_surface, x=8, y=12, tile=Lavel("pac.txt"), ghost_img=image):
        self.main_surface  =main_surface
        self.pos = vec(x, y)
        self.grid = tile.listOfLines
        self.ghost_color = Resources.yellow
        self.direction = vec(0,0)
        self.currentdirection = vec(0,0)
        self.nextdirection = vec(0, 0)
        self.speed = 2
        self.level_speed = 2;
        self.radius = 10
        self.cell_height = 20
        self.cell_width = 20
        self.ghost_img = ghost_img
        #Ghost modes : scatter=1 ,chase=2 ,frightened =3
        self.mode =2
        #Animation image index for frightened ghost
        self.fright_count=0 ;


    def draw (self):
        if self.mode != 3:
            if self.direction == (0,0):
                pygame.draw.circle(self.main_surface, (self.ghost_color), ((int(self.pos.x )+10), (int(self.pos.y )+10) ), self.radius)
            if self.direction == (-1,0):
                self.main_surface.blit(self.ghost_img.left,(self.pos.x,self.pos.y) )
            if self.direction == (1, 0):
                self.main_surface.blit(self.ghost_img.right, (self.pos.x, self.pos.y))
            if self.direction == (0,-1):
                self.main_surface.blit(self.ghost_img.up, (self.pos.x, self.pos.y))
            if self.direction == (0, 1):
                self.main_surface.blit(self.ghost_img.down, (self.pos.x, self.pos.y))
        else:

            if self.fright_count >= 30:
                self.fright_count = 0

            self.main_surface.blit(Resources.fightAmn[self.fright_count//15], (self.pos.x, self.pos.y))
            self.fright_count += 1
        pygame.display.update()

    #Moves the Ghost in the direction given
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

        if self.mode == 3:
            self.speed=0.5
        else:
            self.speed = self.level_speed

        if self.mode ==1 :
            self.scatter_mode(x,y)
        elif self.mode==2:
            self.chase_mode(x,y,direction)
        elif self.mode==3:
            self.frighened_mode()

    def ghost_movement(self, x, y):
        x_right = (self.pos.x / self.cell_width + 1)
        x_left = (self.pos.x / self.cell_width - 1)
        y_down = (self.pos.y / self.cell_height + 1)
        y_up = (self.pos.y / self.cell_height - 1)


        if self.direction == vec(-1, 0):

            if abs(y_down - int(y)) <= abs(y_up - int(y)):
                self.nextdirection = vec(0, 1)
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(0, -1)

            if abs(y_down - int(y)) > abs(y_up - int(y)):
                self.nextdirection = vec(0, -1)
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(0, 1)

            if abs(y_down - int(y)) == abs(y_up - int(y)) and self.collusion(self.direction):
                self.nextdirection = vec(0, -1)
                if self.collusion(self.nextdirection):
                    self.nextdirection = vec(0, 1)

        if self.direction == vec(1, 0):

            if abs(y_down - int(y)) < abs(y_up - int(y)):
                self.nextdirection = vec(0, 1)
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(0, -1)

            if abs(y_down - int(y)) > abs(y_up - int(y)):
                self.nextdirection = vec(0, -1)
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(0, 1)

            if abs(y_down - int(y)) == abs(y_up - int(y)) and self.collusion(self.direction):
                self.nextdirection = vec(0, -1)
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(0, 1)

        if self.direction == vec(0, 1):

            if abs(x_right - int(x)) < abs(x_left - int(x)):
                self.nextdirection = vec(1, 0)
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(-1, 0)

            if abs(x_right - int(x)) > abs(x_left - int(x)):
                self.move(vec(-1, 0))
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(1, 0)

            if abs(x_right - int(x)) == abs(x_left - int(x)) and self.collusion(self.direction):
                self.nextdirection = vec(-1, 0)
                if self.collusion(self.nextdirection):
                    self.nextdirection = vec(1, 0)

        if self.direction == vec(0, -1):

            if abs(x_right - int(x)) < abs(x_left - int(x)):
                self.nextdirection = vec(1, 0)
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(-1, 0)

            if abs(x_right - int(x)) > abs(x_left - int(x)):
                self.nextdirection = vec(-1, 0)
                if self.collusion(self.nextdirection) and self.collusion(self.direction):
                    self.nextdirection = vec(1, 0)

            if abs(x_right - int(x)) == abs(x_left - int(x)) and self.collusion(self.direction):
                self.nextdirection = vec(-1, 0)
                if self.collusion(self.nextdirection):
                    self.nextdirection = vec(1, 0)

        print(self.pos.x / 20, self.pos.y / 20)

    def collusion(self, direction=vec(0,0)):

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

    #Ghost pursuing Pacman
    def chase_mode (self, x, y, direction=vec(0, 0)):
        pass

    def scatter_mode (self, x, y):
        pass

    def frighened_mode(self):

        if self.direction==vec(0, 1) or self.direction == vec(0, -1):
            pos_x=random.randrange(2)

            if pos_x is 0:
                self.nextdirection = vec(1, 0)
            else:
                self.nextdirection = vec(-1, 0)

        if self.direction == vec(-1, 0) or self.direction == vec(1, 0):
            pos_y = random.randrange(2)

            if pos_y is 0:
                self.nextdirection = vec(0, 1)
            else:
                self.nextdirection = vec(0, -1)





class Blinky (Ghost):
    def __init__(self, main_surface, x1=8, y1=12, tile=Lavel("pac.txt"), image = (image)):
        super().__init__(main_surface, x1, y1, tile, image)
        self.move(vec(-1, 0))


    #Ghost pursuing Pacman
    def chase_mode(self, x, y, direction=vec(0, 0)):
        self.ghost_movement(x, y)

    def scatter_mode (self, x, y):
        self.ghost_movement(26, 1)
        if self.pos.x/self.cell_width == 26 and self.pos.y/self.cell_height == 1:
            self.ghost_movement(21, 5)


class Pinky (Ghost):
    def __init__(self, main_surface, x1=8, y1=12, tile=Lavel("pac.txt"), image=(image)):
        super().__init__(main_surface, x1, y1, tile, image)

        self.move(vec(-1, 0))

    #Ghost pursuing Pacman
    def chase_mode (self,x,y,direction=vec(0,0)):

        if direction == (-1, 0):
            self.ghost_movement(x-4, y)

        if direction == (1, 0):
            self.ghost_movement(x+4, y)

        if direction== (0,1):
            self.ghost_movement(x, y+4)

        if direction == (0,-1):
            self.ghost_movement(x-4, y - 4)
        if direction == (0, 0):
            self.ghost_movement(x - 4, y)


    def scatter_mode (self,x,y):
        self.ghost_movement(6, 1)

        if self.pos.x/self.cell_width==6 and self.pos.y/self.cell_height==1:
            self.ghost_movement(1, 5)


class Clyde (Ghost):
    def __init__(self, main_surface, x1=8, y1=12, tile=Lavel("pac.txt"), image=(image)):
        super().__init__(main_surface, x1, y1, tile, image)
        self.move(vec(-1, 0))


    def chase_mode (self, x, y, direction=vec(0, 0)):

        x_pos = (self.pos.x / self.cell_width)
        y_pos = (self.pos.y / self.cell_height)

        if (abs(x_pos-x) + abs(y_pos-y)) > 8:
            self.ghost_movement(x, y)
        else:
            self.scatter_mode(x, y)


    def scatter_mode (self,x,y):
        self.ghost_movement(6, 26)

        if self.pos.x/self.cell_width == 26 and self.pos.y/self.cell_height == 1:
            self.ghost_movement(9, 26)


class Inky(Ghost):
    def __init__(self, main_surface, x1=8, y1=12, tile=Lavel("pac.txt"), image=(image)):
        super().__init__(main_surface, x1, y1, tile, image)
        self.move(vec(-1, 0))
        self.blinky_pos_x = 0
        self.blinky_pos_y = 0
        self.new_x = 0
        self.new_y = 0

    def chase_mode(self, x, y, direction=vec(0, 0)):


        trans=2 #translation of new point from pacman
        new_y=0
        new_x=0

        #left
        if direction == (-1, 0):
            x -= trans
            #Distance from Pacman to Blinky
            x_length = x - int(self.blinky_pos_x)
            y_lemgth = y - int(self.blinky_pos_y)

            #Calculate new cord
            new_x = x+x_length
            new_y = y+y_lemgth

            self.ghost_movement(new_x, new_y)

        #right
        if direction == (1, 0):

            x += trans

            # Distance from Pacman to Blinky
            x_length = x - int(self.blinky_pos_x)
            y_lemgth = y - int(self.blinky_pos_y)

            # Calculate new cord
            new_x = x + x_length
            new_y = y + y_lemgth

            self.ghost_movement(new_x, new_y)

        #dowm
        if direction == (0, 1):

            y += trans
            # Distance from Pacman to Blinky
            x_length = x - int(self.blinky_pos_x)
            y_lemgth = y - int(self.blinky_pos_y)

            # Calculate new cord
            new_x = x + x_length
            new_y = y + y_lemgth

            self.ghost_movement(new_x, new_y)

        #up
        if direction == (0, -1):

            y -= trans

            # Distance from Pacman to Blinky
            x_length = x - int(self.blinky_pos_x)
            y_lemgth = y - int(self.blinky_pos_y)

            # Calculate new cord
            new_x = x + x_length
            new_y = y + y_lemgth

            self.ghost_movement(new_x, new_y)

        #stationary
        if direction == (0, 0):
            self.ghost_movement(x - 4, y)



    def scatter_mode(self, x, y):
        self.ghost_movement(24, 26)