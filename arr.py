""" April 22, 2021 """

import pygame
import numpy as np
from setup.settings import Settings


class Arr:

    def __init__(self):
        pygame.init()
        self.set = Settings()

        self.origin_gap_left = 0.07 + self.set.border_gap## lower = left
        self.origin_gap_bottom = 0.12 + self.set.border_gap ## lower = up

        ## How many labels to divide each axis into
        self.x_num_labels = 15 ## Delete
        self.y_num_labels = 15 ## Delete
        self.axis_labels = 15

        self.arr = np.load('data/arr50.npy')

        self.update_pixel_anchors(1600, 900)
        self.configure()


    """ A. CONFIGURE ARRAYS AND AXIS SCALES FOR 3 UNITS: ARR, NORM_ARR, AND PIXELS """

    def configure(self):
        ### On initialization and when resizing ###

        # Alternative-unit np.arrays
        self.norm_arr = self.get_normalized_arr()
        self.pixels = self.get_pixel_datastructure()

        #  Axis scales
        self.arr_scale = self.configure_arr_scale()
        self.norm_arr_scale = self.configure_norm_arr_scale()
        self.pixel_scale = self.configure_pixel_scale()


    """ A1. Configure arrays """

    def get_normalized_arr(self, n=1):
        ### Scales np array's first n cols to range 0-1 ###
        """
        - [0, 1, 2] = x, y, survived
        - [3] = distance
        - [4] = bool: is nn
        """
        norm_arr = self.arr.copy() ## Deep copy

        for i in range(n+1):
            series = self.arr[:,i]
            mn, mx = series.min(), series.max()
            norm_arr[:,i] = (series - mn) / (mx - mn) # Vector

        ## Append cols [3, 4]: distance and nn
        arr = np.zeros( (len(norm_arr), 2) )

        return  np.append(norm_arr, arr, axis=1)


    def get_pixel_datastructure(self, n=2):
        ### Scales normalized array to pixel units ###
        li = []
        for coord in self.norm_arr:
            pixels = self.convert_norm_arr_to_pixels(coord[:n])
            li.append( tuple(pixels) )

        return np.array(li)


    """ A2. Configure scales """

    def configure_arr_scale(self):
        labels = self.axis_labels
        x, y = self.arr[:,0], self.arr[:,1]

        x_scale = np.linspace( x.min(), x.max(), labels ).reshape(labels, 1)
        y_scale = np.linspace( y.min(), y.max(), labels ).reshape(labels, 1)

        return np.concatenate((x_scale, y_scale), axis = 1)

    ### ARR SCALE
    def configure_norm_arr_scale(self):
        labels = self.axis_labels
        x = np.linspace( 0, 1, labels ).reshape(labels, 1)
        y = np.linspace( 0, 1, labels ).reshape(labels, 1)

        return np.concatenate( (x, y), axis = 1)

    ### PIXELS
    def configure_pixel_scale(self):
        labels = self.axis_labels
        x_min, y_max = self.pixel_origin
        x_max = x_min + self.pixel_w
        y_min = y_max - self.pixel_h ## pixel y: 'min' = more 'up'

        x = np.linspace( x_min, x_max, labels ).reshape(labels, 1)
        y = np.linspace( y_max, y_min, labels ).reshape(labels, 1)

        return np.concatenate( (x, y), axis = 1)


    """ CONVERSION STUFF """
    def convert_pixel_to_norm_arr(self, pixel_coords):
        """ Converts x, y pixel coordinates to original arr units """
        x, y = pixel_coords

        pixel_x_min = self.pixels[:,0].min()
        pixel_y_max = self.pixels[:,1].max()

        ## Zero and convert
        x = (x - pixel_x_min) / self.pixel_w
        y = (pixel_y_max - y) / self.pixel_h

        return x, y


    def convert_norm_arr_to_arr(self, norm_arr_coords):
        ### Converts x, y, norm_arr units to units of the original arr ###
        i = 7
        x, y = norm_arr_coords

        x = x * (self.arr_scale[i,0] / self.norm_arr_scale[i,0])
        y = y * (self.arr_scale[i,1] / self.norm_arr_scale[i,1])

        return x, y


    def convert_arr_to_norm_arr(self, arr_coords):
        ### Converts x, y units of the original arr to norm_arr units ###
        i = 7
        x, y = arr_coords

        x = x * (self.norm_arr_scale[i,0] / self.arr_scale[i,0])
        y = y * (self.norm_arr_scale[i,1] / self.arr_scale[i,1])

        return x, y


    def convert_norm_arr_to_pixels(self, arr_coords):
        """ Convert from normalized arr units to pygame-useful pixel units """
        x, y = arr_coords
        pixel_x_min, pixel_y_max = self.pixel_origin

        x *= self.pixel_w
        y *= self.pixel_h

        x += pixel_x_min
        y = pixel_y_max - y

        return int(x), int(y) ## Pixel values should be int


    """ SCREEN SIZE ADJUSTMENTS """

    def update_pixel_anchors(self, win_w, win_h):
        ### When the screen resizes, update the size anchors for the graph ###

        ## Pixel width and height
        self.pixel_w = win_w * 0.7
        self.pixel_h = win_h * 0.7

        ## Pixel origin
        x = win_w * self.origin_gap_left
        y = win_h * (1-self.origin_gap_bottom)
        self.pixel_origin = (x, y)
