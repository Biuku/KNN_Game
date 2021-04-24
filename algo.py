""" April 24, 2021 """

import pygame
import math as m
import numpy as np
from setup.printr import Printr
from arr import Arr
from draw import Draw
from K import K


class Algo(Arr):
    def __init__(self, win):
        super().__init__()
        pygame.init()
        self.win = win
        self.printr = Printr(self.win)

        self.K = K(self.win, len(self.arr))
        self.draw = Draw(self.win, self.pixels)
        self.configure_draw()

        self.max_k = int(len(self.arr))
        self.k = self.init_k()

        ## Flags
        self.moving = False
        self.draw_outer_circle = False
        self.survived = True

        ### Circle ###
        self.pixel_mid = [800, 400]
        self.pixel_radius = 110

        self.convert(True) ## Initialize self.arr_mid

    def update_flags(self, moving, draw_outer):
        self.moving = moving
        self.draw_outer_circle = draw_outer


    def update(self):
        self.move()
        self.convert(self.moving)
        self.knn()


    """ ********** """
    def update_k(self, delta_k):
        new_k = self.k + delta_k
        if new_k > 0 and new_k < self.max_k:
            self.k = new_k


    def draw_things(self, win_w, win_h):
        self.draw.draw_plot(self.norm_arr)

        radius = 0
        if self.draw_outer_circle:
            radius = self.pixel_radius

        self.draw.draw_circle(self.arr_mid, self.pixel_mid, radius, self.survived)
        self.printr.print_instructions(self.k, self.survived, win_w, win_h)



    def knn(self):

        ## Reset the distances and nn
        self.norm_arr[:,3:] = 0

        ## Calculate the distances and nn -- note, need to vectorize
        for i, coord in enumerate(self.norm_arr[:,:2]):
            euclid = np.sqrt(np.sum(np.square(self.norm_arr_mid - coord)))
            self.norm_arr[i:,3] = euclid

        ## partition the array into smallest / largest K
        part = np.argpartition(self.norm_arr[:,3], self.k)
        self.norm_arr[part[:self.k], 4] = 1

        self.update_radius(self.norm_arr[part[:self.k]])
        self.update_survived(self.norm_arr[part[:self.k]])


    def update_survived(self, part):
        self.survived = True
        if part[:,2].sum() < (len(part)/2):
            self.survived = False


    def update_radius(self, part):
        """ Need to set radius as equal to length of furthest nn """

        # Get index of the furthest nn coordinate in norm_arr
        mx = part[:,3].max()
        index = np.where(self.norm_arr == mx)[0][0]

        # Get the pixel equivalent of that coordinate
        x1, y1 = self.pixels[index,:2]

        ## euclidian distance
        x2, y2 = self.pixel_mid
        self.pixel_radius = m.sqrt( (x2-x1)**2 + (y2-y1)**2)



    """ UPDATES """
    def move(self):
        if self.moving:
            mx, my = pygame.mouse.get_rel()

            ## Move circle if the mouse is anywhere on the graph
            if pygame.mouse.get_pos()[0] < self.pixel_origin[0] + self.pixel_w:
                self.pixel_mid[0] += mx
                self.pixel_mid[1] += my


    def convert(self, moving):
        if moving:
            self.norm_arr_mid = self.convert_pixel_to_norm_arr(self.pixel_mid)
            self.arr_mid = self.convert_norm_arr_to_arr(self.norm_arr_mid)




    """ Run once """
    def configure_draw(self):
        self.draw.configure_scales(self.arr_scale, self.pixel_scale)

    def init_k(self):
        k = int(m.sqrt(self.max_k))
        if k % 2 == 0:
            k += 1

        return k
