#!/usr/bin/env python3
"""
Snakezz - Main Entry Point
A Python implementation of the classic Snake game using Pygame.
"""

from game import SnakeGame

def main():
    """Initialize and run the Snakezz game."""
    try:
        game = SnakeGame()
        game.run()
    except Exception as e:
        print(f"Error starting the game: {e}")
        print("Please make sure all asset files are in the correct location.")

if __name__ == "__main__":
    main()
