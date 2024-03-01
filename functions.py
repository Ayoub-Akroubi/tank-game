import pygame
import math
import random
import variables as var
import sys
pygame.init()

def draw_wall(screen, x,y, height):
    pygame.draw.rect(screen, (100, 100, 100), [x, y, 25, height])

def is_not_obstacle(shell_x, shell_y):
    x_wall_min = (var.screen_width // 2)
    x_wall_max = (var.screen_width // 2) + 35
    # print(shell_x, x_wall, shell_y, var.wall_y)
    if x_wall_min < shell_x < x_wall_max and shell_y > var.wall_y:
        return False
    return True

def is_enemy(shell_x, shell_y, enemyTankX):
    enemyTankY = 550
    return not (enemyTankX <= shell_x <= enemyTankX + 70  and  enemyTankY <= shell_y <=  enemyTankY + 70)

def change_health_color(health):
    health_color = var.health_color
    if 100 > health > 40:
        health_color = (202, 82, 0)
    elif health <= 40 :
        health_color = (202, 0, 0)
    return health_color

def game_over(screen, current_tank):
    popup_width, popup_height = 400, 200
    popup_rect = pygame.Rect(
        (var.screen_width - popup_width) // 2, (var.screen_height - popup_height) // 2,
        popup_width, popup_height
    )

    pygame.draw.rect(screen, (255, 255, 255), popup_rect)
    pygame.draw.rect(screen, (0, 0, 0), popup_rect, 5)

    pygame.font.init()
    font = pygame.font.Font(None, 36)

    if current_tank == 1:
        text = font.render("Player 2 win!", True, (0, 0, 0))
    else:
        text = font.render("Player 1 win!" , True, (0, 0, 0))
    text_rect = text.get_rect(center=popup_rect.center)
    screen.blit(text, text_rect)

    quit_text = font.render("THE END ... Click 'X' To Quit", True, (0, 0, 0))
    quit_rect = quit_text.get_rect(center=(popup_rect.centerx, popup_rect.centery + 50))
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()

def draw_health(screen):
    tank_one_health_bar_width = var.tank_one_health * 2 
    tank_two_health_bar_width = var.tank_two_health * 2  


    pygame.draw.rect(screen, change_health_color(tank_one_health_bar_width), [20, 20, tank_one_health_bar_width, 20])  # Green bar for Tank One
    pygame.draw.rect(screen, change_health_color(tank_two_health_bar_width), [var.screen_width - tank_two_health_bar_width - 20, 20, tank_two_health_bar_width, 20])  # Red bar for Tank Two

def draw_power(screen):
    pygame.font.init()
    font = pygame.font.Font(None, 26) 

    power_text_1 = font.render(f"Power: {var.power_tank_1}", True, (0, 0, 0))
    screen.blit(power_text_1, (60, 80))
    power_text_2 = font.render(f"Power: {var.power_tank_2}", True, (0, 0, 0))
    screen.blit(power_text_2, (630, 80))

def write_names(screen):
    pygame.font.init()
    font = pygame.font.Font(None, 26) 

    power_text_1 = font.render("Player 1", True, (0, 0, 0))
    screen.blit(power_text_1, (70, 50))
    power_text_2 = font.render("Player 2", True, (0, 0, 0))
    screen.blit(power_text_2, (640, 50))

def draw_bomb(screen, x_bomb, y_bomb):
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        magnitude = 1
        clock = pygame.time.Clock()

        while magnitude < 50:
            exploding_bit_x = x_bomb + random.randrange(-1 * magnitude, magnitude)
            exploding_bit_y = y_bomb + random.randrange(-1 * magnitude, magnitude)

            pygame.draw.circle(screen,  (100, 100, 100) , (exploding_bit_x, exploding_bit_y), random.randrange(1, 4))
            magnitude += 1
            pygame.display.update()
            clock.tick(100)
        explode = False