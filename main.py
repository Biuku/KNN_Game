""" APRIL 22, 2021 """


import pygame
from setup.settings import Settings
from setup.pygameBasics import PygameBasics
from algo import Algo



class Main(PygameBasics):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.win_w, self.win_h  = 1600, 900
        self.win = pygame.display.set_mode((self.win_w, self.win_h), pygame.RESIZABLE)

        self.algo = Algo(self.win)
        self.update_window_size(0) ##

        ## Movement flags
        self.moving = False
        self.draw_outer_circle = False


    """ EVENTS """

    def left_click_events(self):
        pygame.mouse.get_rel()
        self.moving = True


    def mouse_button_up_events(self):
        self.moving = False


    def keydown_events(self, event):
        if event.key == pygame.K_a:
            self.algo.update_k(-2)

        if event.key == pygame.K_d:
            self.algo.update_k(2)

        if event.key == pygame.K_SPACE:
            self.draw_outer_circle = not self.draw_outer_circle

        if event.key == pygame.K_q:
            pygame.quit(), quit()


    def keyup_events(self, event):
        pass


    def update_window_size(self, event):
        """ called from pygameBasicselif event.type == pygame.VIDEORESIZE: """
        if event:
            self.win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        ## When user resizes the window, adjust the w and h values everything else is anchored to
        self.win_w = self.win.get_width()
        self.win_h = self.win.get_height()

        self.algo.update_pixel_anchors(self.win_w, self.win_h)
        self.algo.configure()

    """ UPDATES """

    def updates(self):
        self.algo.update_flags(self.moving, self.draw_outer_circle)
        self.algo.update()
        self.draw()


    def draw(self):
        self.win.fill(self.set.white)
        self.draw_page_border()
        self.algo.draw_things(self.win_w, self.win_h)

        pygame.display.update()


    """ MAIN """

    def main(self):
        while True:
            self.win.fill(self.set.background)
            self.set.clock.tick(self.set.FPS)
            self.events()
            self.updates()

if __name__ == "__main__":
    x = Main()
    x.main()
