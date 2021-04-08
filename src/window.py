import pygame
from cursor import Cursor

BLACK = (0, 0, 0)
TITLE = "BugMinion"


class Window:
    def __init__(self, width, height):
        try:
            self.width = int(width)
            self.height = int(height)
        except TypeError as error:
            # Log errors.
            print(type(error))
            print(error.args)
            print(error)

        pygame.init()
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def __del__(self):
        pygame.quit()

    def update(self):
        pygame.display.flip()

    def black_screen(self):
        self.display.fill(BLACK)

    def create_cursor(self):
        return Cursor(self.display, self.width, self.height)
