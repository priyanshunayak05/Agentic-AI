import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
BLOCK = 20

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Q Learning")

clock = pygame.time.Clock()

class SnakeGame:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.snake = [(WIDTH//2, HEIGHT//2)]
        self.direction = "RIGHT"
        self.generate_food()
        self.score = 0
        return self.get_state()
        
    def generate_food(self):
        self.food = (
            random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK)
        )
        
    def move(self, action):
        # 0 = left, 1 = right, 2 = up, 3 = down
        
        if action == 0 and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif action == 1 and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif action == 2 and self.direction != "DOWN":
            self.direction = "UP"
        elif action == 3 and self.direction != "UP":
            self.direction = "DOWN"
            
        x, y = self.snake[0]
        
        if self.direction == "LEFT": x -= BLOCK
        if self.direction == "RIGHT": x += BLOCK
        if self.direction == "UP": y -= BLOCK
        if self.direction == "DOWN": y += BLOCK
        
        new_head = (x, y)
        self.snake.insert(0, new_head)
        
    def step(self, action):
        self.move(action)
        reward = 0
        done = False
        
        if self.is_collision():
            done = True
            reward = -10
            return self.get_state(), reward, done
        
        if self.snake[0] == self.food:
            self.score += 1
            reward = 10
            self.generate_food()
        else:
            self.snake.pop()
            
        return self.get_state(), reward, done
    
    def is_collision(self, point=None):
        if point is None:
            point = self.snake[0]
        x, y = point
        
        # hit wall
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True
        
        # hit itself
        if point in self.snake[1:]:
            return True
        
        return False
        
    def get_state(self):
        head = self.snake[0]
        x, y = head
        
        # Points around snake head
        left = (x - BLOCK, y)
        right = (x + BLOCK, y)
        up = (x, y - BLOCK)
        down = (x, y + BLOCK)

        # Danger detection
        danger_left = self.is_collision(left)
        danger_right = self.is_collision(right)
        danger_straight = False
        
        if self.direction == "LEFT":
            danger_straight = danger_left
        elif self.direction == "RIGHT":
            danger_straight = danger_right
        elif self.direction == "UP":
            danger_straight = self.is_collision(up)
        elif self.direction == "DOWN":
            danger_straight = self.is_collision(down)

        # Food relative position
        food_left = self.food[0] < x
        food_right = self.food[0] > x
        food_up = self.food[1] < y
        food_down = self.food[1] > y
        
        state = (
            int(danger_straight),
            int(danger_left),
            int(danger_right),

            int(food_left),
            int(food_right),
            int(food_up),
            int(food_down)
        )
        
        return state
        
    def draw_grid(self):
        for x in range(0, WIDTH, BLOCK):
            pygame.draw.line(win, (40,40,40), (x,0), (x,HEIGHT))
        for y in range(0, HEIGHT, BLOCK):
            pygame.draw.line(win, (40,40,40), (0,y), (WIDTH,y))

    def render(self):
        win.fill((0, 0, 0))

        # draw grid
        self.draw_grid()
        
        # snake
        for x, y in self.snake:
            pygame.draw.rect(win, (0, 255, 0), (x, y, BLOCK, BLOCK))
            
        # food
        pygame.draw.rect(win, (255, 0, 0), (self.food[0], self.food[1], BLOCK, BLOCK))
        
        pygame.display.update()
