""" April 22, 2021 """

import pygame
from setup.settings import Settings
from setup.printr import Printr
from arr import Arr


class Plot(Arr):

    def __init__(self, win):
        pygame.init()
        super().__init__()
        self.win = win
        self.printr = Printr(self.win)

        self.s0 = self.set.red ## Colour of non-survivors
        self.s1 = self.set.blue  ## Colour of survivors

        self.c0 = self.set.grey
        self.c1 = self.set.light_grey ## Arr coord's
        self.c2 = self.set.light_blue ## Pixel coords


    def draw(self):
        self.draw_axes()
        self.draw_x_axes_labels()
        self.draw_y_axes_labels()
        self.draw_array()
        #self.draw_origin()


    def draw_array(self):

        for i, arr_coord in enumerate(self.norm_arr):
            x, y, survived = arr_coord
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


    def draw_x_axes_labels(self):

        ### Draw x scale
        y = self.false_axes_origin[1]
        origin_x = self.pixel_origin[0]

        for i in range(self.x_num_labels):
            pixel_x = self.pixel_x_scale[i]

            ### Draw dot on axis
            pygame.draw.circle(self.win, self.set.grey, (pixel_x, y+1), 2, 0)

            ### Draw labels
            offset_x = pixel_x - 12

            arr_label = str(int(self.arr_x_scale[i]))
            pixel_label = str( int(self.pixel_x_scale[i]) )

            self.printr.coord_printr(arr_label, offset_x, y + 10, self.c0)
            #self.printr.coord_printr(pixel_label, offset_x, y + 25, self.set.blue)


    def draw_y_axes_labels(self):
            ### Print y scale
            x = self.false_axes_origin[0]
            origin_y = self.pixel_origin[1]

            for i in range(self.y_num_labels):
                pixel_y = self.pixel_y_scale[i]

                ### Draw dot on axis
                pygame.draw.circle(self.win, self.set.grey, (x+1, pixel_y), 2, 0)

                ### Draw labels
                offset_y = pixel_y - 14
                arr_label = str(int(self.arr_y_scale[i]))
                pixel_label = str( int(self.pixel_y_scale[i]) )

                self.printr.coord_printr(arr_label, x - 40, offset_y, self.c0)
                #self.printr.coord_printr(pixel_label, x - 40, offset_y + 12, self.set.blue)






    # def draw_origin(self):
    #     pygame.draw.circle(self.win, self.s0, self.pixel_origin, 6, 0)
    #
    #     x, y = self.pixel_origin
    #     arr_label = str( self.arr_origin )
    #     pixel_label = str( int(x) ) + ", " + str( int(y) )
    #
    #     y-=15
    #     self.printr.coord_printr(arr_label, x+12, y, self.c0)
    #     self.printr.coord_printr(pixel_label, x+12, y + 15, self.set.blue)

    # """ Stuff from Circle """
    #
    # def draw(self, win_w, win_h):
    #     self.draw_circle()
    #     self.printr.print_instructions(self.K, win_w, win_h)
    #
    # def draw_circle(self):
    #     c1 = self.set.ultra_light_grey
    #     c2 = self.set.light_grey
    #
    #     pygame.draw.circle(self.win, c1, self.pixel_mid, self.pixel_radius, 1)
    #     pygame.draw.circle(self.win, c2, self.pixel_mid, 5, 0)
    #
    #     px_x, px_y = self.pixel_mid
    #     arr_x, arr_y = self.arr_mid
    #
    #     arr_coord = "(" + str( round(arr_x, 2) ) + ", " + str( round(arr_y, 2) ) + ")"
    #     px_coord = "(" + str(px_x) + ", " + str(px_y) + ")"
    #
    #     y = px_y - 15
    #
    #     self.printr.coord_printr(arr_coord, px_x+10, y, self.set.grey)
    #     self.printr.coord_printr(px_coord, px_x+10, y + 15, self.set.blue)
