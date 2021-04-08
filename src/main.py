import sys
import logging
import traceback
import pygame
from timer import Timer
from window import Window
from table import Table

SCREEN_WIDTH = 833
SCREEN_HEIGHT = 500
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
    print(cursor.pos)
    if event.key == pygame.K_DOWN or event.key == ord('s'):
        cursor.go_down()
    elif event.key == pygame.K_LEFT or event.key == ord('a'):
        cursor.go_left()
    elif event.key == pygame.K_UP or event.key == ord('w'):
        cursor.go_up()
    elif event.key == pygame.K_RIGHT or event.key == ord('d'):
        cursor.go_right()
    elif event.key == pygame.K_RETURN:
        cursor.hit(table)
        return True
    elif event.key == pygame.K_BACKSPACE:
        cursor.unhit(table)
    cursor.draw()
    return False


def run():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    cursor = window.create_cursor()
    table = Table()
    running = True
    game_ended = False
    starting_screen(cursor.display, window)
    timer = Timer(cursor.display, (700, 350))

    while running:

        timer.update()
        window.draw_background()
        timer.draw()
        table.draw(window.display, cursor.width, cursor.height)
        cursor.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_ended:
                if detect_event(cursor, event, table):
                    table.enemy_pick()
            pygame.display.update()

        if table.player_won():
            print("You win!")

        window.clock.tick(FPS)
        window.update()


if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        logging.error(traceback.format_exc())
