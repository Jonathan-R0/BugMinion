import pygame
from cursor import Cursor

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
TITLE = "BugMinion"


class Window:
    def __init__(self, screen_width, screen_height):
        self.width = 500
        self.height = 500
        pygame.init()
        self.mixer = pygame.mixer
        self.mixer.init()
        self.display = pygame.display.set_mode((screen_width, screen_height))
        self.logo_img = pygame.image.load("./../assets/logo.png")
        pygame.display.set_icon(self.logo_img)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def __del__(self):
        pygame.mixer.quit()
        pygame.quit()

    def update(self):
        pygame.display.flip()

    def draw_background(self):
        self.display.blit(pygame.image.load("./../assets/background.png"),
                          (0, 0))

    def create_cursor(self):
        return Cursor(self.display, self.width, self.height, BLUE)

    def create_enemy(self):
        return Cursor(self.display, self.width, self.height, RED)
