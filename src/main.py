import sys
import pygame
from window import Window
from table import Table

if len(sys.argv) != 3:
    raise IOError("Must include window size.")
    # Read from config file.


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
    window = Window(sys.argv[1], sys.argv[2])
    cursor = window.create_cursor()
    table = Table()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                window.black_screen()
                detect_event(cursor, event, table)
                table.draw(window.display, cursor.width, cursor.height)

            pygame.display.update()
        window.clock.tick(60)
        window.update()


if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        # Log errors.
        print(type(error))
        print(error.args)
        print(error)
