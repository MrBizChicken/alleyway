import pygame, random
from constants import *
import player
import random
pygame.init()
class Bricks(pygame.sprite.Sprite):
    def __init__(self, x ,y, width, height, health):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.color = (0, 255, 0)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.health = health




    def update(self):
        if self.health == 3:
            self.color = (0, 255, 0)
        elif self.health == 2:
            self.color = (255, 255, 0)
        elif self.health == 1:
            self.color = (255, 0, 0)

        self.image.fill(self.color)
        
        if self.health <= 0:
            self.kill()
