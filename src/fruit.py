import pygame
import random
import os
from pygame.math import Vector2
from config import cell_size, cell_number, SCREEN_UPDATE, FPS, GRASS_COLOR

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self, screen, apple_image):
        fruit_rect = pygame.Rect(
            self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size
        )
        screen.blit(apple_image, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)