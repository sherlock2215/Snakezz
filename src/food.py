import pygame
import random
from config import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, RED

class Food:
    """Represents the food that the snake eats to grow."""
    
    def __init__(self, screen, image_path="../assets/images/apple.png"):
        self.screen = screen
        try:
            # Try to load apple image
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (GRID_SIZE, GRID_SIZE))
            self.use_image = True
        except:
            # Fallback to drawing a rectangle if image not found
            self.use_image = False
        self.position = self.randomize_position()
    
    def randomize_position(self):
        """Place food at a random grid position."""
        x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        return (x, y)
    
    def draw(self):
        """Draw the food on the screen."""
        if self.use_image:
            # Draw using apple image
            self.screen.blit(self.image, (self.position[0], self.position[1]))
        else:
            # Fallback: draw red rectangle
            rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(self.screen, RED, rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # Border
    
    def respawn(self, snake_positions):
        """Move food to new position that's not occupied by snake."""
        while True:
            self.position = self.randomize_position()
            # Ensure food doesn't spawn on snake
            if self.position not in snake_positions:
                break
    
    def check_collision(self, snake_head):
        """Check if snake head collides with food."""
        return snake_head == self.position
