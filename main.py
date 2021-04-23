""" APRIL 22, 2021 """


import pygame
from setup.settings import Settings
from setup.pygameBasics import PygameBasics
from algo import Algo



class Main(PygameBasics):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.win_w = 1600
        self.win_h = 900
        self.win = pygame.display.set_mode((self.win_w, self.win_h), pygame.RESIZABLE)

        self.algo = Algo(self.win)
        self.update_window_size(0) ##

        ## Movement flags
        self.moving = False


    """ EVENTS """

    def left_click_events(self):
        pygame.mouse.get_rel()
        self.moving = True


    def right_click_events(self):
        pass

    def mouse_button_up_events(self):
        self.moving = False

    def keydown_events(self, event):
        if event.key == pygame.K_a:
            pass

        if event.key == pygame.K_q:
            pygame.quit(), quit()


    def keyup_events(self, event):
        pass

    """ UPDATES """

    def updates(self):
        self.algo.update_pixel_anchors(self.win_w, self.win_h)
        self.algo.update(self.moving)
        self.draw()


    def draw(self):
        self.win.fill(self.set.white)

        self.draw_page_border()
        self.algo.draw_things(self.win_w, self.win_h)
        #self.circle.draw(self.win_w, self.win_h)

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
