""" April 22, 2021 """

import pygame
from setup.settings import Settings
from setup.printr import Printr


class Draw:

    def __init__(self, win, norm_arr, pixels):
        pygame.init()
        self.win = win
        self.printr = Printr(self.win)
        self.set = Settings()

        self.norm_arr = norm_arr
        self.pixels = pixels


        self.s0 = self.set.red ## Colour of non-survivors
        self.s1 = self.set.blue  ## Colour of survivors

        self.c0 = self.set.grey
        self.c1 = self.set.light_grey ## Arr coord's
        self.c2 = self.set.light_blue ## Pixel coords


    def configure_scales(self, arr, px):
        self.arr_scale = arr
        self.pixel_scale = px
        self.pixel_origin = (px[0,0], px[0,1])

        self.configure_false_axes()


    def draw_plot(self):
        self.draw_axes()
        self.draw_x_axis_labels()
        self.draw_y_axis_labels()
        self.draw_array()
        #self.draw_origin()


    def draw_array(self):

        for i, arr_coord in enumerate(self.norm_arr[:,:-2]):
            x, y, survived = arr_coord ## Last two cols track nn status
            px_coord = self.pixels[i]

            text, c = "X", self.s0
            if survived:
                text, c = "O", self.s1

            text = self.set.small_font.render(text, True, c)
            self.win.blit( text, px_coord )

            #pygame.draw.circle(self.win, c, px_coord, 3, 0)


    def draw_axes(self):
        c = self.set.light_grey
        x, y = self.false_axes_origin
        right = x + self.false_axis_w
        top = y - self.false_axis_h

        pygame.draw.line(self.win, self.c1, (x, y), (x, top), 2)
        pygame.draw.line(self.win, self.c1, (x, y), (right, y), 2)


    def draw_x_axis_labels(self):
        ### Draw x scale
        y = self.false_axes_origin[1]
        origin_x = self.pixel_origin[0]

        for i in range(len(self.pixel_scale)):
            pixel_x = self.pixel_scale[i,0]

            ### Draw dot on axis
            pygame.draw.circle(self.win, self.set.grey, (pixel_x, y+1), 2, 0)

            ### Draw labels
            offset_x = pixel_x - 12

            arr_label = str(int(self.arr_scale[i,0]))
            pixel_label = str( int(self.pixel_scale[i,0]) )

            self.printr.coord_printr(arr_label, offset_x, y + 10, self.c0)
            #self.printr.coord_printr(pixel_label, offset_x, y + 25, self.set.blue)


    def draw_y_axis_labels(self):
            ### Print y scale
            x = self.false_axes_origin[0]
            origin_y = self.pixel_origin[1]

            for i in range(len(self.pixel_scale)):
                pixel_y = self.pixel_scale[i,1]

                ### Draw dot on axis
                pygame.draw.circle(self.win, self.set.grey, (x+1, pixel_y), 2, 0)

                ### Draw labels
                offset_y = pixel_y - 14
                arr_label = str(int(self.arr_scale[i,1]))
                pixel_label = str( int(self.pixel_scale[i,1]) )

                self.printr.coord_printr(arr_label, x - 40, offset_y, self.c0)
                #self.printr.coord_printr(pixel_label, x - 40, offset_y + 12, self.set.blue)


    """ Draw circle stuff """

    def draw_circle(self, arr_mid, pixel_mid, radius):
        c1 = self.set.ultra_light_grey
        c2 = self.set.light_grey

        pygame.draw.circle(self.win, c1, pixel_mid, radius, 1)
        pygame.draw.circle(self.win, c2, pixel_mid, 5, 0)

        self.draw_circle_coord(arr_mid, pixel_mid, radius)


    def draw_circle_coord(self, arr_mid, pixel_mid, radius):

        px_x, px_y = pixel_mid
        arr_x, arr_y = arr_mid

        arr_x = "Fare: £" + str( int(arr_x) )
        arr_y = "Age: " + str( int(arr_y) )
        px_coord = "(" + str(px_x) + ", " + str(px_y) + ")"

        y = px_y - 15
        x = px_x + radius + 12

        ## Draw white rect
        pygame.draw.rect(self.win, self.set.background, pygame.Rect(x-5, y, 60, 30), 0)

        self.printr.coord_printr(arr_x, x, y, self.set.grey)
        self.printr.coord_printr(arr_y, x, y + 15, self.set.grey)
        #self.printr.coord_printr(px_coord, px_x+10, y + 30, self.set.blue)



    def draw_origin(self):
        pygame.draw.circle(self.win, self.s0, self.pixel_origin, 6, 0)

        arr_origin = (self.arr_scale[0])

        x, y = self.pixel_origin
        arr_label = str( arr_origin )
        pixel_label = str( int(x) ) + ", " + str( int(y) )

        y-=15
        self.printr.coord_printr(arr_label, x+12, y, self.c0)
        self.printr.coord_printr(pixel_label, x+12, y + 15, self.set.blue)



    """ UTILITY """
    def configure_false_axes(self):
        buffer = 50
        x, y = self.pixel_origin

        self.pixel_w = self.pixel_scale[-1,0] - self.pixel_scale[0,0]
        self.pixel_h = self.pixel_scale[0,1] - self.pixel_scale[-1,1]


        self.false_axes_origin = (x - buffer, y + buffer)
        self.false_axis_w = self.pixel_w + (2 * buffer)
        self.false_axis_h = self.pixel_h + (2 * buffer)
