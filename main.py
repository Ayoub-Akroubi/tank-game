# main.py
import pygame
import random
from game import Game
from tank import Tank
from functions import *
import variables as var


game = Game(var.screen_width, var.screen_height, "our game", var.background_color)
screen = game.get_screen()


running = True
clock = pygame.time.Clock()

# Variable to keep track of the current tank's turn to fire
current_tank_turn = 1

while running:
    tankOne = Tank(x=var.tankOneX, y=550, screen=screen)
    tankTwo = Tank(x=var.tankTwoX, y=550, screen=screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # check the limits to move tanks
            if event.key == pygame.K_LEFT and var.tankOneX > 0:
                var.tankOneX -= 3
            elif event.key == pygame.K_RIGHT and var.tankOneX <= 320:
                var.tankOneX += 3
            elif event.key == pygame.K_UP and var.tankOneAngle <= -10:
                var.tankOneAngle += 5
            elif event.key == pygame.K_DOWN and var.tankOneAngle >= -80:
                var.tankOneAngle -= 5
            elif event.key == pygame.K_q and var.tankTwoX >= 430:
                var.tankTwoX -= 3
            elif event.key == pygame.K_d and var.tankTwoX < 730:
                var.tankTwoX += 3
            elif event.key == pygame.K_w and var.tankTwoAngle <= 80:
                var.tankTwoAngle += 5
            elif event.key == pygame.K_z and var.tankTwoAngle >= 10:
                var.tankTwoAngle -= 5
            elif event.key == pygame.K_p and var.power_tank_1 < 100:
                var.power_tank_1 += 2
            elif event.key == pygame.K_o and var.power_tank_1 > 0:
                var.power_tank_1 -= 2
            elif event.key == pygame.K_f and var.power_tank_2 < 100:
                var.power_tank_2 += 2
            elif event.key == pygame.K_g and var.power_tank_2 > 0:
                var.power_tank_2 -= 2


            elif event.key == pygame.K_SPACE:
                # Check whose turn it is to fire
                if current_tank_turn == 1:
                    fire_one_shot = tankOne.fire(1, posbarrelOne,var.tankTwoX)
                    if not fire_one_shot :
                        var.tank_two_health -= 20
                else:
                    fire_two_shot = tankTwo.fire(2, posbarrelTwo,var.tankOneX)
                    if not fire_two_shot :
                        var.tank_one_health -= 20

                # Switch the turn to the other tank
                current_tank_turn = 3 - current_tank_turn  # Toggle between 1 and 2

    screen.fill(var.background_color)

    posbarrelOne = tankOne.draw(var.tankOneAngle)
    posbarrelTwo =tankTwo.draw(var.tankTwoAngle)

    draw_wall(screen,var.screen_width // 2,var.wall_y,var.wall_height)

    # Display health bars
    if var.tank_one_health == 0 or var.tank_two_health == 0:
        game_over(screen,current_tank_turn)
    else:
        draw_health(screen)
        write_names(screen)
        draw_power(screen)

        pygame.display.flip()
        clock.tick(100)
pygame.quit()

