import pygame
import random

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
BROWN = (165, 42, 42)
GREY = (50, 50, 50)

# Set the width and height of the screen [width, height]
size = (700, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Kidd Buu Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set up the player
player = pygame.Rect(50, 50, 50, 50)
player_hp = 100
player_speed = 5

# Set up the tree
tree = pygame.Rect(500, 50, 50, 50)
tree_hp = 10

# Set up the rock
rock = pygame.Rect(250, 50, 50, 50)
rock_hp = 100

#creating bullet for player
bullet = pygame.Rect(5, 5, 5, 5)

# Set up the Gold Coin
coin = pygame.Rect(random.randint(0, size[0]), random.randint(0, size[1]), 10, 10)
gold_score = 0

# Set up the experience
experience = 0
gold = 0

# Set up the main level
main_level = 1
main_level_experience = 0
main_level_experience_needed = 10

# Set up the font
font = pygame.font.SysFont(None, 25)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
        
        # shoot circle object
    if keys[pygame.K_SPACE]:
        circle = pygame.draw.circle(screen, RED, (player.x + player.width // 2, player.y + player.height // 2), 10)
        if circle.colliderect(tree):
            tree_hp -= 2
            if tree_hp <= 0:
                tree_hp = 0
                tree.width = 0
                tree.height = 0
                tree.x = -100
                tree.y = -100
    # shoot straight object
    if keys[pygame.K_SPACE]:
        bullet = pygame.draw.circle(screen, BLACK, (player.x + player.width // 2, player.y), 5)
        bullet.y -= 10
        if bullet.colliderect(tree):
            tree_hp -= 2
            if tree_hp <= 0:
                tree_hp = 0
                tree.width = 0
                tree.height = 0
                tree.x = -100
                tree.y = -100
    # update bullet position
                if bullet.y < 0:
                    bullet.width = 0
                    bullet.height = 0
                else:
                    bullet.y -= 10
        
    # collect gold coin
    if player.colliderect(coin):
        gold += 1
        coin.x = random.randint(0, size[0] - coin.width)
        coin.y = random.randint(0, size[1] - coin.height)
        
        
     # Check if player has hit the rock
    if player.colliderect(rock):
        experience -= 1
        main_level_experience -= -1
        print(f"Experience: {experience}")
        if main_level_experience >= main_level_experience_needed:
            main_level += -1
            main_level_experience = -1
            print(f"Main Level: {main_level}")
        # Check if the player has hit the tree
    if player.colliderect(tree):
        experience += 1
        main_level_experience += 1
        print(f"Experience: {experience}")
        if main_level_experience >= main_level_experience_needed:
            main_level += 1
            main_level_experience_needed = int(main_level_experience_needed * 1.1)
            main_level_experience = 0
            print(f"Main Level: {main_level}")
            
    

    # --- Drawing code should go here
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, BROWN, tree)
    pygame.draw.rect(screen, GREY, rock)
    pygame.draw.rect(screen, GOLD, coin)
    pygame.draw.rect(screen, RED, bullet)
    
    # Draw the experience score in the top right corner of the screen
    score_text = font.render(f"Experience: {experience}", True, BLACK)
    screen.blit(score_text, (size[0] - score_text.get_width(), 0))
    
    # Draw the gold score in the top right of the screen
    score_gold = font.render(f"Gold: {gold}", True, RED)
    screen.blit(score_gold, (size[0] - score_gold.get_width(), 15))
    

    # Draw the main level in the top left corner of the screen
    level_text = font.render(f"Main Level: {main_level}", True, BLACK)
    screen.blit(level_text, (0, 0))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
