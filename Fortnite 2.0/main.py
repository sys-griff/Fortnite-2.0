import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Screen")

player_img = pygame.image.load("Default.png")
player_img = pygame.transform.scale(player_img, (75, 100))
player = player_img.get_rect(center = (50, 650))

BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((135, 206, 235))
    
    screen.blit(player_img, player)

    pygame.display.flip()

pygame.quit()
sys.exit()