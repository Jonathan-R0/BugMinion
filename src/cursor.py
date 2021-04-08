import pygame

BLUE = (0, 0, 255)


class Cursor:
    def __init__(self, display, screen_width, screen_height):
        self.display = display
        self.width = screen_width / 3
        self.height = screen_height / 3
        self.pos = (1, 1)
        self.draw()

    def draw(self):
        coords = (self.pos[0] * self.width, self.pos[1] * self.height)
        x_coord = coords[0]
        y_coord = coords[1]
        self.surface = pygame.draw.rect(
            self.display, BLUE,
            pygame.Rect(x_coord, y_coord, self.width, self.height), 5)

    def move_pos(self, vector):
        new_pos = (self.pos[0] + vector[0], self.pos[1] + vector[1])
        if 0 <= new_pos[0] <= 2 and 0 <= new_pos[1] <= 2:
            self.pos = new_pos

    def go_up(self):
        self.move_pos((0, -1))
        self.draw()

    def go_down(self):
        self.move_pos((0, 1))
        self.draw()

    def go_left(self):
        self.move_pos((-1, 0))
        self.draw()

    def go_right(self):
        self.move_pos((1, 0))
        self.draw()

    def hit(self, table):
        table.new_drawing(self.pos)

    def unhit(self, table):
        table.stop_drawing(self.pos)
