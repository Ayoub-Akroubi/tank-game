import pygame
import math
from functions import *

clock = pygame.time.Clock()
class Tank:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 40
        self.turret_length = 20
        self.screen = screen
        self.barrel_angle = 0

    def draw(self, barrel_angle):
        pygame.draw.rect(self.screen, (100, 100, 100), [self.x, self.y, self.width, self.height], border_radius = 7)
        circle_x = self.x + (self.width // 2) 
        circle_y = self.y - self.turret_length  + (self.height // 2) 
        pygame.draw.circle(self.screen, (100, 100, 100), (circle_x, circle_y), 20)

        barrel_width = 5
        barrel_length = 40
        barrel_x = self.x  + (self.width // 2) - (barrel_width // 2)
        barrel_y = self.y - self.turret_length  - barrel_length 
        rotated_barrel = pygame.Surface((barrel_width, barrel_length), pygame.SRCALPHA)
        rotated_barrel.fill((100, 100, 100)) 
        rotated_barrel = pygame.transform.rotate(rotated_barrel, barrel_angle)
        rotated_rect = rotated_barrel.get_rect(center=(barrel_x + barrel_width // 2, barrel_y + barrel_length))
        self.screen.blit(rotated_barrel, rotated_rect.topleft)
        return rotated_rect

    def fire(self, n,posbarrel, enemyTankX ):
        if n == 1: 
            starting_shell_x = list(posbarrel.topright)[0]
            starting_shell_y = list(posbarrel.topright)[1]
        else:
            starting_shell_x = list(posbarrel.topleft)[0]
            starting_shell_y = list(posbarrel.topleft)[1]
        shell_speed_x = 3
        shell_speed_y = 1.5

        fire_width = 800 // 2
        counter = 0.2
        isObstacle = isEnemyTank = True

        print('Fire!')

        while (starting_shell_x < 800 and starting_shell_x > 0) and (starting_shell_y < 600 and starting_shell_y > 0) and isObstacle and isEnemyTank:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.draw.circle(self.screen, (255, 0, 0), (starting_shell_x, starting_shell_y ), 1)

            if n == 1:
                starting_shell_x += shell_speed_x
                starting_shell_y -= shell_speed_y  - counter + (var.power_tank_1  * 0.01)
            else:
                starting_shell_x -= shell_speed_x
                starting_shell_y -= shell_speed_y - counter + (var.power_tank_2  * 0.01)

            if starting_shell_x % 10 == 0:
                counter += 0.2

            isObstacle = is_not_obstacle(starting_shell_x, starting_shell_y)
            isEnemyTank = is_enemy(starting_shell_x, starting_shell_y,enemyTankX )
            pygame.display.update()
            clock.tick(100)
        draw_bomb(self.screen, starting_shell_x, starting_shell_y)
        return isEnemyTank
