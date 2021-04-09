import time
import random
import pygame
import numpy as np

PLAYER_CHARACTER = 'O'
ENEMY_CHARACTER = 'X'


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

    def _make_game_matrix(self):
        ans = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for i in range(0, 3):
            for j in range(0, 3):
                if self.blocks[i][j].drawing:
                    if self.blocks[i][j].enemy:
                        ans[i][j] = ENEMY_CHARACTER
                    else:
                        ans[i][j] = PLAYER_CHARACTER
        return ans

    def __str__(self):
        ans = self._make_game_matrix()
        return '[' + str(ans[0]) + '\n ' + str(ans[1]) + '\n ' + str(ans[2]) + ']'

    def new_drawing(self, coords):
        self.blocks[coords[0]][coords[1]].drawing = True

    def stop_drawing(self, coords):
        self.blocks[coords[0]][coords[1]].drawing = False

    def draw(self, display, cursor_width, cursor_height):
        for i in range(0, 3):
            for j in range(0, 3):
                self.blocks[i][j].draw(display,
                                       (i * cursor_width, j * cursor_height))

    def _check_winning_matrix(self, game_matrix, char):
        for row in game_matrix:
            if len(set(row)) == 1 and any(x != ' ' for x in row):
                return char not in row

    def player_won(self, char):
        game_matrix = self._make_game_matrix()
        if self._check_winning_matrix(game_matrix, char):
            return True
        game_matrix = np.transpose(game_matrix)
        if self._check_winning_matrix(game_matrix, char):
            return True
        diag = set()
        for i in range(0, 3):
            diag.add(game_matrix[i][i])
        if (len(diag) == 1 and any(x != ' ' for x in diag)):
            return char not in diag
        antidiag = set()
        for i in range(0, 3):
            antidiag.add(game_matrix[2 - i][i])
        if (len(antidiag) == 1 and any(x != ' ' for x in antidiag)):
            return char not in antidiag
        return None

    def i_win(self):
        return self.player_won(ENEMY_CHARACTER)

    def i_lose(self):
        return self.player_won(PLAYER_CHARACTER)

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
            choice.image_src = "./../assets/ant.png"

        time.sleep(0.2)
