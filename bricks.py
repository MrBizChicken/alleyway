import pygame, random
from constants import *
import player
pygame.init()
class Bricks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT // 2
        self.width = 60
        self.height = 20
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.score = 0




    def update(self):
        pass
