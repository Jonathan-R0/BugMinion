import logging
import traceback
from game import Game

if __name__ == "__main__":
    try:
        game = Game()
        game.game_loop()
    except Exception as error:
        logging.error(traceback.format_exc())
