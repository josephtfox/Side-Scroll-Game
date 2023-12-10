import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, window, display_width, display_height, env):
        super().__init__()

        self.player_height = 60
        self.player_width = 40
        self.player_speed = 5

        self.player_x_pos = display_width // 2
        self.player_y_pos = display_height - self.player_height
        self.player_pos = pygame.Vector2(display_width / 2, display_height / 2)

        self.is_jumping = False
        self.jump_count = 10

        # Load the character sprite sheet
        self.sprites = []
        sprite_sheet = pygame.image.load("Character_Sprite.jpeg")

        # Define the size of each frame in the sprite sheet
        frame_width, frame_height = 4, 4

        # Split the sprite sheet into individual frames
        for x in range(0, sprite_sheet.get_width(), frame_width):
            image = sprite_sheet.subsurface(pygame.Rect(x, 0, frame_width, frame_height))
            self.sprites.append(image)

        # Set the current frame and its rect
        self.current_frame = 0
        self.image = self.sprites[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (display_width // 2, display_height // 2)

    def update(self):
        # Animate the character by changing the current frame
        self.current_frame = (self.current_frame + 1) % len(self.sprites)
        self.image = self.sprites[self.current_frame]
    
    def move(self): 
        pass 