""" April 19, 2021 """

import pygame
from arr import Arr
from setup.printr import Printr


class Plot(Arr):

    def __init__(self, win):
        pygame.init()
        super().__init__()
        self.win = win
        self.printr = Printr(self.win, self.set)

        self.s0 = self.set.red ## Colour of non-survivors
        self.s1 = self.set.blue  ## Colour of survivors

        self.c0 = self.set.grey
        self.c1 = self.set.light_grey ## Arr coord's
        self.c2 = self.set.light_blue ## Pixel coords

    def tracer(self):
        print(f"\nX: {self.arr[:,0]}\n")
        print(f"Y: {self.arr[:,1]}\n")
        print(f"Z: {self.arr[:,2]}\n")



    def draw(self):
        self.draw_axes()
        self.draw_x_axes_labels()
        self.draw_y_axes_labels()
        self.draw_array()


    def draw_array(self):

        for arr_coord in self.arr:
            x, y, survived = arr_coord
            px_coord = self.convert_to_pixels( (x, y) )

            text, c = "O", self.s0
            if survived:
                text, c = "X", self.s1

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
            arr_label = str( round(self.arr_x_scale[i], 1) )
            #pixel_label = str( int(self.pixel_x_scale[i]) )

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
                offset_y = pixel_y - 9
                arr_label = str( round(self.arr_y_scale[i], 1) )
                # pixel_label = str( int(self.pixel_y_scale[i]) )

                self.printr.coord_printr(arr_label, x - 30, offset_y, self.c0)
                #self.printr.coord_printr(pixel_label, x - 30, offset_y + 15, self.set.blue)
