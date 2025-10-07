import random
import pygame,sys
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.new_block=False

        self.head_up=pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\head4.png").convert_alpha()
        self.head_down = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\head.png").convert_alpha()
        self.head_right = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\head2.png").convert_alpha()
        self.head_left = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\head3.png").convert_alpha()

        self.tail_up = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\tail3.png").convert_alpha()
        self.tail_down = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\tail.png").convert_alpha()
        self.tail_right = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\tail4.png").convert_alpha()
        self.tail_left = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\tail2.png").convert_alpha()

        self.body_vertical = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\body.png").convert_alpha()
        self.body_horizontal = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\body2.png").convert_alpha()

        self.body_tr = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\bend3.png").convert_alpha()
        self.body_t1 = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\bend.png").convert_alpha()
        self.body_br = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\bend4.png").convert_alpha()
        self.body_b1 = pygame.image.load("C:\\Users\\SH\\Downloads\\snake graphic\\bend2.png").convert_alpha()
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            block_rect=pygame.Rect(block.x *cell_size,block.y*cell_size,cell_size,cell_size)
            if index==0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body)-1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block=self.body[index+1]-block
                next_block=self.body[index-1]-block
                if previous_block.x==next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y==next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                        screen.blit(self.body_b1,block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            screen.blit(self.body_tr, block_rect)
                    if previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                        screen.blit(self.body_br,block_rect)
                    if previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x==1:
                        screen.blit(self.body_t1,block_rect)



            #pygame.draw.rect(screen,(50,60,200),block_rect)
    def update_head_graphics(self):
        head_relation=self.body[1]-self.body[0]
        if head_relation==Vector2(1,0):
            self.head=self.head_right
        if head_relation == Vector2(-1, 0):
            self.head = self.head_left
        if head_relation == Vector2(0,1):
            self.head = self.head_up
        if head_relation == Vector2(0,-1):
            self.head = self.head_down
    def update_tail_graphics(self):
        tail_relation=self.body[-2]-self.body[-1]
        if tail_relation==Vector2(1,0):
            self.tail=self.tail_left
        if tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        if tail_relation == Vector2(0,1):
            self.tail = self.tail_up
        if tail_relation == Vector2(0,-1):
            self.tail = self.tail_down


    def move_snake(self):
        if self.new_block==True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block=False
        else:
            body_copy =self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]

    def add_block(self):
        self.new_block=True

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple,fruit_rect)
        #draw square
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake=SNAKE()
        self.fruit=FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.check_fail()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
               self.fruit.randomize()
               self.snake.add_block()
                #reposition the fruit
    def check_fail(self):
        #check if snake hits itself
        if not 0<=self.snake.body[0].x<cell_number:
            self.game_over()
        if not 0<=self.snake.body[0].y<cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
    def draw_grass(self):
        grass_color=(100,200,61)
        for row in range(cell_number):
            if row %2==0:
             for col in range(cell_number):
                 if col % 2 == 0:
                    grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text=str(len(self.snake.body)-3)
        score_surface=game_font.render(score_text,True,(56,74,12))
        score_x=int(cell_size*cell_number-60)
        score_y = int(cell_size * cell_number - 40)
        score_rect=score_surface.get_rect(center=(score_x,score_y))
        apple_rect=apple.get_rect(midright=(score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top, apple_rect.width + score_rect.width, apple_rect.height)
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect,2)



pygame.init()
cell_size=40
cell_number=20
screen=pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock=pygame.time.Clock()
apple=pygame.image.load("C:\\Users\\SH\\OneDrive\\Desktop\\snake.png").convert_alpha()
game_font= pygame.font.Font("C:\\Users\\SH\\Downloads\\bakery\\bakery.otf",25)
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
test_surface=pygame.Surface((100,200))
test_surface.fill((10,60,200))
test_rect= test_surface.get_rect(center=(250,250))
main_game= MAIN()
while True:
    #draw all elements0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==SCREEN_UPDATE:
            main_game.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
              if main_game.snake.direction.y!=1:
                main_game.snake.direction=Vector2(0,-1)
            if event.key==pygame.K_DOWN:
              if main_game.snake.direction.y != -1:
                main_game.snake.direction=Vector2(0,+1)
            if event.key==pygame.K_LEFT:
              if main_game.snake.direction.x !=1:
                main_game.snake.direction=Vector2(-1,0)
            if event.key==pygame.K_RIGHT:
              if main_game.snake.direction.x !=-1:
                main_game.snake.direction=Vector2(+1,0)


    screen.fill((175,250,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
