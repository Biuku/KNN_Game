""" APRIL 20, 2021 """


import pygame
from setup.settings import Settings
from setup.pygameBasics import PygameBasics
from plot import Plot
from circle import Circle



class Main(PygameBasics):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.circle = Circle(self.win)
        self.plot = Plot(self.win)
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
            #self.circle.tracer()
            pass

        if event.key == pygame.K_q:
            pygame.quit(), quit()


    def keyup_events(self, event):
        pass

    """ UPDATES """

    def updates(self):
        self.plot.update_pixel_anchors(self.win_w, self.win_h)
        self.circle.update(self.moving)
        self.draw()


    def draw(self):
        self.win.fill(self.set.white)
        
        self.draw_page_border()
        self.plot.draw()
        self.circle.draw(self.win_w, self.win_h)

        pygame.display.update()


    """ MAIN """

    def main(self):
        while True:
            self.win.fill(self.set.white)
            self.set.clock.tick(self.set.FPS)
            self.events()
            self.updates()

if __name__ == "__main__":
    x = Main()
    x.main()
