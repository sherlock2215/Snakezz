#!/usr/bin/env python3
"""
Snakezz - Main Entry Point
"""

import pygame
import sys
import os

# Import config first
from pygame import Vector2

from config import cell_size, cell_number, SCREEN_UPDATE, FPS, GRASS_COLOR

# Import game classes
from snake import SNAKE
from fruit import FRUIT
from game import MAIN


def main():
    pygame.init()

    # Setup screen
    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
    pygame.display.set_caption("Snakezz")
    clock = pygame.time.Clock()

    # Load assets
    assets_path = os.path.join("..","assets", "images")
    apple = pygame.image.load(os.path.join(assets_path, "apple.jpg")).convert_alpha()
    apple = pygame.transform.scale(apple, (cell_size, cell_size))

    game_font = pygame.font.SysFont("Arial", 25)
    # Create main game
    main_game = MAIN(screen, apple, game_font)

    # Setup timer
    SCREEN_UPDATE_EVENT = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE_EVENT, SCREEN_UPDATE)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE_EVENT:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, +1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(+1, 0)

        screen.fill(GRASS_COLOR)
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()