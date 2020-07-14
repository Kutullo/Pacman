import pygame
pygame.init ()

#bliting an array of images with their directins
class image ():

    def __init__(self, path, left, right, up, down):
        self.left = pygame.image.load(path+"/"+left)
        self.left = pygame.transform.scale(self.left, (20, 20))
        self.right = pygame.image.load(path + "/" + right)
        self.right = pygame.transform.scale(self.right, (20, 20))
        self.up = pygame.image.load(path + "/" + up)
        self.up = pygame.transform.scale(self.up, (20, 20))
        self.down = pygame.image.load(path + "/" + down)
        self.down = pygame.transform.scale(self.down, (20, 20))