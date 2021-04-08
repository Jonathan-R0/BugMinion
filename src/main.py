import sys
import pygame
from window import Window
from table import Table
from threading import Thread
from time import sleep

# Implement a thread safe queue so that I can queue images and they can later be drawn from the main thread.
# or maybe it´s better to just check how much time has passed and see what I should draw from one thread


def timer(display):
    for i in range(5, -1, -1):
        sleep(1)
        display.blit(pygame.image.load(
            "./../assets/" + str(i) + ".png"), (555, 500 - (((5 - i) * 500) / 6)))


def starting_screen(display):
    display.blit(pygame.image.load(
        "./../assets/startingscreen.png"), (0, 0))


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
    elif event.key == pygame.K_BACKSPACE:
        cursor.unhit(table)
    cursor.draw()


def run():
    window = Window(833, 500)
    cursor = window.create_cursor()
    table = Table()
    running = True
    starting_screen(cursor.display)

    thread = Thread(target=timer, args=(cursor.display,))

    thread.start()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                window.draw_background()
                detect_event(cursor, event, table)
                table.draw(window.display, cursor.width, cursor.height)

            pygame.display.update()
        window.clock.tick(60)
        window.update()

    thread.join()


if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        # Log errors.
        print(type(error))
        print(error.args)
        print(error)
