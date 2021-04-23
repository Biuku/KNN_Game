""" April 22, 2021 """


import pygame
import math as m
from setup.printr import Printr
from arr import Arr
from draw import Draw


class Algo(Arr):
    def __init__(self, win):
        super().__init__()
        pygame.init()
        self.win = win
        self.printr = Printr(self.win)

        self.draw = Draw(self.win, self.norm_arr, self.pixels)
        self.configure_draw()

        self.K = 5

        ### Circle ###
        #Pixel units
        self.pixel_mid = [800, 400]
        self.pixel_radius = 110

        # Array units
        self.arr_radius = 1
        self.convert()


    def knn(self):
        pass


    def configure_draw(self):
        self.draw.configure_scales(self.arr_scale, self.pixel_scale)


    def update(self, moving):
        self.move(moving)

    def draw_things(self, win_w, win_h):
        self.draw.draw_plot()
        self.draw.draw_circle(self.arr_mid, self.pixel_mid, self.pixel_radius)
        self.printr.print_instructions(self.K, win_w, win_h)


    """ UPDATES """
    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my

            self.convert()

    def convert(self):
        self.arr_mid = self.convert_to_arr(self.pixel_mid)
