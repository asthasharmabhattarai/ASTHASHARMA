#simple and fun Python game using Pygame

import pygame
import random

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Player
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 50)
player_speed = 7

# Block
block = pygame.Rect(random.randint(0, WIDTH - 40), -40, 40, 40)
block_speed = 5

score = 0
font = pygame.font.SysFont(None, 36)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Move block
    block.y += block_speed

    # Reset block
    if block.y > HEIGHT:
        block.x = random.randint(0, WIDTH - 40)
        block.y = -40
        score += 1
        block_speed += 0.2  # Increase difficulty

    # Collision
    if player.colliderect(block):
        print("Game Over! Score:", score)
        running = False

    # Draw
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, block)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()