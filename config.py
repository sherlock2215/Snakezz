"""
Game configuration constants for Snakezz.
Centralizes all game settings for easy modification.
"""

# Game window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Game grid settings
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)

# Game mechanics
INITIAL_SNAKE_LENGTH = 3
SNAKE_SPEED = 10

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
