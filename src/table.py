import pygame


class Block:
    def __init__(self, image_src=None):
        self.image_src = image_src
        self.drawing = False

    def draw(self, display, coords):
        if self.drawing:
            display.blit(pygame.image.load("./../assets/roach.png"), coords)


class Table:
    def __init__(self):
        self.blocks = ([], [], [])
        for block in self.blocks:
            for _ in range(0, 3):
                block.append(Block())

    def new_drawing(self, coords):
        self.blocks[coords[0]][coords[1]].drawing = True

    def stop_drawing(self, coords):
        self.blocks[coords[0]][coords[1]].drawing = False

    def draw(self, display, cursor_width, cursor_height):
        for i in range(0, 3):
            for j in range(0, 3):
                self.blocks[i][j].draw(display,
                                       (i * cursor_width, j * cursor_height))
