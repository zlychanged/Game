import pygame
import sys
import random
import os

currentDir = os.path.dirname(__file__)

def game_over():
    print("Game Over!")

pygame.init()

width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

snake_pos = [[100, 100], [80, 100], [60, 100]]
snake_size = 10

food_pos = [random.randrange(1, (width // 20)) * 10, random.randrange(1, (height // 20)) * 10]
food_size = 10

clock = pygame.time.Clock()
speed = 15

pygame.display.set_caption("SnakeGame")
try:
    pygame.display.set_icon(pygame.image.load(os.path.join(currentDir, "snake.jpg")))
except pygame.error as e:
    print(f"Could not load icon: {e}")
    game_over()

direction = "RIGHT"

game_active = False

def game_over():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if not game_active:
                game_active = True
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    if game_active:
        if direction == "UP":
            snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - 10])
        if direction == "DOWN":
            snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + 10])
        if direction == "LEFT":
            snake_pos.insert(0, [snake_pos[0][0] - 10, snake_pos[0][1]])
        if direction == "RIGHT":
            snake_pos.insert(0, [snake_pos[0][0] + 10, snake_pos[0][1]])

        if snake_pos[0] == food_pos:
            food_pos = [random.randrange(1, (width // 20)) * 10, random.randrange(1, (height // 20)) * 10]
            print(f"New food position: {food_pos}")
        else:
            snake_pos.pop()

        # 检查贪吃蛇是否碰到边界或自己
        if (snake_pos[0][0] < 0 or snake_pos[0][0] >= width or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= height or
            snake_pos[0] in snake_pos[1:]):
            print(f"Game over! Snake position: {snake_pos[0]}")
            game_over()


        screen.fill(black)
        for pos in snake_pos:
            pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))
    else:
        screen.fill(black)
        font = pygame.font.SysFont(None, 55)
        text = font.render("Press any key to start", True, white)
        screen.blit(text, [width // 4, height // 2])

    # 更新屏幕
    pygame.display.flip()
    clock.tick(speed)
