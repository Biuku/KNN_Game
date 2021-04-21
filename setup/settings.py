""" April 20, 2021 """

import pygame


class Settings:

    def __init__(self):

        ## Set gap in % from edge of pygame window to page border
        self.border_gap = 0.02
        self.origin_gap_left = self.border_gap + 0.07 ## lower = left
        self.origin_gap_bottom = self.border_gap + 0.12 ## lower = up

        self.clock = pygame.time.Clock()
        self.FPS = 120

        ### Colours
        self.white, self.black = (255, 255, 255), (0, 0, 0)
        self.ultra_light_grey = (240, 240, 240)
        self.light_grey, self.grey, self.dark_grey = (221, 221, 221), (150,150,150), (45, 45, 45)
        self.blue, self.light_blue = (190, 170, 255), (210, 210, 255),
        self.red, self.light_red = (235, 52, 52), (255, 175, 175)
        self.yellow = (255, 255, 150)

        ## Colour styles
        self.object1_538 = (217, 240, 222)
        self.object2_538 = (255, 234, 217)

        ### Fonts
        self.small_font = pygame.font.SysFont('lucidasans', 10)
        self.med_font = pygame.font.SysFont('lucidasans', 11)
        self.large_font = pygame.font.SysFont('lucidasans', 12)
