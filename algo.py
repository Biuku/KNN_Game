""" April 22, 2021 """


import pygame
import math as m
import numpy as np
from setup.printr import Printr
from arr import Arr
from draw import Draw


class Algo(Arr):
    def __init__(self, win):
        super().__init__()
        pygame.init()
        self.win = win
        self.printr = Printr(self.win)

        self.draw = Draw(self.win, self.pixels)
        self.configure_draw()

        self.k = 7

        ### Circle ###
        self.pixel_mid = [800, 400]
        self.pixel_radius = 110

        self.convert(True) ## Initialize self.arr_mid


    def tracer(self):
        print(self.norm_arr[:10])


    def update(self, moving):
        self.move(moving)
        self.convert(moving)
        self.knn(moving)


    def draw_things(self, win_w, win_h):
        self.draw.draw_plot(self.norm_arr)
        self.draw.draw_circle(self.arr_mid, self.pixel_mid, self.pixel_radius)
        self.printr.print_instructions(self.k, win_w, win_h)


    def knn(self, moving):
        if moving:
            self.norm_arr[:,3:] = 0

            for i, coord in enumerate(self.norm_arr[:,:2]):
                euclid = np.sqrt(np.sum(np.square(self.norm_arr_mid - coord)))
                self.norm_arr[i:,3] = euclid

            x = np.argpartition(self.norm_arr[:,3], self.k)

            self.norm_arr[x[:self.k], 4] = 1


    """ UPDATES """
    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my


    def convert(self, moving):
        if moving:
            self.norm_arr_mid = self.convert_pixel_to_norm_arr(self.pixel_mid)
            self.arr_mid = self.convert_norm_arr_to_arr(self.norm_arr_mid)







    """ Run once """
    def configure_draw(self):
        self.draw.configure_scales(self.arr_scale, self.pixel_scale)
