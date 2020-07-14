import pygame
import  Resources


from Game import Game
from Levels import Lavel
from Button import Button





displayhight =650
displaywidth=560
exitgame=False
gamestate='menu'


pygame.init ()
main_surface = pygame.display.set_mode((displaywidth,displayhight))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()

# The game objects from the GameClass
game =Game(main_surface,displaywidth,displayhight)

#Creating Buttons and texts for the game
start =Button(main_surface,'START GAME',"comicsansms",220,380)
about=Button(main_surface,'ABOUT',"comicsansms",220,425)
pacman_text =Resources.text('PACMAN',86,Resources.white)



#The main function
def main () :
    global exitgame,gamestate

    while not exitgame :


        if gamestate=='menu':

            Resources.menuImg=pygame.transform.scale(Resources.menuImg,(displaywidth,displayhight))
            main_surface.blit(Resources.menuImg, (0, 0))

            x_center =(displaywidth/2) -(pacman_text.get_width()/2)   # centering the text button
            #main_surface.blit(pacman_text, (x_center, 20))

            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exitgame = True
            if ev.type == pygame.MOUSEBUTTONDOWN:
                start.on_click()
            if ev.type == pygame.MOUSEBUTTONUP:
                if start.on_click():
                    gamestate = 'play'

            start.draw()
            start.OnHover()
            about.draw()
            about.OnHover()

        if gamestate == 'play':

            game.gameInputs()

            exitgame=game.exitgame
            game.logic()
            game.update()
            game.draw()




        pygame.display.update()
        clock.tick(80)

    pygame.quit()



if __name__=="__main__":
    main()
