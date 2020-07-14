
'''
    @The level class of Pacman
    @The class takes in 1 argument of the level *File path as a string type
        *File should be txt file
                                                @BY kUTULL0
'''

import pygame


class Lavel():

    # Init the level
    def __init__(self,path):
        self.path =path
        self.load(self.path)


    #Loads the path text file and creates 2d list

    def load(self,path):

        file = open ("pac.txt", "r")
        self.listOfLines=file.readlines()
        file.close()


        for i in range(len (self.listOfLines)):
            self.listOfLines[i]=self.listOfLines[i].strip()

        #convert the 2d list from str to int's
        for i in range(len (self.listOfLines)):
            self.listOfLines[i]=[int (i) for i in self.listOfLines[i]]

        print (self.listOfLines)




