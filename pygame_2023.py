import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 980
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the player's health
player_health = 100

# Set the NPC's health
npc_health = 100

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.health = player_health
        self.speed = 1 # Change this value to adjust the player's speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

# Define the NPC class
class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 4, screen_height // 4)
        self.health = npc_health
        self.speed = 1 # Change this value to adjust the NPC's speed

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if self.rect.right > screen_width or self.rect.left < 0:
            self.speed *= -1
        if self.rect.bottom > screen_height or self.rect.top < 0:
            self.speed *= -1

# Create the player and NPC sprites
player = Player()
npc = NPC()

# Create the sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player, npc)

# Set the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprites
    all_sprites.update()

    # Draw the sprites
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    # Draw the health bars
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, player.health, 10))
    pygame.draw.rect(screen, (0, 255, 0), (10, 30, npc.health, 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
