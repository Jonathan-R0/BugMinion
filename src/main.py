import sys
import logging
import traceback
import pygame
from timer import Timer
from window import Window
from table import Table

SCREEN_WIDTH = 833
SCREEN_HEIGHT = 500
TADA = "./../assets/tada.wav"
FART = "./../assets/fart.wav"
FPS = 30


def starting_screen(display, window):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return

        display.blit(pygame.image.load("./../assets/startingscreen.png"),
                     (0, 0))
        window.update()


def detect_event(cursor, event, table):
    if event.key == pygame.K_DOWN or event.key == ord('s'):
        cursor.go_down()
    elif event.key == pygame.K_LEFT or event.key == ord('a'):
        cursor.go_left()
    elif event.key == pygame.K_UP or event.key == ord('w'):
        cursor.go_up()
    elif event.key == pygame.K_RIGHT or event.key == ord('d'):
        cursor.go_right()
    elif event.key == pygame.K_RETURN:
        return cursor.hit(table)
    #elif event.key == pygame.K_BACKSPACE:
    #    cursor.unhit(table)
    cursor.draw()
    return False


def draw(timer, window, table, cursor):
    timer.update()
    window.draw_background()
    timer.draw()
    table.draw(window.display, cursor.width, cursor.height)
    cursor.draw()


def play_ending_sound(timer, window, table, cursor, song):
    sound = window.mixer.Sound(song)
    draw(timer, window, table, cursor)
    window.update()
    channel = sound.play()
    while channel.get_busy():
        pygame.time.wait(100)


def run():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    cursor = window.create_cursor()
    table = Table()
    running = True
    game_ended = False
    starting_screen(cursor.display, window)
    timer = Timer(cursor.display, (700, 350),
                  window.mixer.Sound("./../assets/pop.wav"))

    while running:

        draw(timer, window, table, cursor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_ended:
                if detect_event(cursor, event, table) and not table.i_win():
                    table.enemy_pick()
            pygame.display.update()

        if table.i_win():
            running = False
            play_ending_sound(timer, window, table, cursor, TADA)
        if table.i_lose():
            running = False
            play_ending_sound(timer, window, table, cursor, FART)

        window.clock.tick(FPS)
        window.update()


if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        logging.error(traceback.format_exc())
