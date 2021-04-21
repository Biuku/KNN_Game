""" April 20, 2021 """

import pygame
import numpy as np
from setup.settings import Settings


class Arr:

    def __init__(self):
        pygame.init()
        self.set = Settings()

        ## How many labels to divide each axis into
        self.x_num_labels = 17
        self.y_num_labels = 15

        self.arr = self.raw_arr = np.load('data/arr50.npy')
        self.update_pixel_anchors(1600, 900)
        self.configure()


    """ CONFIGURATION STUFF """

    def configure(self):
        """ On initialization and when resizing """

        ## Assume two dimensions of independent data
        self.arr[:,0] = self.normalizr(self.raw_arr[:,0])
        self.arr[:,1] = self.normalizr(self.raw_arr[:,1])

        self.configure_arr()
        self.configure_pixel_scale()
        self.configure_false_axes()
        self.get_pixels_of_arr()


    def normalizr(self, series):
        """ Takes in an np series (1 col) and scales it to range 0-1 """
        mn = series.min()
        mx = series.max()

        return (series - mn) / (mx-mn)


    def update_pixel_anchors(self, win_w, win_h):
        """ When the screen resizes, update the size anchors for the graph """

        ## Pixel width and height
        self.pixel_w = win_w * 0.7
        self.pixel_h = win_h * 0.7

        ## Pixel origin
        x = win_w * self.set.origin_gap_left
        y = win_h * (1-self.set.origin_gap_bottom)

        self.pixel_origin = (x, y)


    ### PIXELS
    def configure_pixel_scale(self):

        # Set pixel min/max
        self.pixel_x_min, self.pixel_y_max = self.pixel_origin
        self.pixel_x_max = self.pixel_x_min + self.pixel_w
        self.pixel_y_min = self.pixel_y_max - self.pixel_h ## pixel y: 'min' = more 'up'

        self.pixel_x_scale = np.linspace( (self.pixel_x_min), (self.pixel_x_max), self.x_num_labels )
        self.pixel_y_scale = np.linspace( (self.pixel_y_max), (self.pixel_y_min), self.y_num_labels )


    ### ARR
    def configure_arr(self):
        self.arr_origin = (0, 0)
        self.arr_x_scale = np.linspace( 0, 1, self.x_num_labels )
        self.arr_y_scale = np.linspace( 0, 1, self.y_num_labels )


    """ CONVERSION STUFF """
    def convert_to_arr(self, pixel_coords):
        """ Converts individual coordinates from pixel units to normalized arr units """
        x, y = pixel_coords

        ## Zero the passed coord
        x = (x - self.pixel_x_min) / self.pixel_w
        y = (self.pixel_y_max - y) / self.pixel_h

        return x, y


    def convert_to_pixels(self, arr_coords):
        """ Convert from normalized arr units to pygame-useful pixel units """
        x, y = arr_coords

        ## Scale those values to be pixels
        x *= self.pixel_w
        y *= self.pixel_h

        ## Find x, y values relative to arr origin
        x += self.pixel_x_min
        y = self.pixel_y_max - y

        return int(x), int(y) ## Pixel values should be int


    def get_pixels_of_arr(self):
        arr = []
        for coord in self.arr:
            coord = coord[:2]
            pixels = self.convert_to_pixels(coord)
            arr.append( tuple(pixels) )

        self.pixels_of_arr = tuple(arr)


    """ UTILITY """
    def configure_false_axes(self):
        self.buffer = 50
        x, y = self.pixel_origin

        self.false_axes_origin = (x - self.buffer, y + self.buffer)
        self.false_axis_w = self.pixel_w + (2 * self.buffer)
        self.false_axis_h = self.pixel_h + (2 * self.buffer)
