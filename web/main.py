import asyncio
import pygame
from game_logic import Game

async def main():
    game = Game()
    await game.run()

if __name__ == "__main__":
    asyncio.run(main())
