import pygame
import os
from pygame.math import Vector2
from config import cell_size, cell_number, SCREEN_UPDATE, FPS, GRASS_COLOR

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        # Load graphics - using relative paths
        assets_path = os.path.join("..","assets", "images")
        self.head_up = pygame.image.load(os.path.join(assets_path, "head4.png")).convert_alpha()
        self.head_down = pygame.image.load(os.path.join(assets_path, "head.png")).convert_alpha()
        self.head_right = pygame.image.load(os.path.join(assets_path, "head2.png")).convert_alpha()
        self.head_left = pygame.image.load(os.path.join(assets_path, "head3.png")).convert_alpha()

        self.tail_up = pygame.image.load(os.path.join(assets_path, "tail3.png")).convert_alpha()
        self.tail_down = pygame.image.load(os.path.join(assets_path, "tail.png")).convert_alpha()
        self.tail_right = pygame.image.load(os.path.join(assets_path, "tail4.png")).convert_alpha()
        self.tail_left = pygame.image.load(os.path.join(assets_path, "tail2.png")).convert_alpha()

        self.body_vertical = pygame.image.load(os.path.join(assets_path, "body.png")).convert_alpha()
        self.body_horizontal = pygame.image.load(os.path.join(assets_path, "body2.png")).convert_alpha()

        self.body_tr = pygame.image.load(os.path.join(assets_path, "bend3.png")).convert_alpha()
        self.body_t1 = pygame.image.load(os.path.join(assets_path, "bend.png")).convert_alpha()
        self.body_br = pygame.image.load(os.path.join(assets_path, "bend4.png")).convert_alpha()
        self.body_b1 = pygame.image.load(os.path.join(assets_path, "bend2.png")).convert_alpha()

    def draw_snake(self, screen):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(
                block.x * cell_size, block.y * cell_size, cell_size, cell_size
            )
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if (
                        previous_block.x == -1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == -1
                    ):
                        screen.blit(self.body_b1, block_rect)
                    if (
                        previous_block.x == -1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == -1
                    ):
                        screen.blit(self.body_tr, block_rect)
                    if (
                        previous_block.x == 1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == 1
                    ):
                        screen.blit(self.body_br, block_rect)
                    if (
                        previous_block.x == 1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == 1
                    ):
                        screen.blit(self.body_t1, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_right
        if head_relation == Vector2(-1, 0):
            self.head = self.head_left
        if head_relation == Vector2(0, 1):
            self.head = self.head_up
        if head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        if tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        if tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        if tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True