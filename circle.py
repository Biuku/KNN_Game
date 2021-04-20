""" April 20, 2021 """


import pygame
import math as m
import random as r
from setup.printr import Printr
from arr import Arr


class Circle(Arr):
    def __init__(self, win):
        super().__init__()
        pygame.init()
        self.win = win
        self.printr = Printr(self.win, self.set)

        ## Pixel units
        self.pixel_mid = [800, 400]
        self.pixel_radius = 110


        ## Array units
        self.arr_mid = (1, 1)
        self.arr_radius = 1


    def update(self, moving):
        self.move(moving)
        #self.update_coords(self):


    def update_coords(self):
        ## If I move recalculate everything ##
        self.convert()


    def draw(self):
        ## Draw perimeter of circle
        pygame.draw.circle(self.win, self.set.yellow, self.pixel_mid, self.pixel_radius, 3)

        ## Draw centre of circle
        pygame.draw.circle(self.win, self.set.yellow, self.pixel_mid, 5, 0)
        #self.printr.print_instructions(self.b0, self.b1, self.SSE, self.y_intercept, self.slope, self.sse)


    """ UPDATES """

    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my

    def convert(self):
        self.arr_mid = self.convert_to_arr(self.pixel_mid)
