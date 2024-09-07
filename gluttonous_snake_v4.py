import pygame
import time
import random

pygame.init()

# 加载字体
try:
    font_style = pygame.font.Font("msyh.ttf", 25)
    score_font = pygame.font.Font("msyh.ttf", 35)
except FileNotFoundError:
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

# 加载声音
pygame.mixer.init()
game_over_sound = pygame.mixer.Sound("game_over.mp3")
eat_sound = pygame.mixer.Sound("eat_sound.wav")

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('贪吃蛇游戏')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

def Your_score(score):
    value = score_font.render("你的分数: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        pygame.draw.circle(dis, white, (x[0] + snake_block // 2, x[1] + snake_block // 2), snake_block // 4)  # 蛇的眼睛

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False
    game_win = False
    paused = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("你输了! 点击按钮重新开始或退出", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # 绘制按钮
            quit_button = pygame.Rect(dis_width / 2 - 100, dis_height / 2 - 25, 200, 50)  # 退出按钮的位置和大小
            continue_button = pygame.Rect(dis_width / 2 - 100, dis_height / 2 + 50, 200, 50)  # 继续按钮的位置和大小

            pygame.draw.rect(dis, red, quit_button)
            pygame.draw.rect(dis, green, continue_button)

            # 绘制按钮文本
            dis.blit(font_style.render("退出", True, white), (dis_width / 2 - 40, dis_height / 2 - 15))
            dis.blit(font_style.render("重玩", True, white), (dis_width / 2 - 40, dis_height / 2 + 65))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if quit_button.collidepoint(mouse_pos):
                        game_over = True
                        game_close = False
                    elif continue_button.collidepoint(mouse_pos):
                        gameLoop()

        while game_win == True:
            dis.fill(blue)
            message("你赢了! 点击按钮重新开始或退出", green)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # 绘制按钮
            quit_button = pygame.Rect(dis_width / 2 - 100, dis_height / 2 - 25, 200, 50)  # 退出按钮的位置和大小
            continue_button = pygame.Rect(dis_width / 2 - 100, dis_height / 2 + 50, 200, 50)  # 继续按钮的位置和大小

            pygame.draw.rect(dis, red, quit_button)
            pygame.draw.rect(dis, green, continue_button)

            # 绘制按钮文本
            dis.blit(font_style.render("退出", True, white), (dis_width / 2 - 40, dis_height / 2 - 15))
            dis.blit(font_style.render("重玩", True, white), (dis_width / 2 - 40, dis_height / 2 + 65))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_win = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if quit_button.collidepoint(mouse_pos):
                        game_over = True
                        game_win = False
                    elif continue_button.collidepoint(mouse_pos):
                        gameLoop()

        while paused:
            dis.fill(blue)
            message("游戏已暂停! 点击按钮继续或退出", yellow)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # 绘制按钮
            continue_button = pygame.Rect(dis_width / 2 - 100, dis_height / 2 - 25, 200, 50)  # 继续按钮的位置和大小
            quit_button = pygame.Rect(dis_width / 2 - 100, dis_height / 2 + 50, 200, 50)  # 退出按钮的位置和大小

            pygame.draw.rect(dis, green, continue_button)
            pygame.draw.rect(dis, red, quit_button)

            # 绘制按钮文本
            dis.blit(font_style.render("继续", True, white), (dis_width / 2 - 40, dis_height / 2 - 15))
            dis.blit(font_style.render("退出", True, white), (dis_width / 2 - 40, dis_height / 2 + 65))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if continue_button.collidepoint(mouse_pos):
                        paused = False
                    elif quit_button.collidepoint(mouse_pos):
                        game_over = True
                        paused = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:
                    paused = True

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            pygame.mixer.Sound.play(game_over_sound)
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.circle(dis, red, (foodx + snake_block // 2, foody + snake_block // 2), snake_block // 4)  # 食物的眼睛
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                pygame.mixer.Sound.play(game_over_sound)

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            pygame.mixer.Sound.play(eat_sound)

            if Length_of_snake - 1 >= 100:
                game_win = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
