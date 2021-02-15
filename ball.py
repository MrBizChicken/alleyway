import pygame, random
from constants import *
import player
pygame.init()
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = 50
        self.width = 64
        self.height = 64
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)





    def update(self):
        pass
