import sys
import pygame
from timer import Timer
from window import Window
from table import Table

SCREEN_WIDTH = 833
SCREEN_HEIGHT = 500

TADA = "./../assets/tada.wav"
FART = "./../assets/fart.wav"
FPS = 30


class Game:
    def __init__(self):
        self.window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.cursor = self.window.create_cursor()
        self.table = Table()
        self.running = True
        self.game_ended = False
        self._starting_screen()
        self.timer = Timer(self.cursor.display, (700, 350),
                           self.window.mixer.Sound("./../assets/pop.wav"))

    def _starting_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    return

            self.window.display.blit(
                pygame.image.load("./../assets/startingscreen.png"), (0, 0))
            self.window.update()

    def detect_event(self, event):
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            self.cursor.go_down()
        elif event.key == pygame.K_LEFT or event.key == ord('a'):
            self.cursor.go_left()
        elif event.key == pygame.K_UP or event.key == ord('w'):
            self.cursor.go_up()
        elif event.key == pygame.K_RIGHT or event.key == ord('d'):
            self.cursor.go_right()
        elif event.key == pygame.K_RETURN:
            return self.cursor.hit(self.table)
        self.cursor.draw()
        return False

    def draw(self):
        self.timer.update()
        self.window.draw_background()
        self.timer.draw()
        self.table.draw(self.window.display, self.cursor.width,
                        self.cursor.height)
        self.cursor.draw()

    def play_ending_sound(self, song):
        sound = self.window.mixer.Sound(song)
        self.draw()
        self.window.update()
        channel = sound.play()
        while channel.get_busy():
            pygame.time.wait(100)

    def game_loop(self):
        while self.running:

            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and not self.game_ended:
                    if self.detect_event(event) and not self.table.i_win():
                        self.table.enemy_pick()
                pygame.display.update()

            if self.table.i_win():
                self.running = False
                self.play_ending_sound(TADA)
            if self.table.i_lose():
                self.running = False
                self.play_ending_sound(FART)

            self.window.clock.tick(FPS)
            self.window.update()