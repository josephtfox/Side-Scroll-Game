import pygame
from Environment import Environment
from Player import Player
# from SpriteSheet import Spritesheet

# Initializes the game window and the name of the window 
pygame.init()
pygame.display.set_caption('Side-Scroller')
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1400, 800
canvas = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
running = True

environment = Environment(window, DISPLAY_WIDTH, DISPLAY_HEIGHT)
player = Player(window, DISPLAY_WIDTH, DISPLAY_HEIGHT, environment)

# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)
# Fill in with the sprite sheet image
# my_spritesheet = Spritesheet('main_character_sprite_sheet.png')
# Enter the coords of where the sprite is on the sheet
main_character1 = my_spritesheet.get_sprite(0,0,128,128)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.screen.blit(environment.bg_surface, (0, 0))
    environment.floor_x_pos -= 1

    environment.draw_floor()

    if environment.floor_x_pos <= -1400:
        environment.floor_x_pos = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.player_pos.x -= 300 * environment.dt
    if keys[pygame.K_d]:
        player.player_pos.x += 300 * environment.dt

    # if player.player_pos.y < environment.platform_height - player.player_height:
    #     player.player_pos.y += 2  # Simulated gravity

    # all_sprites.draw(window.screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    canvas.blit(main_character1, (0, 0))

    environment.dt = environment.clock.tick(60) / 1000

    pygame.display.update()
    environment.clock.tick(120)