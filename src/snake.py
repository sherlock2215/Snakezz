import pygame
from config import GRID_SIZE, GREEN, DARK_GREEN, UP, DOWN, LEFT, RIGHT, INITIAL_SNAKE_LENGTH

class Snake:
    """Represents the player-controlled snake in the game."""
    
    def __init__(self, screen):
        self.screen = screen
        self.reset()
    
    def reset(self):
        """Reset the snake to initial state."""
        self.length = INITIAL_SNAKE_LENGTH
        self.positions = [(GRID_SIZE, GRID_SIZE)]  # Start position
        self.direction = RIGHT
        self.score = 0
        self.grow_pending = INITIAL_SNAKE_LENGTH - 1
    
    def get_head_position(self):
        """Get the current position of the snake's head."""
        return self.positions[0]
    
    def turn(self, point):
        """Change the snake's direction."""
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return  # Prevent 180-degree turns
        self.direction = point
    
    def move(self):
        """Move the snake forward in the current direction."""
        head = self.get_head_position()
        x, y = self.direction
        new_x = (head[0] + (x * GRID_SIZE)) 
        new_y = (head[1] + (y * GRID_SIZE))
        new_position = (new_x, new_y)
        
        # Add new head position
        self.positions.insert(0, new_position)
        
        # Remove tail if not growing
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.positions.pop()
    
    def grow(self):
        """Increase snake length."""
        self.length += 1
        self.grow_pending += 1
        self.score += 1
    
    def draw(self):
        """Draw the snake on the screen."""
        for i, p in enumerate(self.positions):
            # Draw snake segment
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            if i == 0:  # Head
                pygame.draw.rect(self.screen, DARK_GREEN, rect)
            else:  # Body
                pygame.draw.rect(self.screen, GREEN, rect)
            pygame.draw.rect(self.screen, BLACK, rect, 1)  # Border
    
    def check_collision(self):
        """Check if snake collides with itself or walls."""
        head = self.get_head_position()
        
        # Check wall collision
        if (head[0] < 0 or head[0] >= self.screen.get_width() or 
            head[1] < 0 or head[1] >= self.screen.get_height()):
            return True
        
        # Check self collision
        if head in self.positions[1:]:
            return True
        
        return False
