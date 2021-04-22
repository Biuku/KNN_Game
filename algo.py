""" April 22, 2021 """


import pygame
import math as m
from setup.printr import Printr
from arr import Arr


class Algo(Arr):
    def __init__(self, win):
        super().__init__()
        pygame.init()
        self.win = win
        self.printr = Printr(self.win)

        self.K = 5

        ### Circle ###
        #Pixel units
        self.pixel_mid = [800, 400]
        self.pixel_radius = 110

        # Array units
        self.arr_radius = 1
        self.convert()


    def update(self, moving):
        self.move(moving)


    """ UPDATES """

    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my

            self.convert()

    def convert(self):
        self.arr_mid = self.convert_to_arr(self.pixel_mid)
