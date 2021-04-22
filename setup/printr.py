""" April 20, 2021 """

import pygame
import math as m
import random as r
from setup.settings import Settings


class Printr:
    def __init__(self, win):
        pygame.init()
        self.win = win
        self.set = Settings()


    def coord_printr(self, data, x, y, c):
        text = self.set.small_font.render(data, True, c)
        self.win.blit( text, (x, y) )


    def print_instructions(self, K, win_w, win_h):
        x = win_w * 0.88 ## lower number --> leftward
        y = win_h * 0.06 ## lower number --> upward

        texts = [
            'INSTRUCTIONS',
            '  · Click: move',
            'KNN',
            '  · K = ' + str(K)
            ]

        for text in texts:
            print_instructions = self.set.small_font.render(text, True, self.set.grey)
            self.win.blit( print_instructions, (x, y) )
            y += 22


    def format_rss(self, rss):
        if rss:
            return ("{:,}".format(int(rss)))
        return str(0)
