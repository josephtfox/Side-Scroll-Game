import pygame

class Environment():
    def __init__(self, window, display_width, display_height):
        self.platform_width = display_width
        self.platform_height = 75
        self.floor_x_pos = 0
        self.floor_y_pos = display_height - self.platform_height
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.window = window

        # Creates the background image of the game
        self.bg_surface = pygame.image.load('Background.png').convert()
        self.bg_surface = pygame.transform.scale(self.bg_surface, (display_width, display_height))

        # Creates the flooring of the game
        self.floor_surface = pygame.image.load('flooring.png').convert()
        self.floor_surface = pygame.transform.scale(self.floor_surface, (self.platform_width, self.platform_height))

    def draw_floor(self):
        self.window.screen.blit(self.floor_surface, (self.floor_x_pos, 725))
        self.window.screen.blit(self.floor_surface, (self.floor_x_pos + 1400, 725))