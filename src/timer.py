import sys
import time
from math import floor
import pygame

TOTAL_SECONDS = 5
PATH_TO_ASSETS = "./../assets/"
IMG_FORMAT = ".png"


class Timer:
    def __init__(self, display, coords, pop_sound):
        self.now = 5
        self.starting_time = time.time()
        self.display = display
        self.drawing_coords = coords
        self.pop_sound = pop_sound

    def draw(self):
        self.update()
        self.display.blit(
            pygame.image.load(PATH_TO_ASSETS + str(TOTAL_SECONDS - self.now) +
                              IMG_FORMAT), (self.drawing_coords))

    def _get_time(self):
        delta_time = floor(time.time() - self.starting_time)
        if delta_time > TOTAL_SECONDS:
            sys.exit()
        if 0 <= delta_time <= TOTAL_SECONDS:
            return delta_time
        return TOTAL_SECONDS

    def update(self):
        before = self.now
        self.now = self._get_time()
        if before != self.now:
            self.pop_sound.play()