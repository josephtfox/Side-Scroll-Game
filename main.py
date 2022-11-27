import pygame
import sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 725))
    screen.blit(floor_surface, (floor_x_pos + 1400, 725))


pygame.init()
pygame.display.set_caption('Side-Scroller')
screen = pygame.display.set_mode((1400, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('Background.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (1400, 1000))

floor_surface = pygame.image.load('flooring.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (1400, 75))
floor_x_pos = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -1400:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
