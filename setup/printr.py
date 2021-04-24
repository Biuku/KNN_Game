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


    def print_instructions(self, k, survived, win_w, win_h):
        x = win_w * 0.86 ## lower number --> leftward
        y = win_h * 0.06 ## lower number --> upward

        text_survived = "Die"
        if survived:
            text_survived = "Live"

        texts = [
            'INSTRUCTIONS',
            '  · Click: move',
            '  · a = decrease K',
            '  · d = increase K',
            '  · Spacebar = Show KNN circle',
            '',
            'KNN',
            '  · K: ' + str(k),
            '  · Prediction: ' + text_survived,
            ]

        for text in texts:
            print_instructions = self.set.med_font.render(text, True, self.set.grey)
            self.win.blit( print_instructions, (x, y) )
            y += 22


    def format_rss(self, rss):
        if rss:
            return ("{:,}".format(int(rss)))
        return str(0)
