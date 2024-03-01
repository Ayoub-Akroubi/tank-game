import pygame


class Game:
    def __init__(self, width, height, title, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

    def get_screen(self):
        return self.screen