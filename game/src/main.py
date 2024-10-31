import os
import sys
from game.src.game import Game

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, 'frozen', False):
    dirpath = os.path.dirname(sys._MEIPASS)


if __name__ == "__main__":
    game = Game()
    game.run()
    
    