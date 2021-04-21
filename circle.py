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
        self.printr = Printr(self.win)

        self.K = 5

        ## Pixel units
        self.pixel_mid = [800, 400]
        self.pixel_radius = 110

        ## Array units
        self.arr_radius = 1
        self.convert()
        #self.arr_mid = (1, 1)



    def update(self, moving):
        self.move(moving)


    def draw(self, win_w, win_h):
        self.draw_circle()
        self.printr.print_instructions(self.K, win_w, win_h)


    def draw_circle(self):
        c1 = self.set.ultra_light_grey
        c2 = self.set.light_grey

        pygame.draw.circle(self.win, c1, self.pixel_mid, 40, 0)
        # pygame.draw.circle(self.win, c1, self.pixel_mid, self.pixel_radius, 1)
        pygame.draw.circle(self.win, c2, self.pixel_mid, 5, 0)

        px_x, px_y = self.pixel_mid
        arr_x, arr_y = self.arr_mid

        arr_coord = "(" + str( round(arr_x, 2) ) + ", " + str( round(arr_y, 2) ) + ")"
        px_coord = "(" + str(px_x) + ", " + str(px_y) + ")"

        y = px_y - 15

        self.printr.coord_printr(arr_coord, px_x+10, y, self.set.grey)
        self.printr.coord_printr(px_coord, px_x+10, y + 15, self.set.blue)


    """ UPDATES """

    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my

            self.convert()

    def convert(self):
        self.arr_mid = self.convert_to_arr(self.pixel_mid)
