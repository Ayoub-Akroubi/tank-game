import random

background_color = (255, 255, 255)
screen_width = 800
screen_height = 600
wall_height = random.randint(100, 400)
# wall_height = 200
wall_y = screen_height - wall_height // 2
tankOneX = 30
tankTwoX = 700
tankOneAngle = -45
tankTwoAngle = 45
XangleRotate = 0
YangleRotate = 0
fireX = 0
fireY = 0
power_tank_1 = 50
power_tank_2 = 50
tank_one_health = tank_two_health = 100
health_color = (12, 200, 0)