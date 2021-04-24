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
        self.moving = False
        self.draw_outer_circle = False

        ### Circle ###
        self.pixel_mid = [800, 400]
        self.pixel_radius = 110

        self.convert(True) ## Initialize self.arr_mid


    def tracer(self):
        print(self.norm_arr[:10])


    def update_flags(self, moving, draw_outer):
        self.moving = moving
        self.draw_outer_circle = draw_outer


    def update(self):
        self.move()
        self.convert(self.moving)
        self.knn()


    def draw_things(self, win_w, win_h):
        self.draw.draw_plot(self.norm_arr)

        radius = 0
        if self.draw_outer_circle:
            radius = self.pixel_radius

        self.draw.draw_circle(self.arr_mid, self.pixel_mid, radius)

        self.printr.print_instructions(self.k, win_w, win_h)


    def knn(self):
        if self.moving:
            self.norm_arr[:,3:] = 0

            for i, coord in enumerate(self.norm_arr[:,:2]):
                euclid = np.sqrt(np.sum(np.square(self.norm_arr_mid - coord)))
                self.norm_arr[i:,3] = euclid

            part = np.argpartition(self.norm_arr[:,3], self.k)

            self.norm_arr[part[:self.k], 4] = 1

            part = self.norm_arr[part[:self.k]]


            self.update_radius(part)


    def update_radius(self, part):
        """ Need to set radius as equal to length of furthest nn """

        # Get index of the furthest nn coordinate in norm_arr

        mx = part[:,3].max()
        index = np.where(self.norm_arr == mx)[0][0]

        # Get the pixel equivalent of that coordinate
        x1, y1 = self.pixels[index,:2]

        ## euclidian distance
        x2, y2 = self.pixel_mid
        euclid = m.sqrt( (x2-x1)**2 + (y2-y1)**2)

        self.pixel_radius = euclid

        # print("\n", (x1, y1), self.pixel_mid, euclid, "\n")



    """ UPDATES """
    def move(self):
        if self.moving:
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
