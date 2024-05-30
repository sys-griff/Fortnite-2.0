import pygame

class Gameobject:
    def __init__(self, pos, width, height, img, game):
        self.pos = pos
        self.width = width
        self.height = height
        self.img = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.game = game

    def render(self):
        img = pygame.Surface.subsurface(self.img, (0, 0, 2400//10, 160))

        self.game.screen.blit(img, self.pos)
        
        