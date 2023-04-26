import pygame
import random

# 游戏配置
WIDTH = 640
HEIGHT = 480
GRID_SIZE = 20

# 颜色配置
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 初始化 Pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('贪吃蛇')

# 创建字体对象
font = pygame.font.SysFont('Arial', 24)

# 定义蛇类
class Snake:
    def __init__(self):
        self.body = [(WIDTH / 2, HEIGHT / 2)]
        self.direction = 'right'
        self.color = GREEN
    
    def move(self):
        x, y = self.body[0]
        if self.direction == 'up':
            y -= GRID_SIZE
        elif self.direction == 'down':
            y += GRID_SIZE
        elif self.direction == 'left':
            x -= GRID_SIZE
        elif self.direction == 'right':
            x += GRID_SIZE
        self.body.insert(0, (x, y))#我们将蛇头的坐标插入到蛇身体的第一个位置，以实现蛇的移动：
        self.body.pop() #将蛇的最后一个位置弹出

    def draw(self, surface):
        for x, y in self.body:
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, self.color, rect)

    def collide(self, x, y):
        return (x, y) in self.body

    def grow(self):
        x, y = self.body[0]
        if self.direction == 'up':
            y -= GRID_SIZE
        elif self.direction == 'down':
            y += GRID_SIZE
        elif self.direction == 'left':
            x -= GRID_SIZE
        elif self.direction == 'right':
            x += GRID_SIZE
        self.body.insert(0, (x, y))

    def is_dead(self):
        x, y = self.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True
        for x, y in self.body[1:]:
            if (x, y) == self.body[0]:
                return True
        return False

# 定义食物类
class Food:
    def __init__(self):
        self.color = RED
        self.x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)

    def is_eaten(self, x, y):
        return self.x == x and self.y == y

    def reset(self):
        self.x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE

# 创建贪吃蛇和食物对象
snake = Snake()
food = Food()

# 游戏循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # 处理键盘输入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake.direction != 'down':
        snake.direction = 'up'
    elif keys[pygame.K_DOWN] and snake.direction != 'up':
        snake.direction = 'down'
    elif keys[pygame.K_LEFT] and snake.direction != 'right':
        snake.direction = 'left'
    elif keys[pygame.K_RIGHT] and snake.direction != 'left':
        snake.direction = 'right'

    # 更新贪吃蛇的位置
    snake.move()

    # 判断是否吃到食物
    if food.is_eaten(*snake.body[0]):
        snake.grow()
        food.reset()

    # 判断游戏是否结束
    if snake.is_dead():
        text = font.render('Game Over', True, WHITE, BLACK)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        break

    # 绘制游戏界面
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.update()

    # 设置游戏帧率
    pygame.time.Clock().tick(10)
    
pygame.quit()
