import time
import random
import pygame
import numpy as np


class Block:
    def __init__(self, coords, image_src="./../assets/roach.png"):
        self.image_src = image_src
        self.drawing = False
        self.enemy = False
        self.pos = coords

    def draw(self, display, coords):
        if self.drawing:
            display.blit(pygame.image.load(self.image_src), coords)


class Table:
    def __init__(self):
        self.blocks = ([], [], [])
        i = 0
        for block in self.blocks:
            for j in range(0, 3):
                block.append(Block((i, j)))
            i += 1

    def new_drawing(self, coords):
        self.blocks[coords[0]][coords[1]].drawing = True

    def stop_drawing(self, coords):
        self.blocks[coords[0]][coords[1]].drawing = False

    def draw(self, display, cursor_width, cursor_height):
        for i in range(0, 3):
            for j in range(0, 3):
                self.blocks[i][j].draw(display,
                                       (i * cursor_width, j * cursor_height))

    # Not checking diags
    def player_won(self):
        game = tuple(self.blocks)
        won = True
        for row in game:
            for block in row:
                won = won and block.drawing and not block.enemy
        game = np.transpose(game)
        for row in game:
            for block in row:
                won = won and block.drawing and not block.enemy
        return won

    def enemy_pick(self):
        choices = set()
        for row in self.blocks:
            for block in row:
                if not block.drawing:
                    choices.add(block)

        if len(choices) != 0:
            choice = random.choice(tuple(choices))
            choice.drawing = True
            choice.enemy = True
            choice.image_src = "./../assets/circle.png"

        time.sleep(0.2)
