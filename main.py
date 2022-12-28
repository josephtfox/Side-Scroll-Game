import pygame
import sys

# 
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 725))
    screen.blit(floor_surface, (floor_x_pos + 1400, 725))

# Initializes the game window and the name of the window just being "Side-Scoller"
pygame.init()
pygame.display.set_caption('Side-Scroller')
screen = pygame.display.set_mode((1400, 800))
clock = pygame.time.Clock()

# Creates the background image of the game 
bg_surface = pygame.image.load('Background.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (1400, 1000))

# Creates the flooring of the game
floor_surface = pygame.image.load('flooring.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (1400, 75)) 
floor_x_pos = 0

# Creating the class for the player object
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Character_Sprite.jpeg")
        self.rect = self.image.get_rect()
 
# definition of the function for moving the character
def move(self):
      pass
 
# Definition of the function to update where the character is
def update(self):
      pass
 
# Definition of the function for the attack command
def attack(self):
      pass

# Definition of the function for the jump commmand
def jump(self):
      pass


player = Player();
# 
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