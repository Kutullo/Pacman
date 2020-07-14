
import  pygame
import Resources
import Player
import math
import threading


from Player import Player
from Ghosts import Blinky
from Ghosts import Pinky
from Ghosts import Clyde
from Ghosts import Inky

from Images import image
from Levels import Lavel



vec=pygame.math.Vector2


#Loading Game  images
pacmanImg =image ("images/Pacman","Pacman_L.png","Pacman_R.png","Pacman_U.png","Pacman_D.png")
blinkyImg =image ("images/Blinky","Blinky_L.png","Blinky_R.png","Blinky_U.png","Blinky_D.png")
pinkyImg =image ("images/Pinky","Pinky_L.png","Pinky_R.png","Pinky_U.png","Pinky_D.png")
clydeImg =image ("images/Clyde","Clyde_L.png","Clyde_R.png","Clyde_U.png","Clyde_D.png")
inkyImg =image ("images/Inky","Inky_L.png","Inky_R.png","Inky_U.png","Inky_D.png")

#Levels of the game
Lvl1 = Lavel("pac.txt")

class Game ():

    def __init__(self,surface,width=480,height=960,tile=Lavel("pac.txt")):
        # initializ

        self.main_surface=surface
        self.surface_width=width
        self.surface_height=height
        self.cell_width = 20
        self.cell_height = 20
        self.gamestate = 'Play'
        self.exitgame = False
        self.levelTile =tile.listOfLines
        Resources.gridImg=pygame.transform.scale(Resources.gridImg,(560,620))
        self.speed = 4 # speed per px
        self.score = 0
        self.fps =100
        self.scrfont = pygame.font.SysFont("comicsansms", 16)
        self.scorefont = pygame.font.SysFont("comicsansms", 16)
        self.played = False


        self.player = Player(surface, 14 * self.cell_width, 23 * self.cell_height,tile,pacmanImg)
        self.blinky = Blinky(surface,12* self.cell_width, 11 * self.cell_height,tile,blinkyImg)
        self.pinky = Pinky(surface, 12 * self.cell_width, 11 * self.cell_height, tile, pinkyImg)
        self.clyde = Clyde(surface, 15 * self.cell_width, 11 * self.cell_height, tile, clydeImg)
        self.inky = Inky(surface, 15 * self.cell_width, 11 * self.cell_height, tile, inkyImg)

        self.font = pygame.font.SysFont("arial", 14)


    def gameInputs(self):

        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            self.exitgame = True

        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key ==pygame.K_LEFT :
                self.player.move(vec(-1,0))
            if key ==pygame.K_RIGHT :
                self.player.move(vec(1, 0))
            if key == pygame.K_UP :
                self.player.move(vec(0, -1))
            if key == pygame.K_DOWN:
                self.player.move (vec(0, 1))




    def move(self):
        pass


    def logic(self):

        if self.player.pos.x % 20 == 0 and self.player.pos.y % 20 == 0:

            self.blinky.logic(self.player.pos.x/self.cell_width, self.player.pos.y / self.cell_height)
            self.pinky.logic(self.player.pos.x / self.cell_width, self.player.pos.y / self.cell_height, self.player.direction)
            self.clyde.logic(self.player.pos.x / self.cell_width, self.player.pos.y / self.cell_height)

            self.inky.blinky_pos_x = self.blinky.pos.x/self.cell_width
            self.inky.blinky_pos_y = self.blinky.pos.y/self.cell_height
            self.inky.logic(self.player.pos.x / self.cell_width, self.player.pos.y / self.cell_height, self.player.direction)


            if self.levelTile[int (self.player.pos.y /20)][int (self.player.pos.x /20)] ==2:
                self.levelTile[int(self.player.pos.y / 20)][int(self.player.pos.x / 20)] = 0
                self.score += 10


            if self.levelTile[int(self.player.pos.y / 20)][int(self.player.pos.x / 20)] == 3:
                self.levelTile[int(self.player.pos.y / 20)][int(self.player.pos.x / 20)] = 0
                self.score += 50

                self.inky.mode = 3
                self.clyde.mode = 3
                self.pinky.mode = 3
                self.blinky.mode = 3












    def update (self):
        self.player.update()
        self.blinky.update()
        self.pinky.update()
        self.inky.update()
        self.clyde.update()
        pass



    def draw(self):
        count=0
        print (len(self.levelTile))
        print(len(self.levelTile[0]))

        self.main_surface.blit(Resources.gridImg, (0, 0))

        for i in range(len(self.levelTile)):
            for j in range(len(self.levelTile[0])):

                if self.levelTile[i][j]==2:
                     pygame.draw.circle(self.main_surface,(Resources.white),(30+(j-1)*self.cell_width,30+(i-1)*self.cell_height),2)
                if self.levelTile[i][j] == 3:
                    pygame.draw.circle(self.main_surface, (Resources.white), (30 + (j - 1) * self.cell_width, 30 + (i - 1) * self.cell_height), 7)


        #draws the players pos
        self.player.draw()
        self.inky.draw()
        self.clyde.draw()
        self.pinky.draw()
        self.blinky.draw()


        score_text = self.scrfont.render("SCORE :", True, Resources.white)
        self.main_surface.blit(score_text, (20, 622))

        pygame.draw.rect(self.main_surface,(0,0,0),(score_text.get_width()+20,622,50,25))
        score_value= self.scorefont.render(str(self.score), True, Resources.yellow)
        self.main_surface.blit(score_value, (score_text.get_width()+25, 622))
        pygame.display.update()








