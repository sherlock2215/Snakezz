import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, BLACK, BLUE
from snake import Snake
from food import Food

class SnakeGame:
    """Main game class that manages the game state, objects, and loop."""
    
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Create game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snakezz")
        self.clock = pygame.time.Clock()
        
        # Game objects
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)
        
        # Game state
        self.game_over = False
        self.font = pygame.font.SysFont("Arial", 24)
    
    def handle_events(self):
        """Handle all game events like keyboard input and quitting."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                else:
                    # Handle snake direction changes
                    if event.key == pygame.K_UP:
                        self.snake.turn((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.snake.turn((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn((1, 0))
    
    def update(self):
        """Update game logic."""
        if not self.game_over:
            # Move snake
            self.snake.move()
            
            # Check for collisions with food
            if self.food.check_collision(self.snake.get_head_position()):
                self.snake.grow()
                self.food.respawn(self.snake.positions)
            
            # Check for game over conditions
            if self.snake.check_collision():
                self.game_over = True
    
    def draw(self):
        """Draw all game elements."""
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw game objects
        self.food.draw()
        self.snake.draw()
        
        # Draw score
        score_text = self.font.render(f"Score: {self.snake.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("Game Over! Press SPACE to restart", True, WHITE)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(game_over_text, text_rect)
    
    def reset_game(self):
        """Reset the game to initial state."""
        self.snake.reset()
        self.food.respawn(self.snake.positions)
        self.game_over = False
    
    def run(self):
        """Main game loop."""
        while True:
            self.handle_events()
            self.update()
            self.draw()
            
            pygame.display.update()
            self.clock.tick(FPS)
