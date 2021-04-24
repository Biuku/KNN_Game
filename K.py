""" April 24, 2021 """

import pygame
from setup.settings import Settings

class K:

    def __init__(self, win, max_k):
        pygame.init()
        self.win = win
        self.set = Settings()
        self.max_k = max_k
        self.left, self.y = 1376, 54+200
        self.w = 170
        self.h = 20
        self.x = self.centre = self.left + (self.w // 2)


    def draw_IO(self):
        right = self.left + self.w

        pygame.draw.line(self.win, self.set.grey, (self.left, self.y), (right, self.y), 2)


    def draw_slider(self, k, x = 70):
        top = self.y - (self.h//2)
        bot = top + self.h

        pygame.draw.line(self.win, self.set.dark_grey, (self.x, top), (self.x, bot), 1)

        text = 'K: ' + str(k)
        #text = 'K: ' + str(self.max_k)
        text = self.set.med_font.render(text, True, self.set.grey)
        self.win.blit( text, (self.centre-10, self.y-30) )
