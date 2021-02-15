import pygame, random
from constants import *
import player
import random
pygame.init()
class Bricks(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 60
        self.height = 20
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)





    def update(self):
        pass
