""" April 21, 2021 """


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
        self.radius = 110

        ## Array units
        self.convert()


    def update(self, moving):
        self.move(moving)


    def draw(self, win_w, win_h):
        self.draw_circle()
        self.printr.print_instructions(self.K, win_w, win_h)


    def draw_circle(self):
        c1 = self.set.ultra_light_grey
        c2 = self.set.light_grey

        pygame.draw.circle(self.win, c1, self.pixel_mid, self.radius, 1)
        pygame.draw.circle(self.win, c2, self.pixel_mid, 5, 0)

        self.draw_circle_coord()

    def draw_circle_coord(self):


        px_x, px_y = self.pixel_mid
        arr_x, arr_y = self.arr_mid

        arr_x = "Fare: £" + str( int(arr_x) )
        arr_y = "Age: " + str( int(arr_y) )
        px_coord = "(" + str(px_x) + ", " + str(px_y) + ")"

        y = px_y - 15
        x = px_x + self.radius + 12

        ## Draw white rect
        pygame.draw.rect(self.win, self.set.background, pygame.Rect(x-5, y, 60, 30), 0)

        self.printr.coord_printr(arr_x, x, y, self.set.grey)
        self.printr.coord_printr(arr_y, x, y + 15, self.set.grey)
        #self.printr.coord_printr(px_coord, px_x+10, y + 30, self.set.blue)


    """ UPDATES """

    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my

            self.convert()

    def convert(self):
        norm_arr_mid = self.convert_to_arr(self.pixel_mid)
        self.arr_mid = self.convert_norm_arr_to_arr(norm_arr_mid)
