""" APRIL 20, 2021 """

import pygame
from setup.settings import Settings

class PygameBasics:
    def __init__(self):
        pygame.init()
        self.set = Settings()
        #
        # self.win_w = 1600
        # self.win_h = 900
        #
        # self.win = pygame.display.set_mode((self.win_w, self.win_h), pygame.RESIZABLE)


    """ EVENTS """

    def events(self):
        for event in pygame.event.get():


            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.left_click_events()

                if pygame.mouse.get_pressed()[2]:
                    self.right_click_events()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up_events()

            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.keyup_events(event)

            elif event.type == pygame.VIDEORESIZE:
                self.update_window_size(event)

            elif event.type == pygame.QUIT:
                pygame.quit(), quit()


    def update_window_size(self, event):
        if event:
            self.win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        ## When user resizes the window, adjust the w and h values everything else is anchored to
        self.win_w = self.win.get_width()
        self.win_h = self.win.get_height()

        self.algo.update_pixel_anchors(self.win_w, self.win_h)
        self.algo.configure()


    """ Draw background """

    def draw_page_border(self):
        """ Draw rectangle around the entire page to give it an edge """

        x = self.win_w * self.set.border_gap
        y = self.win_h * self.set.border_gap

        w =  self.win_w * (1 - (2 * self.set.border_gap))
        h = self.win_h * (1 - (2 * self.set.border_gap))

        c = self.set.light_grey
        thick = 3

        pygame.draw.rect(self.win, c, pygame.Rect(x, y, w, h), thick)
