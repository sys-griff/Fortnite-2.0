import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Screen")

FONT = pygame.font.Font("Fortnite.ttf", 150)

score = FONT.render("0", True, "black")
score_rect = score.get_rect(center = (400, 100))

restart = FONT.render("RESTART", True, "black")
restart_rect = restart.get_rect(center = (400, 600))

menu_1 = FONT.render("START", True, "black")
menu_2 = FONT.render("MENU", True, "black")
menu_title = menu_2.get_rect(center = (400, 100))
menu_start = menu_1.get_rect(center = (400, 400))

player_img = pygame.image.load("Default.png")
player_img = pygame.transform.scale(player_img, (75, 100))
player = player_img.get_rect(center = (50, 650))

grass_img = pygame.image.load("Grass.png")
grass_img = pygame.transform.scale(grass_img, (900, 200))
grass = grass_img.get_rect(center = (450, 800))

clinger_img = pygame.image.load("Clinger.png")
clinger_img = pygame.transform.scale(clinger_img, (30, 40))
clinger_list = [clinger_img.get_rect(center = (800, 680)), clinger_img.get_rect(center = (1200, 680))]

loser_img = pygame.image.load("L.png")
loser_img = pygame.transform.scale(loser_img, (300, 300))
loser = loser_img.get_rect(center = (400, 400))

collide_menu = False

collide_restart = False

fall_speed = 1
jump = True
BLUE = (0, 0, 255)

points = 0

collide = False

clock = pygame.time.Clock()

def draw_stuff():


    global points

    screen.blit(player_img, player)
    screen.blit(grass_img, grass)
    screen.blit(score, score_rect)
        
    for clinger in clinger_list:
        screen.blit(clinger_img, clinger)

def reset_stuff():
    global clinger_list

    clinger_list = [clinger_img.get_rect(center = (800, 680)), clinger_img.get_rect(center = (1200, 680))]

def play():

    global collide
    global fall_speed
    global points
    global score_rect
    global clinger
    global collide_restart
    global score

    while not collide:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if collide_restart:
            reset_stuff()
            collide_restart = False

        keys = pygame.key.get_pressed()

        for clinger in clinger_list:
            if player.colliderect(clinger):
                collide = True
    
        if keys[pygame.K_SPACE] and jump:
            fall_speed -= 15
            jump = False
    
        for clinger in clinger_list:

            clinger.x -= 7

            if clinger.x < -30:
                clinger.x = 800
                points += 1

        player.y += fall_speed

        if player.y > 600:
            jump = True
            fall_speed = 0
        else:
            fall_speed += 1

        score = FONT.render(f"{points}", True, "black")

        screen.fill((135, 206, 235))

        if collide:
            womp_womp()


        draw_stuff()

        pygame.display.update()

def main_menu():

    global collide_menu

    while not collide_menu:

        clock.tick(60)

        menu_mouse_pos = pygame.mouse.get_pos()

        screen.fill((135, 206, 235))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(menu_1, menu_start)

        if event.type == pygame.MOUSEBUTTONDOWN:
            collide_menu = menu_start.collidepoint(menu_mouse_pos)
            print("wompwomp u stink loser")

        if collide_menu:
            play()

        pygame.display.update()

def womp_womp():

    global collide_restart
    global collide
    global points

    while not collide_restart:
        clock.tick(60)

        womp_mouse_pos = pygame.mouse.get_pos()

        screen.fill((135, 206, 235))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                collide_restart = restart_rect.collidepoint(womp_mouse_pos)

        draw_stuff()
        
        screen.blit(loser_img, loser)
        screen.blit(restart, restart_rect)

        collide = False
        
        if collide_restart:
            points = 0
            play()
        
        pygame.display.update()

main_menu()

pygame.quit()
sys.exit()